from random import random
import math
import time
import re

import requests
import time

from parsel import Selector
from fake_useragent import UserAgent
from w3lib.html import remove_tags

def get_hcv():
    """
    计算cookies中的_hc.v
    """
    def n():
        def n():
            return str(hex(int(65536 * (1 + random()))))[3:]
        return '-'.join([n()+n(), n(), n(), n(), n()+n()+n()])
    def i():
        return n() + '.' + str(int(time.time()))
    return i()

def get_html_content(start_url):
    for tries in range(5):
        ua = UserAgent()
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "HE028T9448613Y4D"
        proxyPass = "9CFB203161ACD692"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        # proxies = {
        #     "http": "http://{}".format('http://125.86.167.6:4697'),
        #     "https": "http://{}".format('http://125.86.167.6:4697'),
        # }
        # print(proxies)
        headers = {
            'Host': 'www.dianping.com',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Cookie': '_hc.v={};'.format(get_hcv())
        }
        try:
            res = requests.get(url=start_url,headers=headers)
            print(res.cookies.get_dict().keys())
            # print(res.headers['Location'])
            print(res)
            if res.status_code == 200:
                return res.content.decode('utf-8')
        except Exception as e:
            print(e.args)
            if tries < (5 - 1):
                time.sleep(tries + 1)  # hava a rest
                print('retry:' + start_url)
                continue
            else:
                print('没有获取到网页数据')
                return ''


def get_deatil(start_url_content):
    html = start_url_content


if __name__ == '__main__':
    start_urls = ['http://www.dianping.com/shop/7870836']
    a = ['http://www.ip138.com/ips1388.asp']
    for start_url in start_urls:
        start_url_content = get_html_content(start_url)
        print(start_url_content)
        # get_deatil(start_url_content)


