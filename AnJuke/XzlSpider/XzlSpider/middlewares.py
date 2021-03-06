# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging

import requests
from time import sleep
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

import redis
from fake_useragent import UserAgent
from scrapy import signals
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
from scrapy.exceptions import IgnoreRequest

from tool.handle_redis import RedisClient

logger = logging.getLogger(__name__)

class XzlspiderSpiderMiddleware(object):
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


class XzlspiderDownloaderMiddleware(object):
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

proxyServer = "http-dyn.abuyun.com:9020"

# 隧道身份信息
proxyUser = "HE028T9448613Y4E"
proxyPass = "9CFB203161ACD693"
proxyAuth = 'Basic SEUwMjhUOTQ0ODYxM1k0RDo5Q0ZCMjAzMTYxQUNENjkz'

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

        logger.warning('错误原因：{}'.format(exception))
        try:
            value_url = request.meta.get('redirect_urls')[0]
        except:
            value_url = request.url
        logger.warning('IP代理不可用，本次url：{}   需要重新入库处理'.format(value_url))
        key = getattr(spider, 'redis_key')
        logger.warning('本次的类名加属性名字为：{}'.format(key))
        # if status:
        db = RedisClient()
        db.add_value(key, value_url)

    def process_response(self, request, response, spider):
        logger.info('到这了：{}'.format('process_response'))
        logger.info(request.url)
        db = RedisClient()
        if response.status==404:
            logger.warning('该URL：{}已经失效，放入失效库，可查看'.format(response.url))
            db.add_value('Xzl:not_url', response.url)
            raise IgnoreRequest
        if response.status != 200 and response.status != 404:
            logger.warning('----')
            logger.warning('出现问题了，这是状态码：{}'.format(response.status))
            try:
                value_url = request.meta.get('redirect_urls')[0]
            except:
                value_url = request.url
            if value_url and 'verify' not in value_url:
                logger.warning('可能被重定向了，本次url：{}   需要重新入库处理'.format(value_url))
                key = getattr(spider, 'redis_key')
                logger.warning('本次的类名加属性名字为：{}'.format(key))
                db.add_value(key, value_url)
            else:
                logger.error('这是个严重错误，request:{},response：{}'.format(request,response))
        if 'captcha' in request.url:
            logger.info('该URL：{}含有验证码应该加入到重'.format(response.url))
        return response


class ThreatDefenceRedirectMiddleware(RedirectMiddleware):
    proxies = {}
    def __init__(self, auth_encoding='latin-1'):
        self.auth_encoding = auth_encoding
        self.proxies[proxyServer] = proxyUser + proxyPass

    def _redirect(self, redirected, request, spider, reason):
        # 如果没有特殊的防范性重定向那就正常工作
        if not self.is_threat_defense_url(redirected.url):
            return super()._redirect(redirected, request, spider, reason)
        logger.warning('被重定向了，原因：{}，重定向到：{}，重定向之前：{}'.format(reason,redirected.url,request.url))
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
        logger.warning('更换了代理IP')
        request.dont_filter = True # 防止原始链接被标记为重复链接
        return request

    def is_threat_defense_url(self, url):
        return 'verify' in url or 'params' in url

url = 'http://127.0.0.1:5000/get'
class RandomProxy(object):
    def process_request(self, request, spider):
        # 随机取出一个代理ip
        for i in range(10):
            proxies_ips = requests.get(url)
            if i == 5:
                sleep(3)
            if proxies_ips.status_code == 200:
                request.meta['proxy'] = "http://{}".format(proxies_ips.text)
                logger.info('使用了代理-----------IP:{}'.format(proxies_ips.text))
                break
            if proxies_ips.status_code == 500:
                logger.info('没有可用代理了，我休息一会')
                sleep(5 * 60)

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
        logger.info('到这了：{}'.format('process_response'))
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
        if 'verify' in request.url:
            logger.info(request)
            # logger.info("有验证码了----{}".format(request.meta.get('redirect_urls')[0]))
        return response
