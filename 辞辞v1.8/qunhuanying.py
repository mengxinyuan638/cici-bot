from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent

welcom=on_notice()

@welcom.handle()
async def welcome(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    user = event.get_user_id()
    at_ = "欢迎！：[CQ:at,qq={}]".format(user)
    msg = at_ + '大佬加入'
    msg = Message(msg)
    await welcom.finish(message=Message(f'{msg}'))




