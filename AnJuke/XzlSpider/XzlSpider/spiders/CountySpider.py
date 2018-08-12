# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector


class CountyspiderSpider(scrapy.Spider):
    name = 'CountySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "CountySpider:start_urls"

    def parse(self, response):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=1,decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                r.rpush('CountySpider:start_urls', url)
        else:
        # if '访问验证-安居客' not in detail_urls_content:
            detail_urls_content = response.text
            # pool = redis.ConnectionPool(host='localhost', port=6379,db=1,decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            xpath_css = Selector(text=detail_urls_content)
            citys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            for city in citys:
                r.rpush('TownSpider:start_urls',city)
                # r.rpush(('CountySpider:start_urls',str(city).replace('sp','xzl')))
            print(citys)
            print('一共{}个url已经入库完毕'.format(len(citys)))
