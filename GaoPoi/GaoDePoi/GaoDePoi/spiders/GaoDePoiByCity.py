# -*- coding: utf-8 -*-
import json
import logging
import math
import re
import urllib
from urllib.parse import urlencode

from random import choice

import pandas as pd
import scrapy
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
from urllib import parse
from GaoDePoi.items import GaodepoiItem
from tool import APIkeys
from tool.handle_redis import RedisClient


class GaodepoibycitySpider(scrapy.Spider):
    name = 'GaoDePoiByCity'
    allowed_domains = ['restapi.amap.com']
    start_urls = ['http://restapi.amap.com/']
    redis_key = 'GaoDePoiByCity:start_urls'


    def make_requests_from_url(self, url):
        url = parse.unquote(url)
        GDkeys = APIkeys.GDkeysList3
        GDkeys.extend(APIkeys.GDkeysList)
        GDkeys.extend(APIkeys.GDkeysList2)
        loc = url.find('&key=')
        if loc > 0:
            url = url[0:loc]
        params = {}
        params['key'] = choice(GDkeys)
        url = url + "&" + urllib.parse.urlencode(params)
        return Request(url, dont_filter=True)

    def parse(self, response):
        res = json.loads(response.text)
        db = RedisClient()
        item = GaodepoiItem()
        if res['status'] == '1':
            count = int(res['count'])
            page = math.ceil(count / 25)
            now_page = re.findall('page=(\d+)', response.url)[0]
            next_page = int(now_page) + 1
            if len(res['pois']) == 25:
                    yield item
                # for i in range(2,page+1):
                    print('有下一页需要把第{}页存入进去'.format(next_page))
                    url = (response.url).replace('page={}'.format(now_page), 'page={}'.format(next_page))
                    # print('下一页URL：{}'.format(url))
                    # db.add_value(self.redis_key, url)
                    yield Request(url=url, callback=self.parse)
            # if len(item['pois']) > 23:
            #     for i in range(2, maxPage):
            #         logger.info('存入下一页的URL到Redis里面')
            #         url = (response.url).replace('page={}'.format(now_page), 'page={}'.format(i))
            #         db.add_value(self.redis_key, url)
            elif len(res['pois']) > 0:
                item['pois'] = res['pois']
                yield item
            elif len(res['pois']) == 0:
                 print('当前没有数据，不可用URL：{}'.format(response.url))
                 # db.add_value('NotGaoDePoiByCity:start_urls', response.url)
            elif page - now_page < 0 and page != 0 :
                 print('出现异常内容：{}'.format(response.text))
                 db.add_value('ExGaoDePoiByCity:start_urls', response.url)

            else:
                print('当前URL出现严重Bug,内容：{}'.format(response.text))
                db.add_value('BugGaoDePoiByCity:start_urls', response.url)
        elif res['status'] == '0':
            print('请求失败，重新入队列')
            db.add_value(self.redis_key, response.url)
        else:
            print('当前URL出现严重Bug,内容：{}'.format(response.text))
            db.add_value('BugGaoDePoiByCity:start_urls', response.url)
