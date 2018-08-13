# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider


class CrawlTownSpider(RedisSpider):
# class CrawlTownSpider(scrapy.Spider):
    name = 'crawl_town'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://wh.sp.anjuke.com/zu/jiangan/']
    redis_key = "crawl_town:start_urls"

    def parse(self, response):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url重新放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                r.rpush('crawl_town:start_urls', url)
        else:
        # if '访问验证-安居客' not in detail_urls_content:
            detail_urls_content = response.text
            # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            xpath_css = Selector(text=detail_urls_content)
            towns = xpath_css.xpath('//div[@class="sub-items"]/a/@href').extract()
            # print(towns[1:])
            for town in towns[1:]:
                r.rpush('crawl_sp_list:start_urls', town)
            print(towns[1:])
            print('一共{}个url已经入库完毕'.format(len(towns[1:])))
            # return citys


