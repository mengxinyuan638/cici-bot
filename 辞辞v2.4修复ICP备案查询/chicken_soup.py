from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests

'''
心灵鸡汤 调用API http://api.yanxi520.cn/api/xljtwr.php?charset=utf-8http://api.yanxi520.cn/api/xljtwr.php?encode=txt
正则命令:心灵鸡汤
'''
chicken_soup = on_regex ( pattern=r'^心灵鸡汤$' )


@chicken_soup.handle ()
async def chicken(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_chicken ()
    await chicken_soup.send ( Message ( msg ) )


async def get_chicken():
    url = 'http://api.yanxi520.cn/api/xljtwr.php?charset=utf-8http://api.yanxi520.cn/api/xljtwr.php?encode=txt'
    get_data = requests.get ( url )
    # print(get_data)
    get_txt = get_data.text
    # print(get_txt)
    return get_txt
