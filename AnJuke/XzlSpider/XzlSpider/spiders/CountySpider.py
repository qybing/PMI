# -*- coding: utf-8 -*-
import logging

import redis
import scrapy
from parsel import Selector

from tool.handle_redis import RedisClient

logger = logging.getLogger(__name__)

class CountyspiderSpider(scrapy.Spider):
    name = 'CountySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "CountySpider:start_urls"

    def parse(self, response):
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'verify' in response.url:
            logger.info('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                db.add_value('CountySpider:start_urls', url)

        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
                logger.info('本url:{}-----没有搜索结果'.format(response.url))
                db.add_value('not_url:xzl', response.url)
        else:
            citys = xpath_css.xpath('/html/body/div[5]/div[2]/div/div[1]/div/a/@href').extract()
            for city in citys[1:]:
                db.add_value('TownSpider:start_urls',city)
            logger.info(citys)
            logger.info('一共{}个url已经入库完毕'.format(len(citys[1:])))
