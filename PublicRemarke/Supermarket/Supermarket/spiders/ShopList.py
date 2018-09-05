# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class ShoplistSpider(RedisSpider):
    name = 'ShopList'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/shanghai/ch20/g187r812']
    redis_key = "ShopList:start_urls"

    def parse(self, response):
        html = response.text
        db = RedisClient()
        if 'verify' in response.url:
            print('出现验证码，该url重新入队列')
            url = response.meta.get('redirect_urls')[0]
            db.add_value(self.redis_key, url)
        elif len(html) < 700 and 'verify' not in response.url:
            print('遇到反爬了，该URL：{}需要重新入队列'.format(response.url))
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            db.add_value(self.redis_key, response.url)
        elif 'verify' not in response.url and len(html) > 700 and r'https://www.abuyun.com' not in html:
            shops_url = response.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a/@href').extract()
            if shops_url:
                for shop_url in shops_url:
                    db.add_value('Shop:start_urls', shop_url)
                print(shops_url)
                print('当前URL：{}'.format(response.url))
                print('一共有{}商铺详情URL入库'.format(len(shops_url)))
                next_page = response.xpath('//a[@class="next"]/@href').extract_first()
                if next_page:
                    try:
                        page = re.search(r'p(\d+)', next_page)
                        print('第{}页---网址为：{}'.format(page.group(1), next_page))
                    except Exception as e:
                        print('出错原因：{}'.format(e.args))
                    yield Request(url=next_page, callback=self.parse)
            else:
                if '没有找到符合条件的商户' in html:
                    print('该URL：{}已经无商铺列表可选'.format(response.url))
                    print('shops_url:{}'.format(shops_url))
                else:
                    print('IP可能出现异常，检查原因，内容为{}'.format(html))
                    print('URL:{}需要重新入库'.format(response.url))
                    db.add_value(self.redis_key, response.url)
        else:
            print('当前URL：{}'.format(response.url))
            print('这是个严重错误，请查看详情:{}   该网页内容：{}'.format(response.url, html))
