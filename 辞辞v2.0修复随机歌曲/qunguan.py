import random
from nonebot import on_keyword, on_request, on_command
from nonebot.exception import ActionFailed
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, GroupRequestEvent, GROUP_ADMIN, GROUP_OWNER
import warnings
from nonebot.permission import *
import re

warnings.filterwarnings ( "ignore" )

# 撤回消息
che = on_keyword (
    {'广告', '沙雕', '广告', 'md', '妈的', '卧槽', '嘛的', '操你妈', '操你', '加vx', '操', '草', '傻逼', 'SB', 'sb', 'nt', '脑瘫', '骚', 'CNM',
     'CNm', 'CnM', 'Cnm', 'cNM', 'cNm', 'cnM'} )
all_ban = on_command ( "开启全禁", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
all_unban = on_command ( "关闭全禁", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
alone_ban = on_command ( "禁", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
alone_unban = on_command ( "解", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
group_remove = on_command ( "踢", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
group_apply = on_request ()
agree_apply = on_command ( "同意", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )
disagree_apply = on_command ( "拒绝", priority=1, block=True, permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER )


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