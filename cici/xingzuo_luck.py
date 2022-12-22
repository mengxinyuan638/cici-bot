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
星座查询 调用API http://hm.suol.cc/API/xzys.php?msg=
命令:#星座天蝎座 #星座巨蟹座
'''

xingzuo = on_keyword ( {'#星座'} )


@xingzuo.handle ()
async def xz(bot: Bot, event: Event, state: T_State):
    get_msg = str ( event.get_message () ).strip ()
    get_msg = get_msg.strip ( '#星座' )
    url = f'http://hm.suol.cc/API/xzys.php?msg={get_msg}'
    get_data = requests.get ( url )
    msg = get_data.text
    html = '{br}'
    n = '\n'
    if html in msg:
        msg = msg.replace ( html, n )
    await xingzuo.finish ( Message ( f'{msg}' ) )
