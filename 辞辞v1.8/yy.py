from nonebot import on_command, on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot,Message,MessageSegment,Event
import requests
from nonebot.rule import to_me
from nonebot import on_regex



test = on_keyword({'#说句话'})


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    ms = await ma()
    chuo = f"[CQ:tts,text={ms}]"
    await test.send(Message(chuo))


async def ma():
    url = 'https://api.sunweihu.com/api/yan/api.php'
    resp = requests.get(url)
    return resp.text

