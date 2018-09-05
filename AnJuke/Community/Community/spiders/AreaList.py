# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class ArealistSpider(RedisSpider):
    name = 'AreaList'
    # allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "AreaList:start_urls"

    def parse(self, response):
        html = response.text
        db = RedisClient()
        if 'verify' in response.url or 'params' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            url = response.meta.get('redirect_urls')[0]
            db.add_value(self.redis_key, url)
        elif r'abuyun.com' not in html and len(html) > 600:
            count = response.xpath('//span[@class="tit"]/em[2]/text()').extract_first()
            print('一共有{}个'.format(count))
            if int(count) < 1500 and int(count) != 0:
                print('直接把URL存到list列表中')
                db.add_value('HouseList:start_urls',response.url)
            elif int(count)==0:
                print('该URL：{}没有小区信息'.format(response.url))
                db.add_value('NotAreaList:start_urls',response.url)
            else:
                print('继续细分到区')
                areas = response.xpath('//div[@class="div-border items-list"]/div[1]/span[2]/a/@href').extract()[1:]
                for area in areas:
                    db.add_value('AddressList:start_urls', area)
                if len(areas)==0:
                    print('这是个不正常的URL：{}'.format(response.url))
                    db.add_value('NotAreaList:start_urls',response.url)
                print(areas)
                print('该URL：{}一共有{}个地区'.format(response.url,len(areas)))
        elif r'abuyun.com' in html:
            print('IP出问题了，该URL：{}需要重新入队列'.format(response.url))
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            db.add_value(self.redis_key, response.url)
        else:
            print('当前URL：{}'.format(response.url))
            print('这是个严重错误，请查看详情:{}   该网页内容：{}'.format(response.url, html))