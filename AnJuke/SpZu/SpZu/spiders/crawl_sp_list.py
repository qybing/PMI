# -*- coding: utf-8 -*-
import re

import redis
import scrapy
from parsel import Selector
from scrapy import Request
from scrapy_redis.spiders import RedisSpider


class CrawlSpListSpider(RedisSpider):
# class CrawlSpListSpider(scrapy.Spider):

    name = 'crawl_sp_list'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/baoshan/']
    redis_key = "crawl_sp_list:start_urls"


    def parse(self, response):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if 'captcha-verify' in response.url:
            urls = response.meta.get('redirect_urls')
            print('遇到验证码了，url:{}----放入待爬队列里面'.format(urls))
            for url in urls:
                r.rpush('crawl_sp_list:start_urls', url)
        else:
        # if '访问验证-安居客' not in city_content:
            city_content = response.text
            xpath_css = Selector(text=city_content)
            # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
            for sp_url in sp_urls:
                r.rpush('sp_detail:start_urls', sp_url)
            print(sp_urls)
            print('本页的URL：{}'.format(response.url))
            print('一共{}个url已经入库完毕'.format(len(sp_urls)))
            next_page = xpath_css.xpath('//a[@class="aNxt"]/@href').extract_first()
            if next_page:
                page = re.search(r'p(\d+)',next_page)
                print('第{}页---网址为：{}'.format(page.group(1),next_page))
                yield Request(url=next_page,callback=self.parse)

