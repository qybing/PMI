import json
import random
import re
import time

import requests
from fake_useragent import UserAgent
from parsel import Selector

from jovan.js_file import get_lxsdk_cuid, get_lxsdk_s, get_hc

a = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
     'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134']

def get_text(i):
    ua = UserAgent()
    # agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    agent = random.choice(a)
    print(agent)
    same = get_lxsdk_cuid(agent)
    cook = '_lxsdk_cuid={}; _lxsdk={}; _hc.v={}; _lxsdk_s={}'.format(
        same, same, get_hc(), get_lxsdk_s())
    headers={
        'Host':'www.dianping.com',
        'Upgrade-Insecure-Requests':'1',
        'Cookie':cook,
        'User-Agent':agent,
    }
    proxies = {
      # "https": "https://106.110.91.225:4224",
      "https": "http://118.190.95.35:9001",
      # "https": "http://117.42.201.221:6214",

    }
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

    proxiess = {
        # "http": proxyMeta,
        "https": proxyMeta,
    }
    base = 'https://www.dianping.com'
    url = 'http://www.dianping.com/shop/50176260'
    test = 'https://ip.cn/'
    # for i in range(10):
    # b = requests.get(base,headers=headers,proxies=proxiess,allow_redirects=False)
    # print(b.cookies.get_dict())
    c = requests.get(url,headers=headers,proxies=proxiess)
    # print('这是第{}'.format(i)+re.findall('<div class="well">(.*?)GeoIP',b.text)[0])
    # print('这是第{}'.format(i)+re.findall('<div class="well">(.*?)GeoIP',c.text)[0])
    # print(b.text)
    print(c.content.decode('utf-8'))
    print('这是第{}'.format(i)+'======================')
if __name__ == '__main__':
    a = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
         'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
         'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
         'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36']
    # get_text(1)
    for i in range(3):
        get_text(i)
    # b = s.get(url,headers=headers,proxies=proxiess,allow_redirects=False)
    # print(res.get_)
    # c = b.text
    # print('{}---------------'.format(i),b.text)







































































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

