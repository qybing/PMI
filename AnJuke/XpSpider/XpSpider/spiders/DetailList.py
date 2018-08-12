# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector
from scrapy import Request


class DetaillistSpider(scrapy.Spider):
    name = 'DetailList'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        city_content = response.text
        xpath_css = Selector(text=city_content)
        # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        # r = redis.Redis(connection_pool=pool)
        sp_urls = [str(sp_url).replace(r'loupan/', r'loupan/canshu-') for sp_url in
                   xpath_css.xpath('//*[@id="container"]/div[2]/div[1]/div[4]/div/@data-link').extract()]
        print(sp_urls)
        print(len(sp_urls))
        # for sp_url in sp_urls:
        #     r.rpush('sp_detail:start_urls', sp_url)
        # print(sp_urls)
        # print('一共{}个url已经入库完毕'.format(len(sp_urls)))
        next_page = xpath_css.xpath('//a[@class="next-page next-link"]/@href').extract_first()
        if next_page:
            print('翻页')
            print(next_page)
            yield Request(url=next_page, callback=self.parse)
