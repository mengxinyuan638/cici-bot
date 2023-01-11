from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests
'''
每日一言 调用API https://api.juncikeji.xyz/api/mryy.php
命令:每日一言
'''
mryy = on_regex(pattern = r'^每日一言$')

@mryy.handle()
async def yy(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_yy()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await mryy.send(Message(msg))


async def get_yy():
    url = 'https://api.juncikeji.xyz/api/mryy.php'
    get_data = requests.get(url=url,timeout=20)
    #print(get_data)
    get_txt = get_data.text
    #print(data)
    return get_txt
