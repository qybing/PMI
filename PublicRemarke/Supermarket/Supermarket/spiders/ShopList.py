# -*- coding: utf-8 -*-
import scrapy


class ShoplistSpider(scrapy.Spider):
    name = 'ShopList'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/shanghai/ch20/g187r812']

    def parse(self, response):
        shops_url = response.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a/@href').extract()
        print(shops_url)