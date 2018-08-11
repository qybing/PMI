# -*- coding: utf-8 -*-
import scrapy


class CityspiderSpider(scrapy.Spider):
    name = 'CitySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
