# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class VillageSpider(RedisSpider):
    name = 'village'
    allowed_domains = ['dianping.com']
    start_urls = ['http://dianping.com/']
    redis_key = "village:start_urls"

    def parse(self, response):
        html = response.text
        db = RedisClient()
        if 'verify' not in response.url and len(html) > 550 and r'https://www.abuyun.com' not in html:
            trade_areas = response.xpath('//*[@id="bussi-nav-sub"]/a/@href').extract()
            if trade_areas:
                for trade_area in trade_areas[1:]:
                    db.add_value('ShopList:start_urls', trade_area)
                print(trade_areas)
                print('以商圈地点为单位当前URL：{}'.format(response.url))
                print('一共有{}商圈地点入库'.format(len(trade_areas[1:])))
            else:
                print('以商圈为单位当前URL：{}'.format(response.url))
                print('该商圈没有商圈地点，存入本商圈ULR：{}'.format(response.url))
                db.add_value('ShopList:start_urls', response.url)
        elif len(html) < 550 and 'verify' not in response.url:
            print('遇到反爬了，该URL：{}需要重新入队列'.format(response.url))
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            print('需要重新入库')
            db.add_value(self.redis_key, response.url)
        elif 'verify' in response.url:
            url = response.meta.get('redirect_urls')[0]
            print('出现问题，有验证码，url:{}'.format(response.url))
            print('需要重新入库，重定向之前的URL：{}'.format(url))
            db.add_value(self.redis_key, url)
        else:
            print('当前URL：{}'.format(response.url))
            print('这是个严重错误，请查看详情:{}   该网页内容：{}'.format(response.url, html))
