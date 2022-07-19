from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests

sjxh = on_regex(pattern = r'^讲个笑话$')

@sjxh.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await xi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await sjxh.send(Message(lovelive_send))


async def xi():
    url = 'http://api.juncikeji.xyz/api/qwxh.php'
    hua = requests.get(url=url,timeout=20)
    #print(hua)
    data = hua.text
    #print(data)
    return data
