from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests
'''
讲个笑话 调用API http://api.juncikeji.xyz/api/qwxh.php
命令:讲个笑话
'''
random_joke = on_regex(pattern = r'^讲个笑话$')

@random_joke.handle()
async def joke(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_joke()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await random_joke.send(Message(msg))


async def get_joke():
    url = 'http://api.juncikeji.xyz/api/qwxh.php'
    get_data = requests.get(url=url,timeout=20)
    #print(get_data)
    get_txt = get_data.text
    #print(data)
    return get_txt
