# -*- coding: utf-8 -*-
import logging

import redis
import scrapy
from parsel import Selector

from tool.handle_redis import RedisClient

logger = logging.getLogger(__name__)

class TownspiderSpider(scrapy.Spider):
    name = 'TownSpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "TownSpider:start_urls"

    def parse(self, response):
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'verify' in response.url:
            logger.info('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                db.add_value('TownSpider:start_urls', url)

        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
                logger.info('本url:{}-----没有搜索结果'.format(response.url))
                db.add_value('not_url:xzl', response.url)
        else:
            towns = xpath_css.xpath('//div[@class="sub-items"]/a/@href').extract()
            for town in towns[1:]:
                db.add_value('XzlList:start_urls', town)
            logger.info(towns[1:])
            logger.info('一共{}个url已经入库完毕'.format(len(towns[1:])))