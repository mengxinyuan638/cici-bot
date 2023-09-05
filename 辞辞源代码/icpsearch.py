"""
作者:萌新源
时间:2022/4/1
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处
"""
'''
备案查询 调用API https://api.mxycn.cn/api/icp.php?msg=
命令:#ICP (.*)
'''
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, Event
import requests,json


icpsearch = on_keyword ( {'#ICP'} )


@icpsearch.handle ()
async def sj(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message()).strip('')
    get_msg = get_msg.strip('#ICP ')
    url = f'https://api.mxycn.cn/api/icp.php?msg={get_msg}'
    get_data = requests.get(url=url)
    get_txt = json.loads(get_data.text)
    code = get_txt['code']
    if code == 200:
        get_txt = get_txt['data']
        host = get_txt['host']#获取主办单位
        nature = get_txt['type']#性质
        icp = get_txt['bah']#备案号
        sitename = get_txt['name']#网站名称
        index = get_txt['link']#首页
        time = get_txt['date']#审核通过时间
        limit = get_txt['limit']#是否限制接入
        mxy = '——Power by 萌新源'
        msg = f'查询结果\n主办单位:{host}\n性质:{nature}\nICP备案号:{icp}\n网站名称:{sitename}\n网站首页:{index}\n审核通过时间:{time}\n是否限制接入:{limit}\n{mxy}'
    else:
        msg = '未查询到该域名备案记录，请检查是否输错域名再重试'
    await icpsearch.finish ( Message ( f'{msg}' ) )
