# -------------------------  url 拼接  --------------#
# from urllib.parse import urlencode

#
# base_url = 'https://restapi.amap.com/v3/place/polygon?'
# params = {'polygon': 1, 'types': 'com', 'offset': 25}
# data = urlencode(params)
# a = base_url+data
# print(a )
# print(type(a))
# -------------------------  url 拼接  --------------#

#-----------------------正则测试----------------#
# import re
# x = []
# a = 'https://restapi.amap.com/v3/place/polygon?polygon=71.234018,17.725738|136.139681,55.28893&keywords=kfc&output=xml&key=222222'
# d = re.sub('&key=222222','',a)
# print(d)
# url = a.find('key=')
# print(a[0:url])
# b = re.findall('polygon=(.*?)&',a)[0]
# c = b.split('|')
# for i in c:
#     x.extend(i.split(','))
# print(float(x[0]))
# print(type(x))
#----------------------------------------------#
# import os
# pwd = os.getcwd()
# a = os.path.join(pwd,'GaodeCode_python.xlsx')
# print(a)
# a = 50
# for i in range(1,a):
#     print(i)
import math

sum = 24
maxPage = math.ceil(sum / 25)
now_page = 1
if sum==25 :
    print('1')
elif sum>1:
    print('2')
elif sum>2:
    print('3')
else:
    print('4')