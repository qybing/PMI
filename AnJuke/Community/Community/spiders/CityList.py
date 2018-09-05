# -*- coding: utf-8 -*-
import scrapy

from tool.handle_redis import RedisClient


class CitylistSpider(scrapy.Spider):
    name = 'CityList'
    # allowed_domains = ['anjuke.com']
    start_urls = ['https://www.anjuke.com/sy-city.html']

    def parse(self, response):
        db = RedisClient()
        url_lists = response.xpath('//div[@class="letter_city"]/ul/li/div[@class="city_list"]/a/@href').extract()
        end = r'/community/?from=navigation'
        urls = []
        for url_list in url_lists:
            urls.append( url_list + end)
            db.add_value('AreaList:start_urls', url_list + end)
        print(urls)
        print('一共有{}个城市入库'.format(len(set(urls))))


