"""
作者:萌新源
时间:2022/3/30
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处
"""
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Message, Event
import requests
import json

'''
辞辞聊天机器人 调用青云客API http://api.qingyunke.com/
命令:*
config变量0代表发送纯文本，1代表发送语音
'''

cici = on_keyword({'*'})
config = 1

@cici.handle()
async def sj(bot: Bot, event: Event, state: T_State):
    anses = str(event.get_message()).strip()
    ansek = anses.strip('*')
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={ansek}'
    k = requests.get(url)
    hua = json.loads(k.text)
    ans = hua['content']
    l = '菲菲'
    if l in ans:
        if config == 0:
            ansl = ans.replace('菲菲','辞辞')
            await cici.send(Message(ansl))
        elif config == 1:
            ansl = ans.replace('菲菲','辞辞')
            ansl = f"[CQ:tts,text={ansl}]"
            await cici.finish(Message(ansl))
    else:
        if config == 0:
            await cici.send(Message(ans))
        elif config == 1:
            ans = f"[CQ:tts,text={ans}]"
            await cici.finish(Message(ans))
