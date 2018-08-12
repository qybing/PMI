# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector


class XinpancitySpider(scrapy.Spider):
    name = 'XinPanCity'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        citys = xpath_css.xpath('//div[@class="sel-city"]/div[@class="city-mod"]/dl/dd/a/@href').extract()
        print(len(citys))
