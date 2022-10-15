from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests

'''
随机一言 调用API http://api.weijieyue.cn/api/yy/api.php
正则命令:随机一言
'''
random_sentence = on_regex ( pattern=r'^随机一言$' )


@random_sentence.handle ()
async def sentence(bot: Bot, event: GroupMessageEvent, state: T_State):
    url = 'http://api.weijieyue.cn/api/yy/api.php'
    get_data = requests.get ( url=url, timeout=20 )
    # print(get_data)
    get_txt = get_data.text
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await random_sentence.send ( Message ( get_txt ) )
