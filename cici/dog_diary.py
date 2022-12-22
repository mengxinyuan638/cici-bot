from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests

'''
条狗日记 调用API https://api.juncikeji.xyz/api/tgrj.php
正则命令:舔狗日记
'''
dog_diary = on_regex ( pattern=r'^舔狗日记$' )


@dog_diary.handle ()
async def dog(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_diary ()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await dog_diary.send ( Message ( msg ) )


async def get_diary():
    url = 'https://api.juncikeji.xyz/api/tgrj.php'
    get_data = requests.get ( url=url )
    # print(get_data)
    get_txt = get_data.text
    # print(get_txt)
    return get_txt
