"""
基本功能：违禁词自动撤回、全员禁言、成员禁言、踢人、同意/拒绝入群申请、入群欢迎、定时推送群消息(支持enjoy表情)

额外依赖pip install nonebot_plugin_apscheduler
定时推送群消息需要在.evn中配置:
send_group_id = ["xxx","xxx"]    # 必填 群号
send_switch_morning = False                      # 选填 True/False 默认开启 早上消息推送是否开启
send_switch_night = False                        # 选填 True/False 默认开启 晚上消息推送是否开启
send_mode = 1                 # 选填 默认模式2 模式1发送自定义句子，模式2随机调用一句
send_sentence_moring = ["句子1","句子2","..."]    # 如果是模式1 此项必填，早上随机发送该字段中的一句
send_sentence_night = ["句子1","句子2","..."]     # 如果是模式1 此项必填，晚上随机发送该字段中的一句
send_time_moring = "8 0"    # 选填 早上发送时间默认为7:00
send_time_night = "23 0"    # 选填 晚上发送时间默认为22:00
"""
from pydoc import text
from nonebot import on_keyword, on_regex, on_request, on_regex
from nonebot.exception import ActionFailed
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, GroupRequestEvent, GROUP_ADMIN, GROUP_OWNER
import warnings
from nonebot.permission import *
import re
import asyncio
import random
from nonebot import require, get_bot, get_driver
from nonebot.log import logger
import requests
import json

warnings.filterwarnings ( "ignore" )

# 撤回消息
che = on_keyword (
    {'沙雕', '妈的','操你妈', '操你', '加vx','傻逼', 'SB', 'sb', '脑瘫', 'CNM',
     'CNm', 'CnM', 'Cnm', 'cNM', 'cNm', 'cnM'} )
all_ban = on_regex ( pattern = r'^开启全禁$', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
all_unban = on_regex ( pattern = r'^关闭全禁$', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
alone_ban = on_keyword ( "禁", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
alone_unban = on_keyword( "解", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
group_remove = on_keyword ( "踢", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
group_apply = on_request ()
agree_apply = on_regex ( pattern = r'^同意申请$', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
disagree_apply = on_regex ( pattern = r'^拒绝申请$', priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )


@che.handle ()
async def c(bot: Bot, event: GroupMessageEvent, state: T_State):
    mid = event.message_id
    group = event.group_id
    qq = event.user_id
    ban = 300  # 禁言300s
    print ( mid )
    print ( group )
    await bot.delete_msg ( message_id=mid )  # 撤回消息
    await bot.set_group_ban ( group_id=group, user_id=qq, duration=ban )  # 禁言
    await che.finish ( message=f'@{qq} 你的发言可能包含敏感词汇，这里禁言5分钟警告一下' )


# 开启全员禁言
@all_ban.handle ()
async def ban_all(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        await bot.set_group_whole_ban ( group_id=event.group_id, enable=True )
        await all_ban.finish ( "已开启全员禁言" )
    except ActionFailed:
        await all_ban.finish ( "权限不足" )


# 关闭全员禁言
@all_unban.handle ()
async def unban_all(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        await bot.set_group_whole_ban ( group_id=event.group_id, enable=False )
        await all_unban.finish ( "已关闭全员禁言" )
    except ActionFailed:
        await all_unban.finish ( "权限不足" )


# 禁言某人
@alone_ban.handle ()
async def ban_alone(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        data = str ( event.message )
        qq = re.findall ( r'qq=(.+?)]', data )
        qq = int ( qq[ 0 ] )
        minute = random.randint ( 1, 10 )
        seconds = minute*60
        await bot.set_group_ban ( group_id=event.group_id, user_id=qq, duration=seconds )
        await alone_ban.finish ( message=f'已禁言\nQQ:{qq}\n时间：{minute}分钟' )
    except ActionFailed:
        await alone_ban.finish ( "权限不足" )


# 解禁某人
@alone_unban.handle ()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        data = str ( event.message )
        qq = re.findall ( r'qq=(.+?)]', data )
        qq = int ( qq[ 0 ] )
        await bot.set_group_ban ( group_id=event.group_id, user_id=qq, duration=0 )
        await alone_unban.finish ( message=f'已解除禁言\nQQ:{qq}' )
    except ActionFailed:
        await alone_unban.finish ( "权限不足" )


# 入群申请消息
@group_apply.handle ()
async def apply_msg(bot: Bot, event: GroupRequestEvent, state: T_State):
    global apply_id
    apply_id = event.user_id
    message = event.comment  # 获取验证信息
    global flag_id
    flag_id = event.flag  # 申请进群的flag
    global type_id
    type_id = event.sub_type  # 请求信息的类型
    await group_apply.finish ( message=f'有人申请进群\nQQ:{apply_id}\n验证消息:{message}\n同意/拒绝' )


# 同意申请入群
@agree_apply.handle ()
async def agree(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        await bot.set_group_add_request ( flag=flag_id, sub_type=type_id, approve=True )
        await agree_apply.finish ( message=f'欢迎{apply_id}入群' )
    except ActionFailed:
        await agree_apply.finish ( "权限不足" )


# 拒绝入群
@disagree_apply.handle ()
async def sn(bot: Bot, event: GroupMessageEvent, state: T_State):
    await bot.set_group_add_request ( flag=flag_id, sub_type=type_id, approve=False,
                                      reason='机器人自动审批，如有误判请联系群主或其他管理员' )


# 踢出群聊
@group_remove.handle ()
async def move(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        data = str ( event.message )
        group_id = event.group_id
        qq_id = re.findall ( r'qq=(.+?)]', data )
        qq_id = qq_id[ 0 ]
        await bot.set_group_kick ( group_id=group_id, user_id=qq_id, reject_add_request=False )
        await group_remove.finish ( message=f'已将QQ:{qq_id}移除群聊' )
    except ActionFailed:
        await group_remove.finish ( "权限不足" )


try:
    scheduler = require ( "nonebot_plugin_apscheduler" ).scheduler
except BaseException:
    scheduler = None

logger.opt ( colors=True ).info (
    "已检测到软依赖<y>nonebot_plugin_apscheduler</y>, <g>开启定时任务功能</g>"
    if scheduler
    else "未检测到软依赖<y>nonebot_plugin_apscheduler</y>，<r>禁用定时任务功能</r>"
)

# 获取QQ群号
try:
    send_group_id = get_driver ().config.send_group_id  # <-填写需要收发的QQ群号,利用for循环遍历发送
except Exception as e:
    logger.error ( "ValueError:{}", e )
    logger.error ( "请配置send_group_id" )

# 开关 默认全开
try:
    send_switch_morning = get_driver ().config.send_switch_morning
except (AttributeError, AssertionError):
    send_switch_morning = True
try:
    send_switch_night = get_driver ().config.send_switch_night
except (AttributeError, AssertionError):
    send_switch_night = True
# print ( send_switch_morning )
# print ( not send_switch_morning )
# print ( type ( send_switch_morning ) )
# evn读进来是str类型，吐了啊，这个bug找了好久一直以为是逻辑有错。str转bool
send_switch_morning = bool ( send_switch_morning )
send_switch_night = bool ( send_switch_night )

# 获取模式 默认模式2 如果是模式1就读取自定义句子，模式2使用API
try:
    send_mode = get_driver ().config.send_mode
except (AttributeError, AssertionError):
    send_mode = 2
if send_mode == 1:
    send_sentence_moring = get_driver ().config.send_sentence_moring
    send_sentence_night = get_driver ().config.send_sentence_night

# 获取自定义时间，默认早上七点，晚上十点
try:
    send_time_moring = get_driver ().config.send_time_moring
    send_time_night = get_driver ().config.send_time_night
    assert send_time_moring is not None
except (AttributeError, AssertionError):
    send_time_moring = "14 50"
    send_time_night = "22 0"
m_hour, m_minute = send_time_moring.split ( " " )
n_hour, n_minute = send_time_night.split ( " " )


# 随机一言API
def hitokoto():
    url = "https://api.juncikeji.xyz/api/mryy.php"
    txt = requests.get ( url )
    data = txt
    msg = data
    add = ""
    if works := data[ "from" ]:
        add += f"《{works}》"
    if from_who := data[ "from_who" ]:
        add += f"{from_who}"
    if add:
        msg += f"\n——{add}"
    return msg


async def send_morning():
    # 如果False直接退出函数
    if send_switch_morning:
        logger.info ( "send_morning()关闭，跳出函数" )
        return
    sendSuccess = False
    while not sendSuccess:
        try:
            await asyncio.sleep ( random.randint ( 1, 10 ) )
            # await get_bot().send_private_msg(user_id=fire_user_id, message="🌞早，又是元气满满的一天")  # 当未连接到onebot.v11协议端时会抛出异常
            for gid in send_group_id:
                if send_mode == 1:
                    await get_bot ().send_group_msg ( group_id=gid,message=f"{random.choice ( send_sentence_moring )}" )
                if send_mode == 2:
                    await get_bot ().send_group_msg ( group_id=gid, message=hitokoto () )
            logger.info ( "群聊推送消息" )
            sendSuccess = True
        except ValueError as e:
            logger.error ( "ValueError:{}", e )
            logger.error ( "群聊推送消息插件获取bot失败，1s后重试" )
            await asyncio.sleep ( 1 )  # 重试前时延，防止阻塞


async def send_night():
    # 如果False直接退出函数
    if not send_switch_night:
        logger.info ( "send_night()关闭，跳出函数" )
        return
    sendSuccess = False
    while not sendSuccess:
        try:
            await asyncio.sleep ( random.randint ( 1, 10 ) )
            # await get_bot().send_private_msg(user_id=fire_user_id, message="🌛今天续火花了么，晚安啦")  # 当未连接到onebot.v11协议端时会抛出异常
            for gid in send_group_id:
                if send_mode == 1:
                    await get_bot ().send_group_msg ( group_id=gid,
                                                      message=f"{random.choice ( send_sentence_night )}" )
                if send_mode == 2:
                    await get_bot ().send_group_msg ( group_id=gid, message=hitokoto () )
            logger.info ( "群聊推送消息" )
            sendSuccess = True
        except ValueError as e:
            logger.error ( "ValueError:{}", e )
            logger.error ( "群聊推送消息插件获取bot失败，1s后重试" )
            await asyncio.sleep ( 1 )  # 重试前时延，防止阻塞


if scheduler:
    scheduler.add_job ( send_morning, "cron", hour=m_hour, minute=m_minute, id="send_morning" )  # 早上推送
    scheduler.add_job ( send_night, "cron", hour=n_hour, minute=n_minute, id="send_night" )  # 晚上推送