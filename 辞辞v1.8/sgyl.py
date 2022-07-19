from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests

twqh = on_regex(pattern = r'^随机一言$')

@twqh.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    lovelive_send = await xi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await twqh.send(Message(lovelive_send))


async def xi():
    url = 'http://api.weijieyue.cn/api/yy/api.php'
    hua = requests.get(url=url,timeout=20)
    # print(hua)
    data = hua.text
    # print(data)
    return data
