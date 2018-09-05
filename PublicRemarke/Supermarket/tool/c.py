import time
from random import random

import requests


def get_hcv():
    """
    计算cookies中的_hc.v
    """

    def n():
        def n():
            return str(hex(int(65536 * (1 + random()))))[3:]

        return '-'.join([n() + n(), n(), n(), n(), n() + n() + n()])

    def i():
        return n() + '.' + str(int(time.time()))

    return i()

# 要访问的目标页面
# targetUrl = "http://proxy.abuyun.com/switch-ip"
# targetUrl = "http://proxy.abuyun.com/current-ip"

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "xxxxxxx"
proxyPass = "xxxxxxxx"
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}
proxies = {
    # "http": proxyMeta,
    "https": proxyMeta,
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie':get_hcv()
}
targetUrl = "https://ip.cn/"
urls = [
    'http://www.dianping.com/shop/98133712','http://www.dianping.com/shop/98250272',
    'http://www.dianping.com/shop/70419682','http://www.dianping.com/shop/93933218',
    'http://www.dianping.com/shop/7211461','http://www.dianping.com/shop/98046236'
]
for url in urls:
    resp = requests.get(url,headers=headers, proxies=proxies)
    print(resp.text)