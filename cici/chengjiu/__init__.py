from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import time
import json
import random



qd = on_regex(pattern = r'^$')

@qd.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    print()