# -*- coding: utf-8 -*-
import scrapy


class CountyspiderSpider(scrapy.Spider):
    name = 'CountySpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
