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
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, Event
import requests
import json

'''
疫情查询 调用APIhttps://api.juncikeji.xyz/api/yiqing.php?msg=
本API由萌新源API提供服务
命令:#疫情+城市
'''
covid = on_keyword ( {'#疫情'} )


@covid.handle ()
async def query(bot: Bot, event: Event, state: T_State):
    get_city = str ( event.get_message () ).strip ()
    get_city = get_city.strip ( '#疫情' )
    url = f'https://api.juncikeji.xyz/api/yiqing.php?msg={get_city}'
    get_data = requests.get(url)
    msg = json.loads(get_data.text)
    conNum = msg['累计确诊']  # 赋值累计确诊人数
    cureNum = msg['累计治愈']  # 赋值累计治愈人数
    deathNum = msg['累计死亡']  # 赋值累计死亡人数
    asymptomNum = msg['现存无症状']  # 赋值现存无症状人数
    econNum = msg['现存确诊']  # 赋值现存确诊人数
    origin = msg['数据来源']  # 赋值数据来源
    result = f'🏠查询地区:{get_city}\n🌾累计确诊人数:{conNum}\n❤累计治愈人数:{cureNum}\n☠累计死亡人数:{deathNum}\n⛔现存无症状:{asymptomNum}\n🌡现存确诊:{econNum}\n💻数据来源:{origin}'

    await covid.finish ( Message ( f'{result}' ) )
