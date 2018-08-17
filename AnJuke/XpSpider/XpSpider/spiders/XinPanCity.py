# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class XinpancitySpider(scrapy.Spider):
    name = 'XinPanCity'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.fang.anjuke.com/xzl/all/w5/?from=navigation']
    redis_key = "XinPanCity:start_urls"

    def parse(self, response):
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        citys = xpath_css.xpath('//div[@class="sel-city"]/div[@class="city-mod"]/dl/dd/a/@href').extract()
        urls_list = xpath_css.xpath(
            '//*[@id="container"]/div[2]/div[1]/div[@class="key-list"]/div/@data-link').extract()
        if 'verify' in response.url:
            urls = response.meta.get('redirect_urls')
            print('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
            for url in urls:
                db.add_value('XinPanCity:start_urls', url)
        if len(urls_list) > 0:
            for city in citys:
                db.add_value('DetailList:start_urls', city)
        print(citys)
        print('一共有{}个城市url,入库成功'.format(len(citys)))
