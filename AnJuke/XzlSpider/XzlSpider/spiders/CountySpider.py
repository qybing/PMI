# -*- coding: utf-8 -*-
import scrapy


class CountyspiderSpider(scrapy.Spider):
    name = 'CountySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "CitySpider:start_urls"

    def parse(self, response):
        pass
