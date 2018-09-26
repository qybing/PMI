# -*- coding: utf-8 -*-
import json
import re

import scrapy
import urllib

from scrapy.http import Request
from urllib.parse import urlencode
from urllib import parse

from scrapy_redis.spiders import RedisSpider

from xiecheng.tool.handle_redis import RedisClient


class CtripcitySpider(RedisSpider):
    name = 'CtripCity'
    # allowed_domains = ['hotels.ctrip.com']
    # start_urls = ['http://hotels.ctrip.com/']
    redis_key = "CtripCity:start_urls"

    def make_requests_from_url(self, url):
        api = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx?'
        data = {
            'cityId': url,
            'page': '1'
        }
        url = api+urllib.parse.urlencode(data)
        return Request(url,dont_filter=True)


    def parse(self, response):
        # print(response.url)
        html = json.loads(response.text)
        data_page = re.compile('data-pagecount=(\d+) name=')
        page = html['paging']
        page_count = re.findall(data_page, page)[0]
        value = html['HotelMaiDianData']['value']
        htllist = value['htllist'].replace("[", "").replace("]", "")
        db = RedisClient()
        htllists = htllist[1:-1].split('},{')
        house_base_url = 'http://hotels.ctrip.com/hotel/'
        for i in htllists:
            id_price = re.findall('"hotelid":"(\d+)","amount":"(\d+)"', i)
            hotel_id = id_price[0][0]
            low_price = id_price[0][1]
            hotel_url = house_base_url + hotel_id + '.html' + '&hotel_id={}&low_price={}'.format(hotel_id,low_price)
            print(hotel_url)
            print(hotel_id,low_price)
            db.add_value('hotel:start_urls',hotel_url)
        # print(len(htllists))
        # print(type(htllist))
        # print(response.text)
        now_page = re.findall('page=(\d+)', response.url)[0]
        print('当前第{}页，一共{}页'.format(now_page,page_count))
        if int(now_page) < int(page_count)+1:
            next_page = str(response.url).replace('page={}'.format(now_page), 'page={}'.format(int(now_page)+ 1))
            print('要访问第{}页，一共{}页'.format(int(now_page)+ 1, page_count))
            yield Request(url=next_page, callback=self.parse)
