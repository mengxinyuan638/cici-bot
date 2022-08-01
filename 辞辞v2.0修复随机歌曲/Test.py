import requests
import json
import re

url = 'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'
get_data = requests.get(url)
get_json = json.loads(get_data.text)
# print(get_json)
get_dt = get_json['data']
url = get_dt['url']
url = re.findall(r'id=(.+?)$',url)
print(url[0])

