from nonebot import on_regex,on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
from .source import buy,news
from .search import search_bocket,search_use
from .use import useit
from .success import set_success,suc_news
import json
import re
import time as t
import random



store = on_regex(pattern = r'^金币商城$')
boom = on_regex(pattern = r'^炸弹$')
zhuce = on_regex(pattern = r'^注册商店账户$')
bocket = on_regex(pattern = r'^查看背包$')
qb = on_regex(pattern = r'^我的钱包$')

@qb.handle()
async def q(bot: Bot, event: GroupMessageEvent, state: T_State):
    qq_id = event.user_id
    num = await search_qb(qq_id)
    await qb.send(f"您的钱包共有{num}枚金币")

async def search_qb(qq_id) -> int:
    """查询指定用户钱包余额"""
    qq_id = str(qq_id)
    file = 'coints.json'
    read = open(file,'r')
    data = json.load(read)
    conits = int(data[qq_id])
    return conits

@store.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    data_cd = '金币商店\n1.炸弹(单价:$70)\n——————————————\nps:发送商品名称可以获得使用方法\n购买商品指令：买@商品名\n首次使用需发送：注册商店账户\n来完成个人账户初始化\n查看背包内物品请发送：查看背包' 
    await store.finish(message=Message(f'{data_cd}'))

@boom.handle()
async def bom(bot: Bot, event: GroupMessageEvent, state: T_State):
    data = '发送指令 炸@某人就可以把他/她炸晕，不过不要滥用，小心被报复'
    await boom.finish(message=Message(f'{data}'))

@zhuce.handle()
async def zhuce(bot: Bot, event: GroupMessageEvent, state: T_State):
    qq_id = str(event.user_id)
    await search_qq(qq_id)
    if b == True:
        await boom.finish(message=Message('你已经注册过了，无需再注册'))
    else:
        await write_qq(qq_id)
        await boom.finish(message=Message('注册成功'))

@bocket.handle()
async def beibao(bot: Bot, event: GroupMessageEvent, state: T_State):
    qq_id = str(event.user_id)
    qq_id_int = int(qq_id)
    await search_qq(qq_id)
    if b == True:
        message = await search_bocket(qq_id_int)
        await boom.finish(message=Message(str(message)))
    else:
        await boom.finish(message=Message('你还没有注册'))


async def search_qq(qq):#读取个人商店数据
    global data_store
    global b
    b = 'null'#判断变量,用于判断是否注册
    file2_name = 'store.json'
    with open(file2_name) as f:
        data_store = json.load(f)
    if qq in data_store:
        b = True#已注册
    else:
        b = False#非注册
    

async def write_qq(qq):#初始化个人商店数据
    file2_name = 'store.json'
    goods = {'炸弹':'0'}
    dic = {f'{qq}':goods}
    data_dict = dict(data_store)
    data_dict.update(dic)#更新商店数据
    with open(file2_name,'w') as f:
        json.dump(data_dict,f,ensure_ascii=False)

#############购买商品##############
buy_user = on_keyword({'买@'})
money = 'null'
data_user = 'null'

@buy_user.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    anses = str(event.get_message()).strip()
    ansek = str(anses.strip('买@'))#获取商品名称
    qq_id = int(event.user_id)
    goods = {'炸弹':'70'}#商品数据
    price = int(goods[f'{ansek}'])
    await search_qq_money(qq_id)
    await buy(money,data_user2,qq_id,price,data_store2,ansek)
    _news_ = await news()
    p = goods[f'{ansek}']
    await buy_user.finish(message=Message(f'{_news_}'))

    


async def search_qq_money(qq):
    global money
    global data_user2
    global data_store2
    file_name = 'coints.json'
    file2_name = 'store.json'
    with open(file_name) as f:
        data_user2 = json.load(f)
    with open(file2_name) as f:
        data_store2 = json.load(f)
    money = int(data_user2[f'{qq}'])

###############使用商品部分###############
use_bom = on_keyword({'#炸'})
@use_bom.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    time_last = random.randint(0,15)
    time = time_last*60
    anses = str(event.get_message()).strip()
    ansek = str(anses.strip('#炸'))#获取对象
    data = str(ansek)
    goods_name = '炸弹'
    qq_id = event.user_id
    qq = re.findall(r'qq=(.+?)]',data)
    qq = int(qq[0])
    number = await search_use(qq_id,goods_name)
    if number >= 1:
        goods_number_now = number - 1
        await useit(qq_id,goods_name,goods_number_now)
        if time == 0:
            await boom.finish(message=Message('本次轰炸没有对对方造成伤害'))
        else:
            local_time = t.localtime(event.time)
            use_time = int(t.strftime('%M',local_time))
            file2_name = 'usedata.json'
            with open(file2_name) as f:
                data_store_person = dict(json.load(f))
            
            if str(qq_id) in data_store_person.keys():#判断用户是否在列表内
                qq_data = data_store_person[f'{qq_id}']
            else:#不在，则新增
                print('被执行的')
                print(qq_id in data_store_person.keys())
                print(data_store_person.keys())
                data_store_person[qq_id] = {'炸弹':{'num':0,'time':99}}
                with open(file2_name,'w') as f:#写入新用户
                    json.dump(data_store_person,f,ensure_ascii=False)
                with open(file2_name) as f:
                    data_store_person = dict(json.load(f))
                qq_data = data_store_person[f'{qq_id}']


            
            usetime2 = int(qq_data['炸弹']['time'])
            zhadan_number = int(qq_data['炸弹']['num'])
            if qq_data['炸弹']['time'] == 99:
                qq_data['炸弹']['time'] = use_time
                data_store_person[f'{qq_id}'] = qq_data#写入数据
            usetime_jian = int(use_time - usetime2)

            if zhadan_number < 5:
                qq_data['炸弹']['num'] = zhadan_number + 1
                data_store_person[f'{qq_id}'] = qq_data#写入数据
                with open(file2_name,'w') as f:
                    json.dump(data_store_person,f,ensure_ascii=False)
            elif zhadan_number == 5 and usetime_jian <= 1:
                qq_data['炸弹']['num'] = 0#清空
                qq_data['炸弹']['time'] = 99
                data_store_person[f'{qq_id}'] = qq_data
                with open(file2_name,'w') as f:
                    json.dump(data_store_person,f,ensure_ascii=False)
                await set_success(qq_id,'炸弹狂人')
                send = await suc_news()
                await use_bom.send(Message(str(send)))
            else:
                qq_data['炸弹']['num'] = 0#清空
                qq_data['炸弹']['time'] = 99
                data_store_person[f'{qq_id}'] = qq_data
                with open(file2_name,'w') as f:
                    json.dump(data_store_person,f,ensure_ascii=False)

            await bot.set_group_ban(group_id=event.group_id,user_id=qq,duration=time)
            await use_bom.finish(message=f'本次轰炸对\nQQ:{qq}\n造成禁言{time_last}分钟的伤害')
            
    else:
        await use_bom.finish(message=f'您的道具数量不足，快去金币商城购买吧')

