# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy import Request
from scrapy_redis.spiders import RedisSpider


# class CrawlSpPageSpider(RedisSpider):
class CrawlSpPageSpider(scrapy.Spider):

    name = 'crawl_sp_page'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://bj.sp.anjuke.com/zu/chaoyang/']
    redis_key = "crawl_sp_page:start_urls"


    def parse(self, response):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                r.rpush('crawl_sp_page:start_urls', url)
        else:
            city_content = response.text
            xpath_css = Selector(text=city_content)
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            r.rpush('crawl_sp_list:start_urls', response.url)
            print('存入本页URL：{}'.format(response.url))
            print(response.url)
            next_page = xpath_css.xpath('//a[@class="aNxt"]/@href').extract_first()
            if next_page:
                print('翻页')
                print(next_page)
                yield Request(url=next_page,callback=self.parse)

