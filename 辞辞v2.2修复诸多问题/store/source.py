import json
from .write import write_file

a = 'null'
async def buy(coints,data_user,qq_id,price,data_store,goods_name):
    global a
    if coints >= price:
        await write_file(data_user,qq_id,price,data_store,goods_name)
        a = '购买成功'
    else:
        a = '很抱歉，您的金币不足'

async def news():
    data = a
    return data
