from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests

'''
萌新源专用公告API
命令:查看公告
'''
get_advertise = on_regex ( pattern=r'^查看公告$' )


@get_advertise.handle ()
async def advertise(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await advertise_API ()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await get_advertise.send ( Message ( lovelive_send ) )


async def advertise_API():
    url = 'http://www.juncikeji.xyz/gg.php'
    get_data = requests.get ( url=url, timeout=20 )
    # print(get_data)
    get_txt = get_data.text
    get_txt = get_txt + '\npower by 萌新源'
    print ( get_txt )
    return get_txt
