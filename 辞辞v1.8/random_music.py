from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Message, Event,MessageSegment
import requests
import json
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
    await random_music.send ( MessageSegment.record ( get_music[ 0 ] ) )
    await random_music.send(MessageSegment.image(get_music[1]))
    await random_music.send ( get_music[ 2 ]  )


async def music():
    url = 'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'
    get_data = requests.get(url)
    get_json = json.loads(get_data.text)
    # print(get_json)
    get_dt = get_json['data']
    url = get_dt['url']
    tomp3=url+".mp3"
    name = get_dt['name']
    img = get_dt['picurl']
    author = get_dt['artistsname']

    ms = f"曲名:{name}\n歌手:{author}\nPower by 萌新源"
    # wb = f"[CQ:music,type=custom,url={url},audio={url},title={name},image={img},content={ms}]"
    wb=[tomp3,img,ms]
    return wb
