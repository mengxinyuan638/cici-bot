from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot

test_private = on_keyword({'发'})
@test_private.handle()
async def test(bot: Bot, event: GroupMessageEvent, state: T_State):
    get_user = event.user_id
    get_group = event.group_id
    msg = '测试成功'
    await bot.send_private_msg(user_id=get_user,group_id=get_group,message=msg,auto_escape=False)