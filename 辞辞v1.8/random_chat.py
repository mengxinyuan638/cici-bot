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
from nonebot.adapters.onebot.v11 import Bot, Message, Event
import requests
import json

'''
辞辞聊天机器人 调用青云可API http://api.qingyunke.com/
命令:/
'''

cici = on_keyword ( {'/'} )


@cici.handle ()
async def chat(bot: Bot, event: Event, state: T_State):
    anses = str ( event.get_message () ).strip ()
    ansek = anses.strip ( '/' )
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={ansek}'
    get_data = requests.get ( url )
    get_json = json.loads ( get_data.text )
    get_content = get_json[ 'content' ]
    name = '菲菲'
    characters = '{br}'
    if name in get_content:
        msg = get_content.replace ( '菲菲', '辞辞' )
    if characters in get_content:
        msg = get_content.replace ( '{br}', "\n" )
    await cici.finish ( Message ( f'{msg}' ) )
