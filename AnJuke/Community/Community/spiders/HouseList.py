# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class HouselistSpider(RedisSpider):
    name = 'HouseList'
    # allowed_domains = ['anjuke.com']
    # start_urls = ['http://anjuke.com/']
    redis_key = "HouseList:start_urls"

    def parse(self, response):
        html = response.text
        db = RedisClient()
        if 'verify' in response.url or 'params' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            url = response.meta.get('redirect_urls')[0]
            db.add_value(self.redis_key, url)
        elif r'abuyun.com' not in html and len(html) > 600 and '没有找到符合' not in html:
            count = response.xpath('//span[@class="tit"]/em[2]/text()').extract_first()
            count = int(count)
            print('一共有{}个'.format(count))
            if count > 1500 and count < 3000:
                print('当前小区个数大于100页,需要存入每一页的URL地址')
                for i in range(1,int(count/30)+1):
                    db.add_value('dayu:start_urls',response.url+r'/p'+i)
            elif count > 3000:
                print('此URL：{}为特殊URL，需要特殊处理'.format(response.url))
                db.add_value('special:start_urls',response.url)
            elif count > 0 and count < 1500:
                print('采集详情页URL信息')
                houses = response.xpath('//*[@id="list-content"]/div[@class="li-itemmod"]/@link').extract()[1:]
                for house in houses:
                    db.add_value('DetailHouse:start_urls', house+'?from=Filter_1&hfilter=filterlist')
                print(houses)
                if len(houses)==0:
                    print('这是个不正常的URL：{}'.format(response.url))
                    db.add_value('NotHouseList:start_urls',response.url)
                print('该URL：{}一共有{}个房屋'.format(response.url,len(houses)))
                next_page = response.xpath('//a[@class="aNxt"]/@href').extract_first()
                if next_page:
                    try:
                        page = re.search(r'p(\d+)', next_page)
                        print('第{}页---网址为：{}'.format(page.group(1), next_page))
                    except Exception as e:
                        print('出错原因：{}'.format(e.args))
                    yield Request(url=next_page, callback=self.parse)
            else:
                print('当前URL：{}'.format(response.url))
                print('这是个严重错误，请查看详情:{}   该网页内容：{}'.format(response.url, html))
        elif r'abuyun.com' in html:
            print('IP出问题了，该URL：{}需要重新入队列'.format(response.url))
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            db.add_value(self.redis_key, response.url)
        else:
            print('当前URL：{}'.format(response.url))
            print('这是个严重错误，请查看详情:{}   该网页内容：{}'.format(response.url, html))