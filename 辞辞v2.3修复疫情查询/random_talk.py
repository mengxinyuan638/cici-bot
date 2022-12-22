from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Message, Event
import requests

'''
调用墨色网API 随机语录 https://api.sunweihu.com/api/yan/
利用CQ码将文字转语音
命令:#说句话
'''
talk = on_keyword ( {'#说句话'} )


@talk.handle ()
async def r_talk(bot: Bot, event: Event, state: T_State):
    url = 'https://api.sunweihu.com/api/yan/api.php'
    get_data = requests.get ( url )
    msg = get_data.text
    random_talk = f"[CQ:tts,text={msg}]"
    await talk.send ( Message ( random_talk ) )
