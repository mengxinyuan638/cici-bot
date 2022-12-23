"""
作者:萌新源
时间:2022/3/30
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处
"""
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, Event
import requests

'''
原神角色查询 调用API https://wanghun.top/api/v5/yuanshen.php?msg=xxx
命令:#元神+角色名字
'''
yuanshen = on_keyword ( {'#原神'} )


@yuanshen.handle ()
async def characte(bot: Bot, event: Event, state: T_State):
    ansey = str ( event.get_message () ).strip ()
    ansec = ansey.strip ( '#原神' )
    requests.packages.urllib3.disable_warnings ()  # 跳过证书验证
    url = f'https://wanghun.top/api/v5/yuanshen.php?msg={ansec}'
    get_data = requests.get ( url, verify=False )  # verify=False 默认为True,设为False,这是对于证书不验证进行访问
    get_txt = get_data.text
    html = '<br>'
    msg = get_txt
    if html in get_txt:
        msg = get_txt.replace ( html, '\n' )
    await yuanshen.finish ( Message ( f'{msg}' ) )
