"""
作者:萌新源
时间:2022/3/30
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处

"""
from nonebot.plugin.on import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment
import requests
import json

dmtp = on_regex(pattern = r"^动漫壁纸$")

@dmtp.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await tx()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await dmtp.send(MessageSegment.image(lovelive_send))


async def tx():
    url = 'https://api.juncikeji.xyz/api/dmbz.php'
    x = requests.get(url)
    wb = x.text.strip()
# print(hua)
    return wb
