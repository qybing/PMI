# -*- coding: utf-8 -*-
import re

import redis
import scrapy
from parsel import Selector
from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from tools.handle_redis import RedisClient


class CrawlSpListSpider(RedisSpider):
    # class CrawlSpListSpider(scrapy.Spider):

    name = 'crawl_sp_list'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/baoshan/']
    redis_key = "crawl_sp_list:start_urls"

    def parse(self, response):
        # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        # r = redis.Redis(connection_pool=pool)
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'captcha-verify' in response.url:
            urls = response.meta.get('redirect_urls')
            print('遇到验证码了，url:{}----放入待爬队列里面'.format(urls))
            for url in urls:
                db.add_value('crawl_sp_list:start_urls', url)
        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
            print('本url:{}-----没有搜索结果'.format(response.url))
            db.add_value('not_url:sp', response.url)
        else:
            # if '访问验证-安居客' not in city_content:
            #     city_content = response.text
            # xpath_css = Selector(text=city_content)
            # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
            for sp_url in sp_urls:
                db.add_value('sp_detail:start_urls', sp_url)
            print(sp_urls)
            print('本页的URL：{}'.format(response.url))
            print('一共{}个url已经入库完毕'.format(len(sp_urls)))
            next_page = xpath_css.xpath('//a[@class="aNxt"]/@href').extract_first()
            if next_page:
                try:
                    page = re.search(r'p(\d+)', next_page)
                    print('第{}页---网址为：{}'.format(page.group(1), next_page))
                except Exception as e:
                    print('出错原因：{}'.format(e.args))
                yield Request(url=next_page, callback=self.parse)
