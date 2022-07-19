"""
@Author:张时贰
@Blog:zhangshier.vip
"""

"""
nonebot_plugin_firexN
额外依赖pip install nonebot_plugin_apscheduler
需要在.evn中配置:
      fire_users = ["xxx","xxx"]    # 必填 联系人QQ
      fire_mode = 1                 # 必填 模式1发送自定义句子，模式2随机调用一句
      fire_sentence_moring = ["句子1","句子2","..."]    # 如果是模式1 此项必填，早上随机发送该字段中的一句
      fire_sentence_night = ["句子1","句子2","..."]     # 如果是模式1 此项必填，晚上随机发送该字段中的一句
      fire_time_moring = "8 0"    # 选填 早上发送时间默认为7:00
      fire_time_night = "23 0"    # 选填 晚上发送时间默认为22:00                   
"""

import asyncio
import random
from nonebot import require, get_bot, get_driver
from nonebot.log import logger
import requests
import json
import nonebot.plugin

# New way of self registering (use PluginMetadata)
__plugin_meta__ = nonebot.plugin.PluginMetadata (
    name='一起燚xN吧',
    description='为了火花,冲冲冲',
    usage='''默认在7:00和22:00点定时为QQ联系人发送一句消息,如需自定义时间和消息请参考readme''',
    extra={
        'author': '张时贰 qq:1310446718',
        'version': '0.1.0'}
)

try:
    scheduler = require ( "nonebot_plugin_apscheduler" ).scheduler
except BaseException:
    scheduler = None

logger.opt ( colors=True ).info (
    "已检测到软依赖<y>nonebot_plugin_apscheduler</y>, <g>开启定时任务功能</g>"
    if scheduler
    else "未检测到软依赖<y>nonebot_plugin_apscheduler</y>，<r>禁用定时任务功能</r>"
)

# 获取联系人QQ
try:
    fire_user_id = get_driver ().config.fire_users  # <-填写需要收发的QQ联系人,利用for循环遍历QQ发送
except Exception as e:
    logger.error ( "ValueError:{}", e )
    logger.error ( "请配置fire_user_id" )

# 获取模式 如果是模式1就读取自定义句子，模式2使用API
fire_mode = get_driver ().config.fire_mode
if fire_mode == 1:
    fire_sentence_moring = get_driver ().config.fire_sentence_moring
    fire_sentence_night = get_driver ().config.fire_sentence_night

# 获取自定义时间，默认早上七点，晚上十点
try:
    fire_time_moring = get_driver ().config.fire_time_moring
    fire_time_night = get_driver ().config.fire_time_night
    assert fire_time_moring is not None
except (AttributeError, AssertionError):
    fire_time_moring = "7 0"
    fire_time_night = "22 0"
m_hour, m_minute = fire_time_moring.split ( " " )
n_hour, n_minute = fire_time_night.split ( " " )


# 随机一言API
def hitokoto():
    url = "https://v1.hitokoto.cn?c=a&c=b&c=c&c=d&c=h"
    txt = requests.get ( url )
    data = json.loads ( txt.text )
    msg = data[ "hitokoto" ]
    add = ""
    if works := data[ "from" ]:
        add += f"《{works}》"
    if from_who := data[ "from_who" ]:
        add += f"{from_who}"
    if add:
        msg += f"\n——{add}"
    return msg


async def fire_morning():
    sendSuccess = False
    while not sendSuccess:
        try:
            await asyncio.sleep ( random.randint ( 1, 10 ) )
            # await get_bot().send_private_msg(user_id=fire_user_id, message="🌞早，又是元气满满的一天")  # 当未连接到onebot.v11协议端时会抛出异常
            for gid in fire_user_id:
                if fire_mode == 1:
                    await get_bot ().send_private_msg ( user_id=gid,
                                                        message=f"{random.choice ( fire_sentence_moring )}" )
                if fire_mode == 2:
                    await get_bot ().send_private_msg ( user_id=gid, message=hitokoto () )
            logger.info ( "发送火花" )
            sendSuccess = True
        except ValueError as e:
            logger.error ( "ValueError:{}", e )
            logger.error ( "续火花插件获取bot失败，1s后重试" )
            await asyncio.sleep ( 1 )  # 重试前时延，防止阻塞


async def fire_night():
    sendSuccess = False
    while not sendSuccess:
        try:
            await asyncio.sleep ( random.randint ( 1, 10 ) )
            # await get_bot().send_private_msg(user_id=fire_user_id, message="🌛今天续火花了么，晚安啦")  # 当未连接到onebot.v11协议端时会抛出异常
            for gid in fire_user_id:
                if fire_mode == 1:
                    await get_bot ().send_private_msg ( user_id=gid,
                                                        message=f"{random.choice ( fire_sentence_night )}" )
                if fire_mode == 2:
                    await get_bot ().send_private_msg ( user_id=gid, message=hitokoto () )
            logger.info ( "发送火花" )
            sendSuccess = True
        except ValueError as e:
            logger.error ( "ValueError:{}", e )
            logger.error ( "续火花插件获取bot失败，1s后重试" )
            await asyncio.sleep ( 1 )  # 重试前时延，防止阻塞


if scheduler:
    scheduler.add_job ( fire_morning, "cron", hour=m_hour, minute=m_minute, id="fire_morning" )  # 早安
    scheduler.add_job ( fire_night, "cron", hour=n_hour, minute=n_minute, id="fire_night" )  # 晚安
