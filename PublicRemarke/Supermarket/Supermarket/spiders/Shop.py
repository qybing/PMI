# -*- coding: utf-8 -*-
import json
import re

import scrapy
from bs4 import BeautifulSoup
from parsel import Selector

from tool.handle_redis import RedisClient


class ShopSpider(scrapy.Spider):
    name = 'Shop'
    allowed_domains = ['dianping.com']
    redis_key = "Shop:start_urls"

    start_urls = [
        'http://www.dianping.com/shop/4088818',
'http://www.dianping.com/shop/3844195',
'http://www.dianping.com/shop/1942801',
'http://www.dianping.com/shop/97795311',
'http://www.dianping.com/shop/1862386',
'http://www.dianping.com/shop/1879867',
'http://www.dianping.com/shop/93363982',
'http://www.dianping.com/shop/13785094',
'http://www.dianping.com/shop/98824311',
'http://www.dianping.com/shop/90500184',
'http://www.dianping.com/shop/4536585',
'http://www.dianping.com/shop/4657753',
'http://www.dianping.com/shop/4224346',
'http://www.dianping.com/shop/3837505',
'http://www.dianping.com/shop/4280140',
    ]
    num_key = {'fn-67HV': '0',
               'fn-67H1': '1',
               'fn-cMXT': '2',
               'fn-6OZv': '3',
               'fn-JG8T': '4',
               'fn-UqkY': '5',
               'fn-QanZ': '6',
               'fn-Kwvz': '7',
               'fn-Lmh3': '8',
               'fn-JEFc': '9',
               'fn-JEFa': '.',
               'fn-JEFb': '-',
               }

    def parse(self, response):
        html = response.text
        db = RedisClient()
        item = {}
        html = response.text
        print(response.status)
        if 'verify' in response.url:
            url = response.meta.get('redirect_urls')[0]
            print('出现问题，有验证码，url:{}'.format(response.url))
            print('需要重新入库，重定向之前的URL：{}'.format(url))
            db.add_value('Shop:start_urls', url)
        if not html:
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            print('需要重新入库')
            db.add_value('Shop:start_urls', response.url)
        if '抱歉！页面无法访问' in html:
            print('失效URL：{}'.format(response.url))
            db.add_value('NotShop:start_urls', url)

        if html and 'window.shop_config.shopId' not in html:
            mes = html.split('window.shop_config=')[-1]
            me = mes.split(r'</script> <script src')[0]
            result = self.str_to_dict(me.strip())
            dict = json.loads(result)
            item['shopId'] = dict.get('shopId')
            item['shopName'] = dict.get('shopName')
            item['address'] = dict.get('address')
            item['fullName'] = dict.get('fullName')
            item['shopGlat'] = dict.get('shopGlat')
            item['shopGlng'] = dict.get('shopGlng')
            item['reviewCount'] = response.xpath('//*[@id="reviewCount"]/text()').extract_first()
            item['avgPrice'] = self.str_to_deciphering(response,'//*[@id="avgPriceTitle"]','//*[@id="avgPriceTitle"]/span/@class')
            item['productScore'] = self.str_to_deciphering(response,'//*[@id="comment_score"]/span[1]','//span[@class="item"]/span/@class')
            item['environmentScore'] = self.str_to_deciphering(response,'//*[@id="comment_score"]/span[2]','//span[@class="item"]/span/@class')
            item['serviceScore'] = self.str_to_deciphering(response,'//*[@id="comment_score"]/span[3]','//span[@class="item"]/span/@class')
            item['telephone'] = self.str_to_deciphering(response,'//*[@id="basic-info"]/p[1]','//p/span/@class')
            rank = response.xpath('//*[@id="basic-info"]/div[1]/span[1]/@class').extract_first()
            rank_handle = re.findall('\d+', rank)
            rankStars = ''.join(rank_handle) if rank_handle else 0
            item['rankStars'] = rankStars
            shop_hours = response.xpath(
                '//p[@class="info info-indent"]/span[2]/text()').extract()
            item['shopHours'] = shop_hours
            item['url'] = response.url
            print(item)
        else:
            item['shopId'] = response.url
            item['shopName'] = response.xpath('//*[@id="basic-info"]/h1/text()').extract_first().strip()
            item['address'] = response.xpath('string(//*[@id="basic-info"]/div[2])').extract_first().strip()
            item['fullName'] = response.xpath('//*[@id="basic-info"]/h1/text()').extract_first().strip()
            ll = re.findall(r'{(lng:.*?)}', html)[0]
            ll = re.split(r'[:,]', ll)
            item['shopGlng'] = float(ll[1])
            item['shopGlat'] = float(ll[-1])
            # item['shopGlat'] = response.xpath('//*[@id="basic-info"]/h1/text()').extract_first().strip()
            # item['shopGlng'] = response.xpath('//*[@id="basic-info"]/h1/text()').extract_first().strip()
            item['reviewCount'] = response.xpath('//*[@id="basic-info"]/div[1]/span[2]/text()').extract_first()
            item['avgPrice'] = response.xpath('//*[@id="basic-info"]/div[1]/span[3]/text()').extract_first()
            item['productScore'] = response.xpath('//*[@id="basic-info"]/div[1]/span[4]/text()').extract_first()
            item['environmentScore'] = response.xpath('//*[@id="basic-info"]/div[1]/span[5]/text()').extract_first()
            item['serviceScore'] = response.xpath('//*[@id="basic-info"]/div[1]/span[6]/text()').extract_first()
            item['telephone'] = response.xpath('//*[@id="basic-info"]/p/span[2]/text()').extract_first()
            rank = response.xpath('//*[@id="basic-info"]/div[1]/span[1]/@class').extract_first()
            rank_handle = re.findall('\d+', rank)
            rankStars = ''.join(rank_handle) if rank_handle else 0
            shop_hours = response.xpath(
                '//p[@class="info info-indent"]/span[2]/text()').extract()
            item['shopHours'] = shop_hours if shop_hours else ''
            item['rankStars'] = rankStars
            item['url'] = response.url
            print(item)


    def str_to_deciphering(self,response,rule1,rule2):
        number_first = response.xpath(rule1).extract_first()
        change_1 = re.sub('1',r'<span class="fn-67H1"></span>',number_first)
        change_2 = re.sub('span>-<span',r'span><span class="fn-JEFb"></span><span',change_1)
        changes = re.sub('\.',r'<span class="fn-JEFa"></span>',change_2)
        # print(changes)
        html = Selector(text=changes)
        tagert_num = ''
        numbers = html.xpath(rule2).extract()
        if 'info-name' in numbers:
            numbers.remove('info-name')
        if numbers:
            for number in numbers:
                # print(self.num_key.get(number))
                tagert_num += self.num_key.get(number)
        if len(tagert_num)>18:
            tagert_num = tagert_num[0:12]+"     "+tagert_num[12:]
        return  tagert_num


    def str_to_dict(self,start_str):
        result = re.sub('map.*?},', '', start_str)
        pattern = re.compile(r'(\w+):')
        key_list = re.findall(pattern, result)
        key_list.remove('http')
        for key in key_list:
            result = result.replace(key, '"{}"'.format(key))
        return  result
