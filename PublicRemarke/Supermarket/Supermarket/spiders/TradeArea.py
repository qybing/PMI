# -*- coding: utf-8 -*-
import scrapy


class TradeareaSpider(scrapy.Spider):
    name = 'TradeArea'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/luliang/ch20/g187']

    def parse(self, response):
        trade_area = response.xpath('//*[@id="bussi-nav"]/a/@href').extract()
        if trade_area:
            print(trade_area)
        else:
            print('没有商圈选项')
