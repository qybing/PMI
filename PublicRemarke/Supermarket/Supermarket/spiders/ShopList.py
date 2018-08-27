# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from tool.handle_redis import RedisClient


class ShoplistSpider(scrapy.Spider):
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
            db.add_value('ShopList:start_urls', url)
        elif len(html)<50 and 'verify' not in response.url:
            print('遇到反爬了，该URL：{}需要重新入队列'.format(response.url))
            db.add_value('ShopList:start_urls', response.url)
        elif 'verify' not in response.url and len(html)>100:
            shops_url = response.xpath('//*[@id="shop-all-list"]/ul/li/div[1]/a/@href').extract()
            if shops_url:
                for shop_url in shops_url:
                    db.add_value('Shop:start_urls', shop_url)
                print(shops_url)
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
                print('该URL：{}已经无商铺列表可选'.format(response.url))
        # elif '没有找到符合条件的商户' in html:
        #     print('该URL：{}无效'.format(response.url))
