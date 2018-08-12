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
        pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                r.rpush('CitySpider:start_urls', url)
        # if '访问验证-安居客' not in detail_urls_content:
        else:
            detail_urls_content = response.text
            # pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            xpath_css = Selector(text=detail_urls_content)
            countys = xpath_css.xpath('/html/body/div[5]/div[2]/div/div[1]/div/a/@href').extract()
            # print(countys[1:])
            for county in countys[1:]:
                r.rpush('CountySpider:start_urls', county)
            print(countys[1:])
            print('一共{}个url已经入库完毕'.format(len(countys[1:])))