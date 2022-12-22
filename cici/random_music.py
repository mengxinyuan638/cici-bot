from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Message, Event,MessageSegment
import requests
import json
import re
'''
随机歌曲 调用API https://api.uomg.com/api/rand.music?sort=热歌榜&format=json
正则命令:随机歌曲
'''
random_music = on_regex(pattern = r'^随机歌曲$')

@random_music.handle()
async def r_music(bot: Bot, event: Event, state: T_State):
    get_music = await music()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    # for i in get_music:
    await random_music.send(get_music)


async def music():
    url = 'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'
    get_data = requests.get(url)
    get_json = json.loads(get_data.text)
    # print(get_json)
    get_dt = get_json['data']
    url = get_dt['url']
    url = re.findall(r'id=(.+?)$',url)
    wb = MessageSegment.music(type_='163',id_=url[0])
    return wb
