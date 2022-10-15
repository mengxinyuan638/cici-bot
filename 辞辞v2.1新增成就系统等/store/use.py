import json

async def useit(qq_id,goods_name,number_now):
    file2_name = 'store.json'
    with open(file2_name) as f:
        data_store_person = dict(json.load(f))
        
    qq_data = data_store_person[f'{qq_id}']
    qq_data[f'{goods_name}'] = number_now
    data_store_person[f'{qq_id}'] = qq_data
    with open(file2_name,'w') as f:
        json.dump(data_store_person,f,ensure_ascii=False)
