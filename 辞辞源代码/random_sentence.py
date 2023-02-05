from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests

'''
随机一言 调用API https://api.juncikeji.xyz/api/mryy.php
正则命令:随机一言
'''
random_sentence = on_regex ( pattern=r'^随机一言$' )


@random_sentence.handle ()
async def sentence(bot: Bot, event: GroupMessageEvent, state: T_State):
    url = 'https://api.juncikeji.xyz/api/mryy.php'
    get_data = requests.get ( url=url, timeout=10 )
    get_txt = get_data.text
    await random_sentence.send ( Message ( get_txt ) )
