# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider


# class CrawlCitySpider(scrapy.Spider):


class CrawlCitySpider(RedisSpider):

    name = 'crawl_city'
    redis_key = "crawl_city:start_urls"
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/']

    def parse(self, response):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                r.rpush('crawl_city:start_urls', url)
        else:
        # if '访问验证-安居客' not in detail_urls_content:
            detail_urls_content = response.text
            # pool = redis.ConnectionPool(host='localhost', port=6379,db=0, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            xpath_css = Selector(text=detail_urls_content)
            citys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            for city in citys:
                r.rpush('crawl_county:start_urls',city)
                # r.rpush(('CountySpider:start_urls',str(city).replace('sp','xzl')))
            print(citys)
            print('一共{}个url已经入库完毕'.format(len(citys)))
            # return citys
