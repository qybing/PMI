# -*- coding: utf-8 -*-
import logging

import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider

from tools.handle_redis import RedisClient

logger = logging.getLogger(__name__)

class CrawlCountySpider(RedisSpider):
    # class CrawlCountySpider(scrapy.Spider):

    name = 'crawl_county'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.sp.anjuke.com/zu/']
    redis_key = "crawl_county:start_urls"

    def parse(self, response):
        # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        # r = redis.Redis(connection_pool=pool)
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()

        if 'verify' in response.url:
            urls = response.meta.get('redirect_urls')
            logger.warning(response.url)

            logger.warning('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
            for url in urls:
                db.add_value('crawl_county:start_urls', url)
        # if '访问验证-安居客' not in detail_urls_content:
        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in detail_urls_content:
            logger.info('本url:{}-----没有搜索结果'.format(response.url))
            db.add_value('not_url:sp', response.url)
        else:
            countys = xpath_css.xpath('/html/body/div[5]/div[2]/div/div[1]/div/a/@href').extract()
            for county in countys[1:]:
                db.add_value('crawl_town:start_urls', county)
            logger.info(countys[1:])
            logger.info('一共{}个url已经入库完毕'.format(len(countys[1:])))
            # return citys
