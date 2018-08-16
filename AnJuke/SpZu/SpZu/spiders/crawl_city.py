# -*- coding: utf-8 -*-
import logging

import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider

from tools.handle_redis import RedisClient


logger = logging.getLogger(__name__)
# class CrawlCitySpider(scrapy.Spider):
class CrawlCitySpider(RedisSpider):
    name = 'crawl_city'
    redis_key = "crawl_city:start_urls"
    # allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/shou/']

    def parse(self, response):
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'verify' in response.url:
            urls = response.meta.get('redirect_urls')
            logger.info(response.url)
            logger.info('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
            for url in urls:
                db.add_value('crawl_city:start_urls',url)
        elif len(sp_urls) < 0 :
            logger.info('本url:{}-----没有搜索结果'.format(response.url))
            db.add_value('not_url:sp', response.url)
            # r.sadd('not_url:sp', response.url)
        else:
            citys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            for city in citys:
                db.add_value('crawl_county:start_urls', city)
                # r.rpush(('CountySpider:start_urls',str(city).replace('sp','xzl')))
            logger.info(citys)
            logger.info('一共{}个url已经入库完毕'.format(len(citys)))
            # return citys
