# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import redis
from fake_useragent import UserAgent
from scrapy import signals


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
        # print(agent)
        print('更换了UserAgent:{}'.format(agent))


class RandomProxy(object):
    # def process_request(self, request, spider):
    #     # 随机取出一个代理ip
    #     url = 'http://127.0.0.1:5000/get'
    #     proxies_ips = requests.get(url)
    #     if proxies_ips.status_code == 200:
    #         # print(proxies_ips)
    #         request.meta['proxy'] = "http://{}".format(proxies_ips.text)
    #         print('使用第一个更换了代理IP:{}'.format(proxies_ips.text))
    #     else:
    #         url = 'http://127.0.0.1:8080/get'
    #         proxies_ips = requests.get(url)
    #         if proxies_ips.status_code == 200:
    #             # print(proxies_ips)
    #             request.meta['proxy'] = "http://{}".format(proxies_ips.text)
    #             print('使用第一个更换了代理IP:{}'.format(proxies_ips.text))
    #         else:
    #             sleep(10 * 60)

    def process_response(self, request, response, spider):
        print('到这了')
        print(request.url)
        # print(response.status)
        if response.status==302:
            print('有验证码了，被重定向了')
            print('终于看到你了')
        if 'captcha-verify' in request.url:
            print(request)
            print("这是到哪了呀，你知道吗{}".format(request.meta.get('redirect_urls')[0]))
            r = redis.Redis(host='127.0.0.1', port=6379, db=1)
            # r.lpush('sp_zu:start_urls',response['meta'])
        return response
