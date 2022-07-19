from nonebot import on_keyword, on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests

tgrj = on_regex(pattern = r'^舔狗日记$')

@tgrj.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await xi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await tgrj.send(Message(lovelive_send))


async def xi():
    url = 'http://api.yanxi520.cn/api/tiangou.php'
    hua = requests.get(url=url)
    # print(hua)
    data = hua.text
    # print(data)
    return data
