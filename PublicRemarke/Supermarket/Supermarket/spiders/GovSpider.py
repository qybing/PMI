# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class GovspiderSpider(RedisSpider):
    name = 'GovSpider'
    allowed_domains = ['dianping.com']
    start_urls = ['http://dianping.com/']
    redis_key = "GovSpider:start_urls"


    def parse(self, response):
        html = response.text
        db = RedisClient()
        if 'verify' not in response.url and len(html) > 700 and r'https://www.abuyun.com' not in html:
            is_50 = response.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/a[10]/text()').extract_first()
            try:
                page = int(is_50) if is_50 else int(1)
            except Exception as e:
                print('查找页数失败，失败原因：{},可能原因{}'.format(e.args, is_50))
                page = 1
            if int(page)==50:
                print('该地区已经满50页需要在划分')
                areas = response.xpath('//*[@id="region-nav-sub"]/a/@href').extract()
                if areas:
                    for area in areas:
                        db.add_value('village:start_urls', area)
                    print(areas)
                    print('一共有{}个详细地点入库'.format(len(areas)))
                else:
                    print('该URL：{}出现异常,该网页内容为：{}'.format(response.url, html))
                    db.add_value('ExGovSpider:start_urls',response.url)
            else:
                print('该地区页数不满50页，一共有{}页,直接将本页存入本URL：{}'.format(page,response.url))
                db.add_value('ShopList:start_urls',response.url)
        elif len(html) < 700 and 'verify' not in response.url:
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

