# #-------------------------根据多边形进去切割上传数据到Redis----------------#
# import pandas as pd
# import redis
#
# codePath2 = 'GaodeCode_python.xlsx'
# from urllib.parse import urlencode
# import urllib
#
# df1 = pd.read_excel(codePath2, sheetname='大陆adcode')
# df2 = pd.read_excel(codePath2, sheetname='POI分类与编码（中英文）')
# base_url = 'https://restapi.amap.com/v3/place/polygon?'
# a = []
# pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
# r = redis.Redis(connection_pool=pool)
# for type in df2['NEW_TYPE']:
#     params = {'offset': 25, 'extensions': 'base','polygon': '71.234018,17.725738|136.139681,55.28893','types': type,'page':'1'}
#     # print(base_url+urllib.parse.urlencode(params))
#     a.append(base_url+urllib.parse.urlencode(params))
#     r.sadd('GaoDePoiByPolygon:start_urls',base_url+urllib.parse.urlencode(params))
# print(len(a))
# #-------------------------根据多边形进去切割上传数据到Redis----------------#



# #-------------------------根据城市acode 把URL存入Redis----------------#
import pandas as pd
import redis

codePath2 = 'GaodeCode_python.xlsx'
from urllib.parse import urlencode
import urllib
base_url = 'https://restapi.amap.com/v3/place/text?'
df1 = pd.read_excel(codePath2, sheetname='大陆adcode')
df2 = pd.read_excel(codePath2, sheetname='POI分类与编码（中英文）')
a = []
for city in df1['adcode']:
    for type in df2['NEW_TYPE']:
        params = {'citylimit': True, 'children': 1, 'offset': 25, 'extensions': 'all','page':'1','city':city,'types':type}
        real_url = base_url + urllib.parse.urlencode(params)
        a.append(real_url)
print(len(a))
# #-------------------------根据城市acode 把URL存入Redis----------------#
