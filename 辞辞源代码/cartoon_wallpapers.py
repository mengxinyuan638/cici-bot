"""
作者:萌新源
时间:2022/3/30
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处
"""
from nonebot.plugin.on import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, MessageSegment
import requests

'''
动漫壁纸 调用API https://api.mxycn.cn/api/dmbz.php
正则命令:动漫壁纸
'''
wallpapers = on_regex ( pattern=r"^动漫壁纸$" )


@wallpapers.handle ()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_wallpapers ()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await wallpapers.send ( MessageSegment.image ( msg ) )


async def get_wallpapers():
    url = 'https://api.mxycn.cn/api/dmbz.php'
    get_data = requests.get ( url )
    img = get_data.text.strip ()
    return img
