import json

async def search_bocket(qq_id):
    file2_name = 'store.json'
    with open(file2_name) as f:
        data_store_person = json.load(f)
    qq_data = data_store_person[f'{qq_id}']
    for key,value in qq_data.items():
        data = f'{key}:{value}'
    return(data)

async def search_use(qq_id,goods_name):
    file2_name = 'store.json'
    with open(file2_name) as f:
        data_store_person = dict(json.load(f))
    qq_data = data_store_person[f'{qq_id}']
    goods_number = int(qq_data[f'{goods_name}'])
    return goods_number
