# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector


class TownspiderSpider(scrapy.Spider):
    name = 'TownSpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "TownSpider:start_urls"

    def parse(self, response):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                r.rpush('TownSpider:start_urls', url)

        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
                print('本url:{}-----没有搜索结果'.format(response.url))
                r.rpush('not_url:xzl', response.url)
        else:
            towns = xpath_css.xpath('//div[@class="sub-items"]/a/@href').extract()
            for town in towns[1:]:
                r.rpush('XzlList:start_urls', town)
            print(towns[1:])
            print('一共{}个url已经入库完毕'.format(len(towns[1:])))