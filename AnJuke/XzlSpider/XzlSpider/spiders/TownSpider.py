# -*- coding: utf-8 -*-
import scrapy


class TownspiderSpider(scrapy.Spider):
    name = 'TownSpider'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
