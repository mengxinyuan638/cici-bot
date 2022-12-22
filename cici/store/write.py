import json

async def write_file(file_read,qq,cost,data_store,goods_name):
    file_name = 'coints.json'
    file2_name = 'store.json'
    data = dict(file_read)
    data2 = dict(data_store)
    qq_str = str(qq)
    data2_unqq = data_store[f'{qq_str}']
    goods_number = data2_unqq[f'{goods_name}']
    goods_top = int(goods_number) + 1
    data2_unqq[f'{goods_name}'] = int(goods_top)
    coints = data[f'{qq_str}']
    data[f'{qq_str}'] = int(coints) - int(cost)
    with open(file_name,'w') as f:
        json.dump(data,f,ensure_ascii=False)
    with open(file2_name,'w') as f:
        json.dump(data2,f,ensure_ascii=False)
    
