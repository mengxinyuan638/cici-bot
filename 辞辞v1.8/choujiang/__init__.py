from nonebot import on_regex,on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import json
import re
import random

choujiang = on_regex(pattern = r'^幸运抽奖$')
chou = on_regex(pattern = r'^抽奖$')

@choujiang.handle()
async def lj(bot: Bot, event: GroupMessageEvent, state: T_State):
    data_cd = '幸运抽奖\n随机获得金币，禁言等\n发送指令：抽奖即可' 
    await choujiang.finish(message=Message(f'{data_cd}'))


@chou.handle()
async def cj(bot: Bot, event: GroupMessageEvent, state: T_State):
    qq_id = event.user_id
    money = await search(qq_id)
    if money >= 5:
        file_name = 'coints.json'
        with open(file_name) as f:
            data_user = json.load(f)
        now = money - 5
        data = dict(data_user)
        data[f'{qq_id}'] = now
        with open(file_name,'w') as f:
            json.dump(data,f,ensure_ascii=False)
        j = random.randint(0,100)
        if 0 <= j <= 5:
            first_prize = random.randint(100,200)
            await get_prize(qq_id,data_user,first_prize)
            await chou.finish(message=Message(f'恭喜你，中奖{first_prize}个金币'))
        elif 5 < j <= 15:
            first_prize = random.randint(30,100)
            await get_prize(qq_id,data_user,first_prize)
            await chou.finish(message=Message(f'恭喜你，中奖{first_prize}个金币'))
        elif 15 < j <= 20:
            first_prize = random.randint(1,10)
            await bot.set_group_ban(group_id=event.group_id,user_id=qq_id,duration=first_prize*60)
            await chou.finish(message=Message(f'很遗憾抽到禁言{first_prize}分钟'))
        elif 20 < j <= 35:
            first_prize = random.randint(10,30)
            await get_prize(qq_id,data_user,first_prize)
            await chou.finish(message=Message(f'恭喜你，中奖{first_prize}个金币'))
        elif 35 < j <= 50:
            first_prize = random.randint(1,10)
            await get_prize(qq_id,data_user,first_prize)
            await chou.finish(message=Message(f'恭喜你，中奖{first_prize}个金币'))
        else:
            await chou.finish(message=Message(f'很遗憾没有中奖'))
    else:
        await chou.finish(message=Message(f'金币不足，无法抽奖'))
        

async  def get_prize(qq_id,file_read,prize):
    file_name = 'coints.json'
    data = dict(file_read)
    coints = int(data[f'{qq_id}'])
    data[f'{qq_id}'] = int(coints)+prize 
    with open(file_name,'w') as f:
        json.dump(data,f,ensure_ascii=False)





async def search(qq_id):
    file_name = 'coints.json'
    with open(file_name) as f:
        data_user2 = json.load(f)
    money = int(data_user2[f'{qq_id}'])
    return(money)


