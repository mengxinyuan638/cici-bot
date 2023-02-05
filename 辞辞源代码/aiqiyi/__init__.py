import httpx
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, MessageSegment

"""
本插件功能为返回爱奇艺热播榜榜单
命令：
  - 爱奇艺榜 返回爱奇艺热播榜榜单
writen by mengxinyuan at 2023/2/5
CopyRight© 2023 萌新源
"""

aqy = on_regex(pattern=r'^爱奇艺榜$')


@aqy.handle()
async def qy(bot: Bot, event: GroupMessageEvent, state: T_State):
    """返回热播电视剧榜单"""
    url = 'https://pcw-api.iqiyi.com/strategy/pcw/data/topRanksData?page_st=0&tag=0&category_id=-1&date=&pg_num=1'
    async with httpx.AsyncClient() as client:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        data = await client.get(url=url, headers=headers)
    data = data.json()
    video_data = data['data']['formatData']['data']['content']  # 获取榜单
    video_num = len(video_data)  # 获取榜单电视剧数量
    temp = []
    for i in range(0, video_num):
        k = i + 1
        img = video_data[i]['img']
        img = MessageSegment.image(img)
        desc = video_data[i]['desc']  # 电视剧描述
        tags = video_data[i]['tags']  # 标签
        danmu = video_data[i]['danmu']  # 弹幕数量
        index = video_data[i]['index']  # 热度
        pageurl = video_data[i]['pageUrl']  # 播放链接
        temp2 = {
            "type": "node",
            "data": {
                "name": "辞辞传声机",
                "uin": "10087",
                "content": f"{k}.{video_data[i]['title']}\r\n{img}\r\n简介:{desc}\r\n标签:{tags}\r\n弹幕:{danmu}\r\n热度:{index}\r\n播放链接:{pageurl}\r\n"
            }
        }
        temp.append(temp2)
    await bot.send_group_forward_msg(group_id=event.group_id, messages=temp)
