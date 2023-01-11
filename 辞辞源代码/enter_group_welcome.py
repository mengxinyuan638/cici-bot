from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters import Bot
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent,GroupDecreaseNoticeEvent
'''
入群欢迎以及退群通报
'''

welcom=on_notice()
getout=on_notice()

@welcom.handle()
async def welcome(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    """入群欢迎"""
    user = event.get_user_id()
    at_ = "欢迎！：[CQ:at,qq={}]".format(user)
    msg = at_ + '大佬加入'
    msg = Message(msg)
    await welcom.finish(message=Message(f'{msg}'))

@getout.handle()
async def get(bot: Bot, event: GroupDecreaseNoticeEvent, state: T_State):
    """退群通报"""
    if event.sub_type == 'leave':
        """主动退出"""
        user = event.get_user_id() # 获取离开者的QQ号
        msg = f'很遗憾，{user}退出了本群，江湖有缘再见！'
        await getout.finish(Message(msg))
    elif event.sub_type == 'kick':
        """非主动退出，被踢出群"""
        user = event.user_id # 获取被踢的qq号
        msg = f'{user}被踢出了群聊，群友们引以为戒哦'
        await getout.finish(Message(msg))




