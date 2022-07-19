"""
作者:萌新源
时间:2022/3/30
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

cici = on_keyword({'/'})

@cici.handle()
async def sj(bot: Bot, event: Event, state: T_State):
    anses = str(event.get_message()).strip()
    ansek = anses.strip('/')
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={ansek}'
    k = requests.get(url)
    hua = json.loads(k.text)
# print(hua)
    ans = hua['content']
    l = '菲菲'
    if l in ans:
        ansl = ans.replace('菲菲','辞辞')
        await cici.finish(Message(f'{ansl}'))
    else:
        await cici.finish(Message(f'{ans}'))
    
    

