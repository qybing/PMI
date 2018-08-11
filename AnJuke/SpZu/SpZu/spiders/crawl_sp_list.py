# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy import Request
from scrapy_redis.spiders import RedisSpider


# class CrawlSpListSpider(RedisSpider):
class CrawlSpListSpider(scrapy.Spider):

    name = 'crawl_sp_list'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/dahua/']
    redis_key = "crawl_sp_list:start_urls"


    def parse(self, response):
        city_content = response.text
        if '访问验证-安居客' not in city_content:
            xpath_css = Selector(text=city_content)
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
            for sp_url in sp_urls:
                r.lpush('sp_detail:start_urls', sp_url)
            print(sp_urls)
            print('已经入库完毕')
            next_page = xpath_css.xpath('//a[@class="aNxt"]/@href').extract_first()
            if next_page:
                print('翻页')
                print(next_page)
                yield Request(url=next_page,callback=self.parse)
            print(len(sp_urls))
        else:
            print('有验证码')

