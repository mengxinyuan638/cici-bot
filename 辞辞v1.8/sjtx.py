from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment
import requests
import json

sjgq = on_regex(pattern = r'^随机头像$')

@sjgq.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await tx()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await sjgq.send(Message(lovelive_send))


async def tx():
    url = 'https://www.yuanxiapi.cn/api/touxiang/?format=json'
    x = requests.get(url)
    hua = json.loads(x.text)
# print(hua)
    img = hua['imgurl']
    wb = f"[CQ:image,file={img}]"
    return wb
