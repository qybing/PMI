# a = '                                                                    豪宅                                                                    内环内                                                                    轨交房                                                                    全景看房                                                                    景区                                                            '
# b = a.strip().split(' ')
# c = [ i for i in b if i]
# print(c)
import random
from time import sleep

import requests
url = 'http://127.0.0.1:5000/get'
for i in range(10):
    # sleep(2)
    rea = requests.get(url)
    print (rea)
    # print(rea.text)
