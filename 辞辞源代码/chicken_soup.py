from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests
import json

'''
心灵鸡汤 调用API https://api.mxycn.cn/api/xljt.php
正则命令:心灵鸡汤
writen by mengxinyuan at 2023/2/5
CopyRight© 2023 萌新源
'''
chicken_soup = on_regex(pattern=r'^心灵鸡汤$')


@chicken_soup.handle()
async def chicken(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_chicken()
    await chicken_soup.send(Message(msg))


async def get_chicken():
    url = 'https://api.mxycn.cn/api/xljt.php'
    get_data = requests.get(url)
    get_txt = json.loads(get_data.text)
    get_txt = get_txt['data']['content']
    return get_txt
