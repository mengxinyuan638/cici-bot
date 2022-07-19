from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot,Message,Event
import requests
import json

random_head = on_regex(pattern = r'^随机头像$')

@random_head.handle()
async def sj(bot: Bot, event: Event, state: T_State):
    get_img = await head()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await random_head.send(Message(get_img))


async def head():
    url = 'https://www.yuanxiapi.cn/api/touxiang/?format=json'
    get_data = requests.get(url)
    get_json = json.loads(get_data.text)
    # print(get_json)
    img = get_json['imgurl']
    wb = f"[CQ:image,file={img}]"
    return wb