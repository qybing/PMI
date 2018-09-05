# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class TradeareaSpider(RedisSpider):
    name = 'TradeArea'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/luliang/ch20/g187']
    redis_key = "TradeArea:start_urls"

    def parse(self, response):
        html = response.text
        db = RedisClient()
        if 'verify' not in response.url and len(html) > 400 and r'https://www.abuyun.com' not in html:
            trade_areas = response.xpath('//*[@id="bussi-nav"]/a/@href').extract()
            if trade_areas:
                for trade_area in trade_areas:
                    db.add_value('village:start_urls', trade_area)
                print(trade_areas)
                print('以商圈为单位当前URL：{}'.format(response.url))
                print('一共有{}商圈入库'.format(len(trade_areas)))
            else:
                adms = response.xpath('//*[@id="region-nav"]/a/@href').extract()
                for adm in adms:
                    db.add_value('gov:start_urls', adm)
                print('没有商圈选项,以行政区为单位')
                print('以行政区为单位当前URL：{}'.format(response.url))
                print(adms)
                print('一共有{}个行政单位入库'.format(len(adms)))
        elif len(html) < 400 and 'verify' not in response.url:
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
