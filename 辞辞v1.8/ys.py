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

yuanshen = on_keyword({'#原神'})

@yuanshen.handle()
async def sj(bot: Bot, event: Event, state: T_State):
    ansey = str(event.get_message()).strip()
    ansec = ansey.strip('#原神')
    url = f'https://wanghun.top/api/v5/yuanshen.php?msg={ansec}'
    k = requests.get(url)
    y_ans = k.text
    l = '<br>'
    if l in y_ans:
        ansl = y_ans.replace(l,'\n')
        await yuanshen.finish(Message(f'{ansl}'))
    else:
        await yuanshen.finish(Message(f'{y_ans}'))
    
    

