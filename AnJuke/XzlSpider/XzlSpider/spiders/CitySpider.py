# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector


class CityspiderSpider(scrapy.Spider):
    name = 'CitySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "CitySpider:start_urls"

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
                r.rpush('CitySpider:start_urls', url)
        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
                print('本url:{}-----没有搜索结果'.format(response.url))
                r.rpush('not_url:xzl', response.url)
        else:
            countys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            for county in countys:
                r.rpush('CountySpider:start_urls', county)
            print(countys)
            print('一共{}个url已经入库完毕'.format(len(countys)))