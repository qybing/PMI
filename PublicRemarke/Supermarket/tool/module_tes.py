# import json
# import re
#
# a = 'mid-rank-stars mid-str45'
# b = re.findall('\d+',a)
# c = ''.join(b)
# print(c)
#
# num_key = {'fn-67HV': '0',
#                'fn-67H1': '1',
#                'fn-cMXT': '2',
#                'fn-6OZv': '3',
#                'fn-JG8T': '4',
#                'fn-UqkY': '5',
#                'fn-QanZ': '6',
#                'fn-Kwvz': '7',
#                'fn-Lmh3': '8',
#                'fn-JEFc': '9',
#                'fn-JEFa': '.',
#
#                }
# print(num_key.get('fn-JEFa'))


import base64  # 代理服务器

proxyServer = "http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "HE028T9448613Y4D"
proxyPass = "9CFB203161ACD692"

# for Python2
# proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)


# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
print(proxyAuth)