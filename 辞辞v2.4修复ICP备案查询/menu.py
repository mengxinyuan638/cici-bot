from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,Event

gjc =on_regex(pattern = r'^菜单$')
hwlt =on_regex(pattern = r'^和我聊天$')
xzys =on_regex(pattern = r'^星座运势$')
dmtp =on_regex(pattern = r'^原神角色$')
fy =on_regex(pattern = r'^中英互译$')
yq =on_regex(pattern = r'^疫情查询$')
qg =on_regex(pattern = r'^群管工具$')
icp =on_regex(pattern = r'^备案查询$')



@gjc.handle()
async def kk(bot: Bot, event: GroupMessageEvent, state: T_State):
    datb = "——☃—辞辞机器—☃——\n♚随机一言♚随机歌曲♚\n♚随机头像♚和我聊天♚\n♚星座运势♚动漫壁纸♚\n♚原神角色♚中英互译♚\n♚今日运势♚疫情查询♚\n♚舔狗日记♚心灵鸡汤♚\n♚土味情话♚讲个笑话♚\n♚群管工具♚金币商城♚\n♚每日一言♚备案查询♚\n♚系统信息♚等待更新♚\n——————————————\n❤️欢迎使用辞辞机器人❤️\n"
    datb = Message(datb)
    await gjc.finish(message=Message(f'{datb}'))
    
@hwlt.handle()#和我聊天响应体
async def ll(bot: Bot, event: GroupMessageEvent, state: T_State):
    data1 = "艾特我加你要和我聊的内容"
    data1 = Message(data1)
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await hwlt.finish(message=Message(f'{data1}'))
    
@xzys.handle()#星座运势响应体
async def ll(bot: Bot, event: GroupMessageEvent, state: T_State):
    data2 = "输入#星座加要查询的星座"
    data2 = Message(data2)
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await xzys.finish(message=Message(f'{data2}'))
    
    
@dmtp.handle()#原神角色响应体
async def ll(bot: Bot, event: GroupMessageEvent, state: T_State):
    data3 = "输入#原神加要查询的原神角色"
    data3 = Message(data3)
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await dmtp.finish(message=Message(f'{data3}'))
    

@fy.handle()#中英互译响应体
async def ll(bot: Bot, event: GroupMessageEvent, state: T_State):
    data4 = "输入#翻译加要翻译的文本，语种将会自动识别"
    data4 = Message(data4)
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await fy.finish(message=Message(f'{data4}'))
    

@yq.handle()#疫情查询响应体
async def ll(bot: Bot, event: GroupMessageEvent, state: T_State):
    data5 = "输入#疫情加要查询的县级以上地域，如:泉州，福建"
    data5 = Message(data5)
    await yq.finish(message=Message(f'{data5}'))

@qg.handle()#群管工具响应体
async def ll(bot: Bot, event: GroupMessageEvent, state: T_State):
    data5 = "#全体禁言\n1.开启全禁\n2.关闭全禁\n#单人禁言\n1.禁@某人 禁言时间（单位：分钟）\n2.解@某人\n#移出群聊\n1.踢@某人\n#入群申请\n1.同意申请\n2.拒绝申请"
    data5 = Message(data5)
    await yq.finish(message=Message(f'{data5}'))

@icp.handle()#备案查询响应体
async def ll(bot: Bot, event: GroupMessageEvent, state: T_State):
    data5 = "命令:ICP 加要查询的网站\n例如:baidu.com"
    data5 = Message(data5)
    await yq.finish(message=Message(f'{data5}'))
    
    

    