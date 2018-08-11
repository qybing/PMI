# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector


class CrawlCountySpider(scrapy.Spider):
    name = 'crawl_county'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/']
    redis_key = "crawl_county:start_urls"

    def parse(self, response):
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            url = str(response.meta.get('redirect_urls')[0])
            pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            r.rpush('crawl_county:start_urls', url)
        # if '访问验证-安居客' not in detail_urls_content:
        else:
            detail_urls_content = response.text
            pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            xpath_css = Selector(text=detail_urls_content)
            countys = xpath_css.xpath('/html/body/div[5]/div[2]/div/div[1]/div/a/@href').extract()
            print(countys[1:])
            for county in countys[1:]:
                r.lpush('crawl_town:start_urls', county)
            print('已经入库完毕')
            print(len(countys[1:]))
            # return citys

