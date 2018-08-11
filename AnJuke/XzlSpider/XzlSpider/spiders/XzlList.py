# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy import Request


class XzllistSpider(scrapy.Spider):
    name = 'XzlList'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "XzlList:start_urls"

    def parse(self, response):
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            url = str(response.meta.get('redirect_urls')[0])
            pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            r.rpush('XzlList:start_urls', url)
        else:
        # if '访问验证-安居客' not in city_content:
            city_content = response.text
            xpath_css = Selector(text=city_content)
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
            for sp_url in sp_urls:
                r.lpush('DetailSpider:start_urls', sp_url)
            print(sp_urls)
            print('已经入库完毕')
            next_page = xpath_css.xpath('//a[@class="aNxt"]/@href').extract_first()
            if next_page:
                print('翻页')
                print(next_page)
                yield Request(url=next_page,callback=self.parse)
            print(len(sp_urls))
