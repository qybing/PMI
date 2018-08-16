# -*- coding: utf-8 -*-
import logging

import redis
import scrapy
from parsel import Selector

from tool.handle_redis import RedisClient

logger = logging.getLogger(__name__)

class CityspiderSpider(scrapy.Spider):
    name = 'CitySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.xzl.anjuke.com/zu/?from=navigation']
    redis_key = "CitySpider:start_urls"

    def parse(self, response):
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'verify' in response.url:
            logger.info('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                db.add_value('CitySpider:start_urls', url)
        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
                logger.info('本url:{}-----没有搜索结果'.format(response.url))
                db.add_value('not_url:xzl', response.url)
        else:
            countys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
            for county in countys:
                db.add_value('CountySpider:start_urls', county)
            logger.info(countys)
            logger.info('一共{}个url已经入库完毕'.format(len(countys)))