# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector


class CityspiderSpider(scrapy.Spider):
    name = 'CitySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "CitySpider:start_urls"

    def parse(self, response):
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            url = str(response.meta.get('redirect_urls')[0])
            pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            r.rpush('crawl_city:start_urls', url)
        else:
        # if '访问验证-安居客' not in detail_urls_content:
            detail_urls_content = response.text
            pool = redis.ConnectionPool(host='localhost', port=6379,db=1, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            xpath_css = Selector(text=detail_urls_content)
            citys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            print(citys)
            for city in citys:
                r.lpush('crawl_county:start_urls',city)
            print('已经入库完毕')
            print(len(citys))
