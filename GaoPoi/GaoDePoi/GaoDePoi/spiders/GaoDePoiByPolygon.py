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

logger = logging.getLogger(__name__)

# 获取最小矩形框
from tool.handle_redis import RedisClient


class Rect:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax


class GaodepoibypolygonSpider(RedisSpider):
    name = 'GaoDePoiByPolygon'
    # allowed_domains = ['restapi.amap.com']
    start_urls = [
        'https://restapi.amap.com/v3/place/polygon?offset=25&extensions=base&polygon=71.234018%2C17.725738%7C136.139681%2C55.28893&types=50120&page=1']
    import os
    pwd = os.getcwd()
    codePath2 = os.path.join(pwd, 'GaodeCode_python.xlsx')
    df1 = pd.read_excel(codePath2, sheetname=r'POI分类与编码（中英文）')
    # params = {'offset': 25, 'extensions': 'base'}
    base_url = 'https://restapi.amap.com/v3/place/polygon?'
    redis_key = 'GaoDePoiByPolygon:start_urls'

    # def make_requests_from_url(self, url):
    #     url = parse.unquote(url)
    #     GDkeys = APIkeys.GDkeysList3
    #     GDkeys.extend(APIkeys.GDkeysList)
    #     GDkeys.extend(APIkeys.GDkeysList2)
    #     loc = url.find('&key=')
    #     if loc > 0:
    #         url = url[0:loc]
    #     params = {}
    #     a = '5505395763b84ab30052bde548ef6db2'
    #     # params['key'] = choice(GDkeys)
    #     params['key'] = a
    #     url = url + "&"+urllib.parse.urlencode(params)
    #     return Request(url, dont_filter=True)

    def parse(self, response):
        # self.CutChina(response.url)
        item = GaodepoiItem()
        db = RedisClient()
        result = json.loads(response.text)
        try:
            sum = int(result['count'])
        except:
            sum = 0
        maxPage = math.ceil(sum / 20)
        now_page = re.findall('page=(\d+)', response.url)[0]
        next_page = int(now_page) + 1
        if result['status'] == '1':
            item['pois'] = result['pois']
            if sum > 840:
                logger.info('数量大于850，需要再次切分')
                self.CutChina(response.url)
            elif len(item['pois']) > 0:
                yield item
                if len(item['pois']) == 20:
                    # for i in range(now_page+1,maxPage+1):
                    url = (response.url).replace('page={}'.format(now_page), 'page={}'.format(next_page))
                    logger.info('要访问第{}页了一共有{}页'.format(next_page,maxPage))
                    logger.info('一共有{}条数据'.format(sum))
                    logger.info('下一页URL：{}'.format(url))
                    # db.add_value(self.redis_key,url)
                    yield Request(url=url, callback=self.parse,dont_filter=True)
                if len(item['pois'])>0 and len(item['pois'])<20 and maxPage - int(now_page) != 0:
                    url = (response.url).replace('page={}'.format(now_page), 'page={}'.format(next_page+1))
                    logger.info('要访问第{}页了一共有{}页'.format(next_page+1, maxPage))
                    yield Request(url=url, callback=self.parse,dont_filter=True)
            elif maxPage - int(now_page) < 0 and  len(item['pois']) == 0:
                if maxPage == 0 and int(now_page) == 1:
                    logger.info('第一页就没有结果没有结果的URL：{}'.format(response.url))
                elif now_page - maxPage == 1:
                    logger.info('当前第{}页了一共有{}'.format(now_page, maxPage + 1))
                    logger.info('没有结果的URL：{}'.format(response.url))
                else:
                    logger.warning('当前URL:{},还没取取到最后一页就为0了，重新如队列'.format(response.url))
                    logger.info('把第{}页了URL存入Redis,一共有{}页'.format(now_page, maxPage))
                    db.add_value(self.redis_key, response.url)
            elif sum == 0 and int(now_page) == 1 and len(item['pois']) == 0:
                logger.info('当前第{}页了一共有{}'.format(now_page, maxPage+1))
                logger.info('没有结果的URL：{}'.format(response.url))
            elif sum != 0 and maxPage - int(now_page) == -1 and len(item['pois']) == 0:
                logger.info('当前第{}页了一共有{}'.format(now_page, maxPage))
                logger.info('没有结果的URL：{}'.format(response.url))

            else:
                logger.warning('1-出现严重的异常的URL：{}，内容为：{}'.format(response.url, response.text))
                db.add_value('Exception1:start_urls', response.url)
        elif result['status'] == '0':
            logger.info('请求失败，重新入队列')
            db.add_value(self.redis_key, response.url)
        else:
            logger.warning('2-出现严重的异常的URL：{}，内容为：{}'.format(response.url, response.text))
            db.add_value('Exception2:start_urls', response.url)

    # 切分地块
    def CutChina(self, url):
        url = parse.unquote(url)
        db = RedisClient()
        x = []
        a = re.findall('polygon=(.*?)&', url)[0]
        c = a.split('|')
        for i in c:
            x.extend(i.split(','))
        logger.info('从URL：里面查找出两个点的坐标')
        rect = Rect(xmin=float(x[0]), ymin=float(x[1]), xmax=float(x[2]), ymax=float(x[3]))
        # 规则：经度和纬度用","分割，经度在前，纬度在后，坐标对用"|"分割。经纬度小数点后不得超过6位。
        polygon = "{:.6f},{:.6f}|{:.6f},{:.6f}".format(rect.xmin, rect.ymin, rect.xmax, rect.ymax)
        middleX = (rect.xmin + rect.xmax) / 2
        middleY = (rect.ymin + rect.ymax) / 2
        lng_lat = []
        rect1 = Rect(xmin=rect.xmin, ymin=rect.ymin, xmax=middleX, ymax=middleY)
        polygon1 = "{:.6f},{:.6f}|{:.6f},{:.6f}".format(rect1.xmin, rect1.ymin, rect1.xmax, rect1.ymax)
        lng_lat.append(polygon1)
        rect2 = Rect(xmin=middleX, ymin=rect.ymin, xmax=rect.xmax, ymax=middleY)
        polygon2 = "{:.6f},{:.6f}|{:.6f},{:.6f}".format(rect2.xmin, rect2.ymin, rect2.xmax, rect2.ymax)
        lng_lat.append(polygon2)
        rect3 = Rect(xmin=rect.xmin, ymin=middleY, xmax=middleX, ymax=rect.ymax)
        polygon3 = "{:.6f},{:.6f}|{:.6f},{:.6f}".format(rect3.xmin, rect3.ymin, rect3.xmax, rect3.ymax)
        lng_lat.append(polygon3)
        rect4 = Rect(xmin=middleX, ymin=middleY, xmax=rect.xmax, ymax=rect.ymax)
        polygon4 = "{:.6f},{:.6f}|{:.6f},{:.6f}".format(rect4.xmin, rect4.ymin, rect4.xmax, rect4.ymax)
        lng_lat.append(polygon4)
        count = 0
        for i in lng_lat:
            for type in self.df1['NEW_TYPE']:
                params = {'polygon': i, 'types': type, 'page': '1', 'offset': 20, 'extensions': 'all'}
                real_url = self.base_url + urlencode(params)
                db.add_value(self.redis_key, real_url)
                count += 1
        logger.info('切分的矩形重新放入redis中,一共{}个URL'.format(count))
