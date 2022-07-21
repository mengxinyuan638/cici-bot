"""
作者:萌新源
时间:2022/4/1
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处
"""
'''
翻译 调用API http://hm.suol.cc/API/fy.php?msg=
命令:#翻译
'''
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, Event
import requests

translate = on_keyword ( {'#翻译'} )


@translate.handle ()
async def sj(bot: Bot, event: Event, state: T_State):
    get_msg = str ( event.get_message () ).strip ()
    get_msg = get_msg.strip ( '#翻译' )
    url = f'http://hm.suol.cc/API/fy.php?msg={get_msg}'
    get_data = requests.get ( url )
    get_txt = get_data.text
    mxy = '——Power by 萌新源'
    msg = f'{get_txt}\n{mxy}'
    await translate.finish ( Message ( f'{msg}' ) )
