# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider


# class CrawlCitySpider(scrapy.Spider):
from tools.handle_redis import RedisClient


class CrawlCitySpider(RedisSpider):
    name = 'crawl_city'
    redis_key = "crawl_city:start_urls"
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/']

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
                db.add_value('crawl_city:start_urls',url)
                # is_repeat = r.sadd('crawl_city:start_urls', url)
                # if is_repeat==1:
                #     print('url:{}-----插入成功'.format(url))
                # else:
                #     print('url:{}-----已经存在队列中'.format(url))
        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
            print('本url:{}-----没有搜索结果'.format(response.url))
            db.add_value('not_url:sp', response.url)
            # r.sadd('not_url:sp', response.url)
        else:
            # if '访问验证-安居客' not in detail_urls_content:
            # pool = redis.ConnectionPool(host='localhost', port=6379,db=0, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            citys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            for city in citys:
                db.add_value('crawl_county:start_urls', city)
                # r.rpush(('CountySpider:start_urls',str(city).replace('sp','xzl')))
            print(citys)
            print('一共{}个url已经入库完毕'.format(len(citys)))
            # return citys
