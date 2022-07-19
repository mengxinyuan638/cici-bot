"""
作者:萌新源
时间:2022/4/1
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处

"""
from nonebot import on_keyword, on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment,Event
import requests
import json

fy = on_keyword({'#翻译'})

@fy.handle()
async def sj(bot: Bot, event: Event, state: T_State):
    anses = str(event.get_message()).strip()
    ansek = anses.strip('#翻译')
    url = f'http://hm.suol.cc/API/fy.php?msg={ansek}'
    k = requests.get(url)
    ans = k.text
    mxy = '——Power by 萌新源'
    ans_a = f'{ans}\n{mxy}'
    await fy.finish(Message(f'{ans_a}'))
    
    

