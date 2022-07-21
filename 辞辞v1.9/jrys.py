import random
from datetime import date
from nonebot import on_keyword
from nonebot.plugin import on_command,export
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

export = export()#获取当前插件的导出内容对象
export.name   =  '今日运势'

def ys_simple(ys):
    if ys < 20:
        return '大吉'
    elif ys < 55:
        return '吉'
    elif ys < 60:
        return '半吉'
    elif ys < 64:
        return '小吉'
    elif ys < 67:
        return '末小吉'
    elif ys < 73:
        return '末吉'
    else:
        return '凶'
    

jrys = on_keyword(['今日运势'])
@jrys.handle()
async def jrys_handle(bot: Bot, event: Event):
    rnd = random.Random()
    rnd.seed(( int(date.today().strftime("%y%m%d"))*45 )*( int(event.get_user_id())*55 ))
    yunshi = rnd.randint(1,100)
    await jrys.finish(message = Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{yunshi}（越低越好），为"{ys_simple(yunshi)}"'))