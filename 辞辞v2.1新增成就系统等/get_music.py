from nonebot import on_command, get_driver
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
import requests
from nonebot.log import logger

'''
命令:网易云+歌名
默认只发送歌曲，可在evn中配置
music_song=True/False(歌曲开关)
music_record=True/False(音频开关)
'''
music_163 = on_command ( "网易云" )
try:
    music_song = get_driver ().config.music_song
except Exception as e:
    music_song = True
try:
    music_record = get_driver ().config.music_record
except Exception as e:
    music_record = False


@music_163.handle ()
async def search_163(bot: Bot, event: Event, state: T_State):
    get_msg = str ( event.get_message () ).strip ()
    get_msg = get_msg.strip ( '网易云' )
    logger.info ( "歌名:" + get_msg )
    # https://music.163.com/api/cloudsearch/pc?s=xxx&type=1&offset=0&limit=1
    url = "https://music.163.com/api/cloudsearch/pc?s=" + f"{get_msg}" + "&type=1&offset=0&limit=1"
    get_data = requests.get ( url )
    result = get_data.json ()
    if songs := result[ "result" ][ "songs" ]:
        if music_song:
            await music_163.send ( MessageSegment.music ( "163", songs[ 0 ][ "id" ] ) )
        if music_record:
            murl = "http://music.163.com/song/media/outer/url?id=" + str ( songs[ 0 ][ "id" ] ) + ".mp3"
            logger.info ( "音频" + murl )
            await music_163.send ( MessageSegment.record ( murl ) )
    else:
        await music_163.send ( "网易云音乐中找不到相关的歌曲" )
