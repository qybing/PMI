# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector


class CrawlCitySpider(scrapy.Spider):
    name = 'crawl_city'
    redis_key = "crawl_city:start_urls"
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/']

    def parse(self, response):
        detail_urls_content = response.text
        if '访问验证-安居客' not in detail_urls_content:
            pool = redis.ConnectionPool(host='localhost', port=6379,db=1, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            xpath_css = Selector(text=detail_urls_content)
            citys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            print(citys)
            for city in citys:
                r.lpush('crawl_city:start_urls',city)
            print('已经入库完毕')
            print(len(citys))
            # return citys
        else:
            print('有验证码')
