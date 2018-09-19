# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import urllib
from random import choice
from urllib.parse import urlencode
from scrapy import signals
from urllib import parse

from tool import APIkeys
from tool.handle_redis import RedisClient
logger = logging.getLogger(__name__)


class GaodepoiSpiderMiddleware(object):
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


class GaodepoiDownloaderMiddleware(object):
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
        # print(request._url)
        url = parse.unquote(request._url)
        GDkeys = APIkeys.GDkeysList3
        GDkeys.extend(APIkeys.GDkeysList)
        GDkeys.extend(APIkeys.GDkeysList2)
        loc = url.find('&key=')
        if loc > 0:
            url = url[0:loc]
        params = {}
        a = '5505395763b84ab30052bde548ef6db2'
        params['key'] = choice(GDkeys)
        # params['key'] = a
        request._url = url + "&" + urllib.parse.urlencode(params)
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
        logger.warning('错误原因：{}'.format(exception))
        try:
            value_url = request.meta.get('redirect_urls')[0]
        except:
            value_url = request.url
        logger.info('IP代理不可用，本次url：{}   需要重新入库处理'.format(value_url))
        key = getattr(spider, 'redis_key')
        logger.info('本次的类名加属性名字为：{}'.format(key))
        db = RedisClient()
        db.add_value(key, value_url)

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
