from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests

gg = on_regex(pattern = r'^查看公告$')

@gg.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await xi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await gg.send(Message(lovelive_send))


async def xi():
    url = 'http://www.juncikeji.xyz/gg.php'
    hua = requests.get(url=url,timeout=20)
    # print(hua)
    data = hua.text
    data = data + '\npower by 萌新源'
    print(data)
    return data
