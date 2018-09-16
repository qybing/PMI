# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
from scrapy import signals
import base64

from scrapy.exceptions import IgnoreRequest

from tool.handle_redis import RedisClient


class CommunitySpiderMiddleware(object):
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
        spider.logger.info('Spider opened: %s' % spider.name)


class CommunityDownloaderMiddleware(object):
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
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentMiddleware(object):
    """ 换User-Agent """
    def process_request(self, request, spider):
        ua = UserAgent()
        agent = ua.random
        request.headers["User-Agent"] = agent
        print('添加了--------------UserAgent:{}'.format(agent))

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "xxxx"
proxyPass = "xxxxxxxxx"
# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
        print('添加了代理IP------------------------')

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
        # print('到这了：{}'.format('process_response'))
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
            print('该URL有验证码需求重新入队：{}含有验证码应该加入到队列中'.format(request.url))
            try:
                value_url = request.meta.get('redirect_urls')[0]
            except:
                value_url = request.url
            key = getattr(spider, 'redis_key')
            db.add_value(key, value_url)
            raise IgnoreRequest
        elif response.status==200 and 'verify' not in request.url:
            pass
            # print('该URL：{}，状态码为：{}'.format(response.url, response.status))
        else:
            print('状态码异常，请查看原因')
            print('该URL：{}，状态码为：{}'.format(response.url, response.status))
        return response

