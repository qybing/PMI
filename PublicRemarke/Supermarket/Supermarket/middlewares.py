# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
from random import random
import time

from fake_useragent import UserAgent
from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.exceptions import IgnoreRequest

from tool.handle_redis import RedisClient


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

class CookiesMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        dict={'_hc.v':get_hcv()}
        request.cookies =dict
        print('更换了--------------Cookies:{}'.format(dict))


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        ua = UserAgent()
        agent = ua.random
        # request.headers['Host'] = 'www.dianping.com'
        # request.headers["Connection"] = 'keep-alive'
        # request.headers['Pragma'] = 'no-cache'
        # request.headers['Cache-Control'] = 'no-cache'
        # request.headers['Upgrade-Insecure-Requests'] = 1
        request.headers["User-Agent"] = agent
        # request.headers[
        #     "Accept"] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        # request.headers['Accept-Encoding'] = 'gzip, deflate'
        # request.headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
        request.headers['Cookie'] = '_hc.v={};'.format(get_hcv())
        # request.headers['Cookie'] = '{}'.format('_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1657a454988c8-064dd5236927-2711639-100200-1657a454988c8; _lxsdk=1657a454988c8-064dd5236927-2711639-100200-1657a454988c8; _hc.v=3198aa04-8172-a269-8faa-f1384c933a17.1535354686; s_ViewType=10; cy=7; cye=shenzhen; _lxsdk_s=1657f41d359-85f-3f0-ac9%7C%7C927')

        print('更换了--------------UserAgent:{}'.format(agent))


# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "xxx"
proxyPass = "xxxxxxx"
# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
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
        ua = UserAgent(use_cache_server=False)
        agent = ua.random
        headers = {
            # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # 'Accept-Encoding':'gzip, deflate',
            # 'Accept-Language':'zh-CN,zh;q=0.9',
            # 'Cache-Control':'no-cache',
            # 'Connection':'keep-alive',
            # 'Cookie':'s_ViewType=10; _lxsdk_cuid=16584f26411c8-053ce1508e1bb1-2711639-100200-16584f26412c8; _lxsdk=16584f26411c8-053ce1508e1bb1-2711639-100200-16584f26412c8; _hc.v=22baacb8-5b7b-bc0e-3786-233fcf8541b7.1535533803; _lxsdk_s=16584f26414-d22-5b5-1ee%7C%7C42',
            # 'Host':'www.dianping.com',
            # 'Pragma':'no-cache',
            # 'Upgrade-Insecure-Requests':'1',
            'Cookie': get_hcv(),
            'User-Agent':agent ,
        }
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"
        # 代理隧道验证信息
        proxyUser = "xxxxxx"
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
        import requests
        res = requests.get(request.url,headers=headers,proxies=proxies)
        if res.status_code !=200:
            print('该URL:{},状态码：{}，内容为：{}'.format(request.url,res.status_code,res.text))
            key = getattr(spider, 'redis_key')
            db = RedisClient()
            print('该URL：{}需要重新入队列'.format(request.url))
            db.add_value(key,request.url)
            raise IgnoreRequest
        else:
            from scrapy.http.response.html import HtmlResponse
            response = HtmlResponse(url=request.url,body=res.text,encoding="utf-8",request=request)
            return response