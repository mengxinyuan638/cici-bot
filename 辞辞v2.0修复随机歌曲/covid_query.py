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
疫情查询 调用API http://api.yanxi520.cn/api/virus.php?msg=
命令:#疫情+城市
'''
covid = on_keyword ( {'#疫情'} )


@covid.handle ()
async def query(bot: Bot, event: Event, state: T_State):
    get_city = str ( event.get_message () ).strip ()
    get_city = get_city.strip ( '#疫情' )
    url = f'http://api.yanxi520.cn/api/virus.php?msg={get_city}'
    get_data = requests.get ( url )
    msg = get_data.text
    html = '{br}'
    n = '\n'
    if html in msg:
        msg = msg.replace ( html, n )
    await covid.finish ( Message ( f'{msg}' ) )
