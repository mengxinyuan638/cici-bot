from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import json




qd = on_regex(pattern = r'^我的钱包$')

@qd.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    qq_id = str(event.user_id)
    await search_qq(qq_id)
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    lovelive_send = await notice()
    await qd.send(Message(str(lovelive_send)))

send = 0
async def search_qq(qq):
    global send
    file_name = 'coints.json'
    with open(file_name) as f:
        data_user = json.load(f)
    money = data_user[f'{qq}']
    send = f'您的金币共有{money}个'

async def notice():
    news = send
    return news