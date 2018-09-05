# -*- coding: utf-8 -*-
import scrapy

from tool.handle_redis import RedisClient


class CitylistSpider(scrapy.Spider):
    name = 'citylist'
    # allowed_domains = ['dianping.com']
    start_urls = [
        'http://www.dianping.com/citylist',
    # 'https://ip.cn/',
    #     'http://httpbin.org/get'
    #     'http://test.abuyun.com'
    ]

    # start_urls = ['https://sh.xzl.anjuke.com/zu/?from=navigation']

    redis_key = "CitylistSpider:start_urls"


    def parse(self, response):
        city_list = response.xpath('//div[@class="findHeight"]/a/@href').extract()
        base_url = 'http://www.dianping.com'
        end_url = '/ch20/g187'
        citys = []
        db = RedisClient()
        for city in city_list:
            citty = base_url+city.replace(r'//www.dianping.com','')+end_url
            citys.append(citty)
            db.add_value('TradeArea1:start_urls', citty)
        print(citys)
        print('一共有{}个城市URL入库成功'.format(len(citys)))
