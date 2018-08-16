# -*- coding: utf-8 -*-
import logging
import re

import redis
import scrapy
from parsel import Selector
from scrapy import Request

from tool.handle_redis import RedisClient

logger = logging.getLogger(__name__)

class XzllistSpider(scrapy.Spider):
    name = 'XzlList'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "XzlList:start_urls"

    def parse(self, response):
        # pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
        # r = redis.Redis(connection_pool=pool)
        db = RedisClient()
        city_content = response.text
        xpath_css = Selector(text=city_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'verify' in response.url:
            logger.info('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                db.add_value('XzlList:start_urls', url)

        elif len(sp_urls) < 0 :
                logger.info('本url:{}-----没有搜索结果'.format(response.url))
                db.add_value('not_url:xzl', response.url)
        else:
            sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
            for sp_url in sp_urls:
                db.add_value('DetailSpider:start_urls', sp_url)
            logger.info(sp_urls)
            logger.info('一共{}个url已经入库完毕'.format(len(sp_urls)))
            next_page = xpath_css.xpath('//a[@class="aNxt"]/@href').extract_first()
            if next_page:
                try:
                    page = re.search(r'p(\d+)', next_page)
                    logger.info('第{}页---网址为：{}'.format(page.group(1), next_page))
                except Exception as e:
                    logger.info('出错原因：{}'.format(e.args))
                yield Request(url=next_page,callback=self.parse)
