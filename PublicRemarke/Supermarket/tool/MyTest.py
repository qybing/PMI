import json

import requests
def get():
    url_POI = 'https://restapi.amap.com/v3/place/text?'
    maxDoc = 25
    params = {'citylimit': True, 'children': 1, 'offset': maxDoc, 'extensions': 'all'}
    params['page'] = 2
    # params['key'] = choice(GDkeys)
    params['key'] = '5505395763b84ab30052bde548ef6db2'
    params['city'] = '110101'
    params['types'] = '160336'
    result = requests.get(url=url_POI, params=params, timeout=15).json()
    print(result['count'])
    json_dicts = json.dumps(result['pois'], indent=4,ensure_ascii=False)
    print(json_dicts)

if __name__ == '__main__':
    # print('aaaaaaaaaaaaa')
    get()