from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
from .read import notice2, read_data
from .login import notice,search
from .write import write_file
import time
import json
import random



qd = on_regex(pattern = r'^签到$')

@qd.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    coints = random.randint(1,100)
    qq_id = str(event.user_id)
    local_time = time.localtime(event.time)
    login_time = time.strftime('%d',local_time)
    file_name = 'coints.json'
    with open(file_name) as f:
            data_user = json.load(f)
    if qq_id in data_user:#判断用户是不是第一次签到
        await read_data(coints,qq_id,login_time)  #首次使用签到功能需要先执行一次签到
        lovelive_send = await notice()
    else:
        await read_data(coints,qq_id,login_time)  #首次使用签到功能需要先执行一次签到
        lovelive_send = await notice2()
    
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    
    
    await qd.send(Message(str(lovelive_send)))

