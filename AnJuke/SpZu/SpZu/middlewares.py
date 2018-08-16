# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging

import requests
import redis
from time import sleep
import base64
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

from scrapy import signals
from fake_useragent import UserAgent

from tools.handle_redis import RedisClient

logger = logging.getLogger(__name__)

class SpzuSpiderMiddleware(object):
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


class SpzuDownloaderMiddleware(object):
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
        # logger.info(agent)
        logger.info('更换了--------------UserAgent:{}'.format(agent))

    # def process_exception(self, request, exception, spider):
    #     logger.info('UserAgent不可用，本次url需要重新入库处理')
    #     logger.info(exception)
    #     status = exception.osError
    #     key = getattr(spider, 'redis_key')
    #     if status:
    #         pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
    #         r = redis.Redis(connection_pool=pool)
    #         r.rpush(key, request.url)
    #         logger.info('url:{} 入库成功'.format(request.url))

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 隧道身份信息
proxyUser = "H58053994503UZ9F"
proxyPass = "6A29C1C28E3929F7"
# proxyAuth = "Basic " + base64.urlsafe_b64encode(proxyUser + ":" + proxyPass)
proxyAuth = "Basic " + "SEUwMjhUOTQ0ODYxM1k0RDo5Q0ZCMjAzMTYxQUNENjky"
class ProxyMiddleware(HttpProxyMiddleware):
    proxies = {}

    def __init__(self, auth_encoding='latin-1'):
        self.auth_encoding = auth_encoding
        self.proxies[proxyServer] = proxyUser + proxyPass

    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
        logger.info('添加了代理IP----------------')

    def process_exception(self, request, exception, spider):

        logger.info('错误原因：{}'.format(exception))
        try:
            value_url = request.meta.get('redirect_urls')[0]
        except:
            value_url = request.url
        logger.info('IP代理不可用，本次url：{}   需要重新入库处理'.format(value_url))
        key = getattr(spider, 'redis_key')
        logger.info('本次的类名加属性名字为：{}'.format(key))
        # if status:
        db = RedisClient()
        db.add_value(key, value_url)

    def process_response(self, request, response, spider):
        logger.info('到这了：{}'.format('process_response'))
        logger.info(request.url)
        if response.status != 200:
            logger.info('----')
            logger.info('出现问题了，这是状态码：{}'.format(response.status))
            try:
                value_url = request.meta.get('redirect_urls')[0]
            except:
                value_url = request.url
            if value_url and 'verify' not in value_url:
                logger.info('可能被重定向了，本次url：{}   需要重新入库处理'.format(value_url))
                key = getattr(spider, 'redis_key')
                logger.info('本次的类名加属性名字为：{}'.format(key))
                # if status:
                db = RedisClient()
                db.add_value(key, value_url)
            else:
                logger.info('这是个严重错误，request:{},response'.format(request,response))
        if 'captcha' in request.url:
            logger.info(request)
        return response


url = 'http://127.0.0.1:5000/get'
class RandomProxy(object):
    def process_request(self, request, spider):
        # 随机取出一个代理ip
        for i in range(10):
            proxies_ips = requests.get(url)
            # proxies_ips.status_code == 200
            if i == 5:
                sleep(3)
            if proxies_ips.status_code == 200:
                request.meta['proxy'] = "http://{}".format(proxies_ips.text)
                logger.info('使用了代理-----------IP:{}'.format(proxies_ips.text))
                break
            if proxies_ips.status_code == 500:
                logger.info('没有可用代理了，我休息一会')
                sleep(5 * 60)
        # else:
        #     sleep(2)
        #     proxies_ips = requests.get(url)
        #     request.meta['proxy'] = "http://{}".format(proxies_ips.text)
        #     logger.info('使用第二个更换了代理IP:{}'.format(proxies_ips.text))

    #     else:
    #         url = 'http://127.0.0.1:8080/get'
    #         proxies_ips = requests.get(url)
    #         if proxies_ips.status_code == 200:
    #             # logger.info(proxies_ips)
    #             request.meta['proxy'] = "http://{}".format(proxies_ips.text)
    #             logger.info('使用第一个更换了代理IP:{}'.format(proxies_ips.text))
    #         else:
    #             sleep(10 * 60)

    def process_exception(self, request, exception, spider):

        logger.info('错误原因：{}'.format(exception))
        try:
            value_url = request.meta.get('redirect_urls')[0]
        except:
            value_url = request.url
        logger.info('IP代理不可用，本次url：{}   需要重新入库处理'.format(value_url))
        key = getattr(spider, 'redis_key')
        logger.info('本次的类名加属性名字为：{}'.format(key))
        db = RedisClient()
        db.add_value(key, value_url)

    def process_response(self, request, response, spider):
        logger.info('到这了：{}   本页的URL:{}'.format('process_response',request.url))
        # logger.info(response.status)
        logger.info(request.url)
        if response.status != 200:
            logger.info('出现问题了，这是状态码：{}'.format(request.status))
            logger.info(request.url)
            logger.info('仔细看状态码')
            sleep(2)
            proxies_ips = requests.get(url)
            request.meta['proxy'] = "http://{}".format(proxies_ips.text)
            logger.info('使用第二个更换了代理IP:{}'.format(proxies_ips.text))
            return request
        if 'captcha-verify' in request.url:
            logger.info(request)
            # logger.info("有验证码了----{}".format(request.meta.get('redirect_urls')[0]))
        return response
