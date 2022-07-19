from nonebot import on_keyword,on_message
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment,Event

sl = on_keyword({'发'})
@sl.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    qq = event.user_id
    group = event.group_id
    xx = '测试成功'
    await bot.send_private_msg(user_id=qq,group_id=group,message=xx,auto_escape=False)
