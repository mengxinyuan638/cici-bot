from nonebot.plugin.on import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests
import json

'''
土味情话 调用API https://api.uomg.com/api/rand.qinghua?format=json
正则命令:土味情话
'''
random_love = on_regex ( pattern=r"^土味情话$" )


@random_love.handle ()
async def love(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_love ()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await random_love.send ( Message ( msg ) )


async def get_love():
    url = 'https://api.uomg.com/api/rand.qinghua?format=json'
    get_data = requests.get ( url )
    # print(get_data)
    get_json = json.loads ( get_data.text )
    get_content = get_json[ 'content' ]
    # print(get_content)
    return get_content
