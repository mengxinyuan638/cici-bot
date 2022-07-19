from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests

xljt = on_regex(pattern = r'^心灵鸡汤$')

@xljt.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await xi()
    await xljt.send(Message(lovelive_send))


async def xi():
    url = 'http://api.yanxi520.cn/api/xljtwr.php?charset=utf-8http://api.yanxi520.cn/api/xljtwr.php?encode=txt'
    hua = requests.get(url=url)
    # print(hua)
    data = hua.text
    # print(data)
    return data
