# -*- coding: utf-8 -*-
import json

import scrapy


class ShopSpider(scrapy.Spider):
    name = 'Shop'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/shop/74834891']

    def parse(self, response):
        print(response)
        html = response.text
        print(html)
        mes = html.split('window.shop_config=')[-1]
        me = mes.split(r'</script> <script src')[0]
        print(me.strip())
        dict = eval(me.strip())
        print(type(dict))
        print(dict)
        print('结束了')
