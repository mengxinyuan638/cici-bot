"""
本模块实现bilibili qq群登录
"""
import asyncio
import json
import pathlib
import os
import httpx
import qrcode
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, MessageSegment
from PIL import Image, ImageDraw, ImageFont

bili_login = on_regex(pattern=r'^申请哔哩登录$')
data_person = on_regex(pattern=r'^哔哩个人信息$')
bili_menu = on_regex(pattern=r'^哔哩菜单$')


@bili_login.handle()
async def code(bot: Bot, event: GroupMessageEvent, state: T_State):
    apply_type = await read_apply(event.user_id)
    if apply_type == 'False':
        await change_apply(event.user_id, 'T')
        data = await make_qrcode(event.user_id)
        msg = data['msg']  # 获取提示文字
        if data['code'] == '200':
            await bili_login.send(Message(msg))
            await bili_login.send(MessageSegment.image(pathlib.Path(f"bilibili_login/qrcode/{event.user_id}.png")))
            await check_login(data['token'], event.user_id)
        else:
            await bili_login.send(Message(msg))
    else:
        await bili_login.send(Message(f'[CQ:at,qq={event.user_id}]您还有正在使用的二维码，请等待二维码失效后重新申请'))


@data_person.handle()
async def person(bot: Bot, event: GroupMessageEvent, state: T_State):
    """获取个人信息"""
    url = 'https://api.bilibili.com/x/web-interface/nav'
    cookie = await load_cookie(event.user_id)
    async with httpx.AsyncClient() as client:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        data = await client.get(url=url, headers=headers, cookies=cookie)
    data = data.json()
    person_data = data['data']  # 获取个人信息
    user_name = person_data['uname']
    coint_num = str(person_data['money'])
    level = str(person_data['level_info']['current_level'])
    face = str(person_data['face'])
    url = await draw_card(event.user_id, user_name, coint_num, level, face)
    await data_person.send(MessageSegment.image(pathlib.Path(url)))

@bili_menu.handle()
async def menu(bot: Bot, event: GroupMessageEvent, state: T_State):
    """哔哩哔哩菜单"""
    menu_msg = "申请哔哩登录\n哔哩个人信息"
    await bili_menu.send(Message(menu_msg))


async def draw_card(id, name, coint, level, face) -> str:
    """绘制资料卡片"""
    async with httpx.AsyncClient() as client:
        """下载头像到本地"""
        face_data = await client.get(face)
        try:
            with open(f'./bilibili_login/pitcure/{id}/face.png', 'wb') as f:
                f.write(face_data.content)
        except FileNotFoundError:
            os.mkdir(f'./bilibili_login/pitcure/{id}')
            with open(f'./bilibili_login/pitcure/{id}/face.png', 'wb') as f:
                f.write(face_data.content)
    card_way = './bilibili_login/pitcure/card.png'
    face = await cut_img(f'./bilibili_login/pitcure/{id}/face.png') #剪裁图片
    face.save(f'./bilibili_login/pitcure/{id}/face.png')
    card = Image.open(card_way)  # 获取card对象
    face_img = Image.open(f'./bilibili_login/pitcure/{id}/face.png') #获取头像
    draw = ImageDraw.Draw(card)
    ft = ImageFont.truetype("./bilibili_login/font/cn.ttf", 90)
    name_wz = (1330, 690)  # 绘制名字的坐标
    coint_wz = (1330, 870)  # 绘制硬币的坐标
    level_wz = (1330, 1080)  # 绘制等级坐标
    face_wz = (255, 530)  # 绘制头像坐标
    draw.text(name_wz, name, font=ft, fill='black')  # 绘制名字
    draw.text(coint_wz, coint, font=ft, fill='black')  # 绘制硬币
    draw.text(level_wz, level, font=ft, fill='black')  # 绘制等级
    card.paste(face_img, face_wz)  # 绘制头像
    card_url = f'./bilibili_login/pitcure/{id}/preson.png'
    try:
        card.save(card_url)
    except FileNotFoundError:
        os.mkdir(f'./bilibili_login/pitcure/{id}')
        card.save(card_url)
    return card_url


async def cut_img(fpath):
    x = 300
    r = int(x / 2)

    # turn src image to square with x width
    img_src = Image.open(fpath).convert("RGBA")
    img_src = img_src.resize((x, x), Image.ANTIALIAS)

    # create a new pinture which is used for return value
    img_return = Image.new('RGBA', (x, x), (255, 255, 255, 0))

    # create a white picture,alpha tunnuel is 100% transparent
    img_white = Image.new('RGBA', (x, x), (255, 255, 255, 0))

    # create the objects link to the pixel matrix of img
    p_src = img_src.load()
    p_return = img_return.load()
    p_white = img_white.load()

    # set the pixels of the return picture
    for i in range(x):
        for j in range(x):
            lx = abs(i - r)
            ly = abs(j - r)
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5

            if l < r:
                p_return[i, j] = p_src[i, j]
            if l > r:
                p_return[i, j] = p_white[i, j]
    return img_return

async def get_qrurl() -> list:
    """返回qrcode链接以及token"""
    async with httpx.AsyncClient() as client:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        url = 'https://passport.bilibili.com/x/passport-login/web/qrcode/generate?source=main-fe-header'
        data = await client.get(url=url, headers=headers)
    total_data = data.json()
    qrcode_url = total_data['data']['url']
    qrcode_key = total_data['data']['qrcode_key']
    data = {}
    data['url'] = qrcode_url
    data['qrcode_key'] = qrcode_key
    return data


async def make_qrcode(qq_id) -> dict:
    """制作二维码"""
    data = await get_qrurl()
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data['url'])
    qr.make(fit=True)
    # fill_color和back_color分别控制前景颜色和背景颜色，支持输入RGB色，注意颜色更改可能会导致二维码扫描识别失败
    img = qr.make_image(fill_color="black")
    try:
        img.save(f'./bilibili_login/qrcode/{qq_id}.png')
    except FileNotFoundError:
        """当未找到项目依赖文件夹则创建"""
        os.mkdir('./bilibili_login/')
        os.mkdir('./bilibili_login/qrcode')
        img.save(f'./li_login/qrcode/{qq_id}.png')
    file_check = os.path.exists(f'./bilibili_login/qrcode/{qq_id}.png')
    if file_check:
        """文件存在"""
        result = {'code': '200', 'msg': f'[CQ:at,qq={qq_id}]二维码已生成，请扫码登录', 'token': data['qrcode_key']}
    else:
        result = {'code': '200', 'msg': f'[CQ:at,qq={qq_id}]未知错误，二维码没有生成，请再试一次'}
    return result


async def check_login(token, id):
    """请求二维码状态"""
    checker = 0
    while True:
        async with httpx.AsyncClient() as client:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
            }
            url = f"https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={token}&source=main-fe-header"
            data = await client.get(url=url, headers=headers)  # 请求二维码状态
            data = json.loads(data.text)
        code = int(data['data']['code'])
        if code == 86101:
            """未扫码"""
            result = '未扫码'
        elif code == 86090:
            if checker == 0:
                """已扫描，未确认"""
                result = f'[CQ:at,qq={id}]已扫描，请尽快确认'
                await bili_login.send(Message(result))
                await change_apply(id, 'F')
                checker = 1
        elif code == 0:
            """确认登录"""
            result = f'[CQ:at,qq={id}]您已成功登录'
            cookie = dict(client.cookies)
            await bili_login.send(Message(result))
            await change_apply(id, 'F')
            await sav_cookie(cookie, id)
            break
        elif code == 86038:
            """二维码已失效"""
            result = f'[CQ:at,qq={id}]二维码已失效，如果您还未登录请重新申请'
            await bili_login.send(Message(result))
            await change_apply(id, 'F')
            break
        await asyncio.sleep(2)


async def read_apply(id) -> str:
    """用于读取请求状态"""
    try:
        data = open(f'./bilibili_login/{id}.txt', 'r').read()
    except FileNotFoundError:
        """写入True表示正在申请，无法申请新的"""
        file = open(f'./bilibili_login/{id}.txt', 'w')
        file.write('False')
        data = 'False'
    return data


async def change_apply(id, type):
    """用于修改请求状态"""
    if type == 'T':
        """修改状态为True"""
        file = open(f'./bilibili_login/{id}.txt', 'w')
        file.write('True')
    else:
        """修改状态为False"""
        file = open(f'./bilibili_login/{id}.txt', 'w')
        file.write('False')


async def sav_cookie(data, id):
    """用于储存cookie"""
    try:
        with open(f'./bilibili_login/cookie/{id}.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)
    except FileNotFoundError:
        os.mkdir('./bilibili_login/cookie')
        with open(f'./bilibili_login/cookie/{id}.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)


async def load_cookie(id) -> dict:
    """用于加载cookie"""
    try:
        file = open(f'./bilibili_login/cookie/{id}.json', 'r')
        cookie = dict(json.load(file))
    except FileNotFoundError:
        msg = '未查询到用户文件，请确认资源完整'
        cookie = 'null'
        await bili_login.send(msg)
    return cookie
