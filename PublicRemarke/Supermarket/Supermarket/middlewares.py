# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random
import time

import faker
from fake_useragent import UserAgent
from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.exceptions import IgnoreRequest
from jovan.js_file import get_lxsdk_cuid, get_lxsdk_s, get_hc

from tool.handle_redis import RedisClient

useragent = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
     'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
     'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
     'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
             ]
class SupermarketSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.print('Spider opened: %s' % spider.name)


class SupermarketDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.print('Spider opened: %s' % spider.name)

class CookiesMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        # dict={'_hc.v':get_hcv()}
        # request.cookies =dict
        print('更换了--------------Cookies:{}'.format(dict))


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        # a = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
        #      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
        #      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
        #      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        #      'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
        #      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
        #      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        #      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        #      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
        #      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        #      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        #      ]
        # ua = UserAgent()
        # agent = ua.random
        agent = random.choice(useragent)
        # agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        same = get_lxsdk_cuid(agent)

        # agent = random.choice
        # f = faker.Faker(locale='zh_cn')
        # agent = f.user_agent()
        request.headers['Host'] = 'www.dianping.com'
        # request.headers['Pragma'] = 'no-cache'
        # request.headers['Cache-Control'] = 'no-cache'
        request.headers['Upgrade-Insecure-Requests'] = 1
        request.headers["User-Agent"] = agent
        cook = '_lxsdk_cuid={}; _lxsdk={}; _hc.v={}; _lxsdk_s={}'.format(same,same,get_hc(),get_lxsdk_s())
        request.headers["Cookie"] = cook
        cookie = {'_lxsdk_cuid': same,
                  '_lxsdk': same,
                  '_hc.v': get_hc(),
                  '_lxsdk_s': get_lxsdk_s(),
                  }
        # request.cookies = cookie

        print('更换了--------------UserAgent:{}'.format(agent))


# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "HE028T9448613Y4D"
proxyPass = "9CFB203161ACD692"

# for Python2
# proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)


# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer

        # request.meta["proxy"] = proxyServer
        # request.headers["Proxy-Authorization"] = proxyAuth
        print('添加了代理IP----------------')

    def process_exception(self, request, exception, spider):
        print('错误原因：{}'.format(exception))
        try:
            value_url = request.meta.get('redirect_urls')[0]
        except:
            value_url = request.url
        print('IP代理不可用，本次url：{}   需要重新入库处理'.format(value_url))
        key = getattr(spider, 'redis_key')
        print('本次的类名加属性名字为：{}'.format(key))
        db = RedisClient()
        db.add_value(key, value_url)

    def process_response(self, request, response, spider):
        print('到这了：{}'.format('process_response'))
        # print('该URL：{}，状态码为：{}'.format(response.url,response.status))
        db = RedisClient()
        if response.status in [404, 403]:
            if response.status ==404:
                print('该URL：{}已经失效，状态码为：{}'.format(response.url, response.status))
                db.add_value('not_url:Shop', response.url)
            else:
                print('该IP已经被封，该url:{}，需要重新入队列，状态码为：{}'.format(response.url,response.status))
                key = getattr(spider, 'redis_key')
                db.add_value(key, response.url)
            raise IgnoreRequest
        elif response.status != 200 and response.status not in [404, 403]:
            print('----')
            print('该URL：{}      ，状态码为：{}'.format(response.url, response.status))
            try:
                value_url = request.meta.get('redirect_urls')[0]
            except:
                value_url = request.url
            if value_url and 'verify' not in value_url:
                print('可能被重定向了，本次url：{}   需要重新入库处理'.format(value_url))
                key = getattr(spider, 'redis_key')
                print('本次的类名加属性名字为：{}'.format(key))
                db.add_value(key, value_url)
            else:
                print('这是个严重错误，request:{},response：{}'.format(request, response))
        elif 'verify' in request.url:
            print('该URL：{}含有验证码应该加入到队列中'.format(request.url))
        elif response.status==200 and 'verify' not in request.url:
            print('该URL：{}，状态码为：{}'.format(response.url, response.status))
        else:
            print('状态码异常，请查看原因')
            print('该URL：{}，状态码为：{}'.format(response.url, response.status))

        return response



class ProxyRequestsMiddleware(object):
    def process_request(self, request, spider):
        # ua = UserAgent()
        # agent = ua.chrome
        # f = faker.Faker(locale='zh_cn')
        # agent = f.user_agent()
        agent = random.choice(useragent)
        same = get_lxsdk_cuid(agent)
        cook = '_lxsdk_cuid={}; _lxsdk={}; _hc.v={}; _lxsdk_s={}'.format(
            same, same, get_hc(), get_lxsdk_s())
        # cook = '_lxsdk_cuid={}; _lxsdk={}; _hc.v={}; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s={}'.format(same,same,get_hc(),get_lxsdk_s())
        cook1 = 'cy=1236; cityid=1236; cye=huixian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=165c6b8e911c8-0383cc5ec3114e-37664109-144000-165c6b8e91289; _lxsdk=165c6b8e911c8-0383cc5ec3114e-37664109-144000-165c6b8e91289; _hc.v=0c84e8b5-c945-5c86-bb54-94e4936012e5.1536637332; s_ViewType=10; cye=beijing; _lxsdk_s=165cb7d7e23-268-18-f1%7C%7C87'
        # print(cook)
        headers = {
            'Host':'www.dianping.com',
            'Upgrade-Insecure-Requests':'1',
            'Cookie':cook,
            'User-Agent':agent ,
            # 'Proxy-Connection':'keep-alive'
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

        proxies = {
            # "http": proxyMeta,
            "https": proxyMeta,
        }
        proxiess = {
            "https": "http://140.255.6.45:5649",
            # "https": "http://118.79.54.90:6996",
            # "https": "http://117.42.201.221:6214",

        }

        import requests
        #s = requests.Session()
        #base = 'https://www.dianping.com/'
        try:
            # start_url = requests.get(base, headers=headers, proxies=proxies, timeout=15)
            # print(start_url.text)
            res = requests.get(request.url, headers=headers, proxies=proxies, timeout=15)
            if res.status_code != 200 or len(res.text) < 560:
                if res.status_code == 403 or res.status_code == 404:
                    content = '页面无法访问'
                else:
                    content = res.text
                print('该URL:{},状态码：{}，内容为：{}'.format(request.url, res.status_code, content))
                key = getattr(spider, 'redis_key')
                db = RedisClient()
                print('该URL：{}需要重新入队列'.format(request.url))
                db.add_value(key, request.url)
                raise IgnoreRequest
            else:
                from scrapy.http.response.html import HtmlResponse
                rs = res.content.decode('utf-8')
                # print(rs)
                response = HtmlResponse(url=request.url, body=res.content.decode('utf-8'), encoding="utf-8", request=request)
                return response
        except Exception as e:
            print('出现错误，原因{}'.format(e.args))
            key = getattr(spider, 'redis_key')
            db = RedisClient()
            print('该URL：{}需要重新入队列'.format(request.url))
            db.add_value(key, request.url)
            raise IgnoreRequest
