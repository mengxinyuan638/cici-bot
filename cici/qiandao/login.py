import json
from .write import write_file

send = 0
async def search(coint,qq,time):
    file_name = 'coints.json'
    with open(file_name) as f:
        data_user = json.load(f)
    last_time = data_user[f'{qq}login']
    global send
    if time == last_time:
        send = '你已经签到过了，明天再来吧'
    else:
        send = f'签到成功，获得{coint}个金币'
        await write_file(coint,qq,False,data_user,time)
        
async def notice():#返回信息
    news = send
    return news