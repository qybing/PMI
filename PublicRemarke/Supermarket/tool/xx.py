import json
import re
import time
from random import random

import requests
from fake_useragent import UserAgent
from parsel import Selector


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
a = str(hex(int(65536 * (1 + random()))))[3:]
print(a)
ua = UserAgent()
agent = ua.random
headers={
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate',
# 'Accept-Language':'zh-CN,zh;q=0.9',
# 'Cache-Control':'no-cache',
# 'Connection':'keep-alive',
# 'Cookie':'s_ViewType=10; _lxsdk_cuid=16584f26411c8-053ce1508e1bb1-2711639-100200-16584f26412c8; _lxsdk=16584f26411c8-053ce1508e1bb1-2711639-100200-16584f26412c8; _hc.v=22baacb8-5b7b-bc0e-3786-233fcf8541b7.1535533803; _lxsdk_s=16584f26414-d22-5b5-1ee%7C%7C42',
# 'Host':'www.dianping.com',
# 'Pragma':'no-cache',
# 'Upgrade-Insecure-Requests':'1',
    # 'Cookie':get_hcv(),
'User-Agent':agent,
    # 'Cookie':'_lxsdk_cuid=1659e1d2b71c8-09c4421e7c65e4-37664109-144000-1658e1d2b71c8; _lxsdk=1658e08c9d457-03f523ea4f47fe-37664109-144000-1658e08c9d6c8; _hc.v=717e6927-3c19-a6e0-ae54-7d4d84fe190a.1535687601; s_ViewType=10; _lxsdk_s=1658e1d2b85-a58-a12-cd7%7C%7C23'
}
proxies = {
  # "https": "http://115.196.46.164:1246",
  # "https": "http://118.79.54.90:6996",
  "https": "http://115.202.129.74:7586",

}
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"
# 代理隧道验证信息
proxyUser = "xxxxxx"
proxyPass = "xxxxxxxxx"
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxiess = {
    # "http": proxyMeta,
    "https": proxyMeta,
}
'http://m.dianping.com/shop/2619856'
url = 'http://www.dianping.com/shop/15748800'
test = 'https://ip.cn/'
res = requests.get(url,headers=headers,proxies=proxiess,allow_redirects=False)
a = res.text
print(a)
# b = re.findall('<meta name="location" content="province=(.*?);city=(.*?);">',a,re.S)
# print(b[0][0],b[0][1])
# b = a.split(r'id="shop-detail">')[-1]
# c = b.split('</textarea>')[0]
# d = json.loads(c)
# address = d['address']
# html = Selector(res.text)
# print(res.text)
# shopName = html.xpath('//div[@class="shopPicBg"]/h1[@class="shop-name"]/text()').extract_first()
# reviewCount = html.xpath('//span[@class="itemNum-val"]/text()').extract_first()
# avgPrice = html.xpath('//span[@class="price"]/text()').extract_first()
# productScore = html.xpath('//div[@class="desc"]/span[1]/text()').extract_first()
# environmentScore = html.xpath('//div[@class="desc"]/span[2]/text()').extract_first()
# serviceScore = html.xpath('//div[@class="desc"]/span[3]/text()').extract_first()
# telephone = html.xpath('/html/body/div[5]/div[1]/div/div/a/@href').extract_first()
# rank = html.xpath("/html/body/div[3]/div/div[1]/p/span[1]/@class").extract_first()
# rank_handle = re.findall('\d+', rank)
# rankStars = ''.join(rank_handle) if rank_handle else 0
# shopId = re.findall(r'\d+',url)
# shopHours = html.xpath('//div[@class="businessTime"]/text()').extract_first()
# print('shopHours',shopHours)
# print('shopId',shopId[0])
# print('shopName',shopName)
# print('address',address)
# print('reviewCount',reviewCount)
# print('avgPrice',avgPrice)
# print('productScore',productScore)
# print('environmentScore',environmentScore)
# print('serviceScore',serviceScore)
# print('telephone',telephone)
# print('rankStars',rankStars)

