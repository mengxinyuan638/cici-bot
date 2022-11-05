import json
from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message

send = 0#初始化全局变量
send2 = 0

cj = on_regex(pattern = r'^我的称号$')

async def set_success(qq_id,success_name):
    global send#获取全局变量
    file2_name = 'success.json'
    with open(file2_name) as f:
        data_success_person = dict(json.load(f))
        
    qq_id = str(qq_id)#转换一下数据类型避免出错
    if qq_id in data_success_person:
        person_success = data_success_person[qq_id]#获取个人数据
    else:
        data_success_person[qq_id] = ['新手上路']
        person_success = data_success_person[qq_id]


    if success_name in person_success:
        send = f'要不我们休息一下吧，炸太多容易拉仇恨'
    else:
        person_success = list(person_success)#转换为列表
        person_success.append(success_name)#追加称号
        data_success_person[qq_id] = person_success#修改值
        with open(file2_name,'w') as f:
            json.dump(data_success_person,f,ensure_ascii=False)
        send = f'恭喜你，触发了{success_name}的称号'

@cj.handle()
async def show_success(bot: Bot, event: GroupMessageEvent, state: T_State): 
    global send2#获取全局变量
    qq_id = str(event.user_id)
    file2_name = 'success.json'
    with open(file2_name) as f:
        data_success_person = dict(json.load(f)) 
    l = 0
    cj1 = ''
    person_success = data_success_person[qq_id]
    for i in person_success:
        l = l+1
        cj1 += f'{l}.{i}\n'
    send2 = f'您的称号\n{cj1}'

    await cj.send(message=Message(f'{send2}'))



async def suc_news():
    news = send
    return news

