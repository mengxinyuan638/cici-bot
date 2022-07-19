from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment
import requests
import re
import json

sjgq = on_regex(pattern = r'^随机歌曲$')

@sjgq.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await xi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await sjgq.send(Message(lovelive_send))


async def xi():
    url = 'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'
    k = requests.get(url)
    hua2 = json.loads(k.text)
# print(hua)
    hua = hua2['data']
    url = hua['url']
    name = hua['name']
    img = hua['picurl']
    mz = hua['artistsname']
    ms = f"歌手:{mz}\nPower by 萌新源"
    wb = f"[CQ:music,type=custom,url={url},audio={url},title={name},image={img},content={ms}]"
    return wb

