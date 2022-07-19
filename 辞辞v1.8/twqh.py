from nonebot.plugin.on import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests
import json

sjyl = on_regex(pattern = r"^土味情话$")

@sjyl.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await xi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await sjyl.send(Message(lovelive_send))


async def xi():
    url = 'https://api.uomg.com/api/rand.qinghua?format=json'
    hua1 = requests.get(url=url)
    # print(hua)
    hua = json.loads(hua1.text)
    data = hua['content']
    # print(data)
    return data
