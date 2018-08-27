# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class TradeareaSpider(RedisSpider):
    name = 'TradeArea'
    allowed_domains = [' ']
    start_urls = ['http://www.dianping.com/luliang/ch20/g187']
    redis_key = "TradeArea:start_urls"

    def parse(self, response):
        html = response.text
        db = RedisClient()
        if 'verify' not in response.url and len(html) > 100:
            trade_areas = response.xpath('//*[@id="bussi-nav"]/a/@href').extract()
            if trade_areas:
                for trade_area in trade_areas:
                    db.add_value('village:start_urls', trade_area)
                print(trade_areas)
                print('一共有{}商圈入库'.format(len(trade_areas)))
            else:
                print('没有商圈选项,以行政区为单位')
                adms = response.xpath('//*[@id="region-nav"]/a/@href').extract()
                for adm in adms:
                    db.add_value('gov:start_urls', adm)
                print(adms)
                print('一共有{}行政单位入库'.format(len(trade_areas)))
        elif len(html) < 50 and 'verify' not in response.url:
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            print('需要重新入库')
            db.add_value('TradeArea:start_urls', response.url)
        elif 'verify' in response.url:
            url = response.meta.get('redirect_urls')[0]
            print('出现问题，有验证码，url:{}'.format(response.url))
            print('需要重新入库，重定向之前的URL：{}'.format(url))
            db.add_value('TradeArea:start_urls', url)
        else:
            print('出现问题，请查看详情:{}   该网页内容：{}'.format(response.url, html))
