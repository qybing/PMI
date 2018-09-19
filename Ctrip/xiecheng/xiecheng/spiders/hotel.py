# -*- coding: utf-8 -*-
import scrapy


class HotelSpider(scrapy.Spider):
    name = 'hotel'
    allowed_domains = ['hotels.ctrip.com']
    start_urls = ['http://hotels.ctrip.com/']

    def parse(self, response):
        pass
