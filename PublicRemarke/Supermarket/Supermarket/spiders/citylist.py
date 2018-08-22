# -*- coding: utf-8 -*-
import scrapy


class CitylistSpider(scrapy.Spider):
    name = 'citylist'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/citylist']

    def parse(self, response):
        city_list = response.xpath('//div[@class="findHeight"]/a/@href').extract()
        base_url = 'http://www.dianping.com'
        end_url = '/ch20/g187'
        citys = []

        for city in city_list:
            citys.append(base_url+city.replace(r'//www.dianping.com','')+end_url)
        print(citys)
        print(len(citys))
            # print(city.replace(r'//www.dianping.com/',''))
