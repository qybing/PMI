# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider

from tools.handle_redis import RedisClient


class CrawlTownSpider(RedisSpider):
    # class CrawlTownSpider(scrapy.Spider):
    name = 'crawl_town'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://wh.sp.anjuke.com/zu/jiangan/']
    redis_key = "crawl_town:start_urls"

    def parse(self, response):
        # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        # r = redis.Redis(connection_pool=pool)
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'captcha-verify' in response.url:
            urls = response.meta.get('redirect_urls')
            print('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
            for url in urls:
                db.add_value('crawl_town:start_urls', url)

        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
            print('本url:{}-----没有搜索结果'.format(response.url))
            db.add_value('not_url:sp', response.url)

        else:
            # if '访问验证-安居客' not in detail_urls_content:
            #     detail_urls_content = response.text
            # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            # xpath_css = Selector(text=detail_urls_content)
            towns = xpath_css.xpath('//div[@class="sub-items"]/a/@href').extract()
            # print(towns[1:])
            for town in towns[1:]:
                db.add_value('crawl_sp_list:start_urls', town)
            print(towns[1:])
            print('一共{}个url已经入库完毕'.format(len(towns[1:])))
            # return citys
