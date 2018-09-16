# -*- coding: utf-8 -*-
import json
import re
import datetime
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider

from tool.handle_redis import RedisClient


class ShopSpider(RedisSpider):
    name = 'Shop'
    # allowed_domains = ['dianping.com']
    redis_key = "NotShop:start_urls"

    start_urls = [
        # 'http://www.dianping.com/shop/112205355',
        'http://www.dianping.com/shop/110294996',
        'http://www.dianping.com/shop/114644795',
        'http://www.dianping.com/shop/114516583'
    ]
    num_key = {'fn-BARz': '0',
               'fn-67H1': '1',
               'fn-mcun': '2',
               'fn-SbXU': '3',
               'fn-xBtZ': '4',
               'fn-kiQs': '5',
               'fn-PV9m': '6',
               'fn-QQA6': '7',
               'fn-YSfV': '8',
               'fn-Gypm': '9',
               'fn-JEFa': '.',
               'fn-JEFb': '-',
               }

    def parse(self, response):
        db = RedisClient()
        item = {}
        html = response.text
        # print(html)
        # print(response.decode('utf-8'))
        if 'verify' in response.url:
            url = response.meta.get('redirect_urls')[0]
            print('出现问题，有验证码，url:{}'.format(response.url))
            print('需要重新入库，重定向之前的URL：{}'.format(url))
            db.add_value(self.redis_key, url)
        if not html:
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            print('需要重新入库')
            db.add_value(self.redis_key, response.url)
        if '页面无法访问' in html or '页面不存在' in html and 'verify' not in response.url:
            print('失效URL：{}'.format(response.url))
            db.add_value('Not:start_urls', response.url)

        if html and 'window.shop_config='  in html and 'verify' not in response.url and r'https://www.abuyun.com' not in html and 'window.shop_config.shopId' not in html:
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
            ad = re.findall('<meta name="location" content="province=(.*?);city=(.*?);">', html, re.S)
            item['url'] = response.url
            item['province'] = ad[0][0]
            item['city'] = ad[0][1]
            now_time = datetime.datetime.now()
            item['now_time'] = str(now_time)[0:-7]
            from xpinyin import Pinyin
            pin = Pinyin()
            item['sheetName'] = pin.get_pinyin(item['province'], '')

        if html and 'window.shop_config.shopId' in html and 'verify' not in response.url and r'https://www.abuyun.com' not in html:
            item['shopId'] = re.findall('shop/(\d+)',response.url)[0]
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
            ad = re.findall('<meta name="location" content="province=(.*?);city=(.*?);">',html,re.S)[0]
            item['province'] = ad[0]
            item['city'] = ad[1]
            from xpinyin import Pinyin
            pin = Pinyin()
            item['sheetName'] = pin.get_pinyin(item['province'], '')
            now_time = datetime.datetime.now()
            item['now_time'] = str(now_time)[0:-7]
        if len(item)>0:
            # print('这是结果：{}'.format(item))
            # print(item)
            yield item


    def str_to_deciphering(self,response,rule1,rule2):
        number_first = response.xpath(rule1).extract_first()
        change_1 = re.sub(r'1<span class',r'<span class="fn-67H1"></span><span class',number_first)
        change_2 = re.sub(r'span>-<span',r'span><span class="fn-JEFb"></span><span',change_1)
        changes = re.sub('\.',r'<span class="fn-JEFa"></span>',change_2)
        html = Selector(text=changes)
        tagert_num = ''
        numbers = html.xpath(rule2).extract()
        if numbers:
            if 'info-name' in numbers:
                numbers.remove('info-name')
            if numbers:
                for number in numbers:
                    # print(self.num_key.get(number))
                    tagert_num += self.num_key.get(number)
            if len(tagert_num)>18:
                tagert_num = tagert_num[0:12]+"     "+tagert_num[12:]
        else:
            tagert_num = ''
        return  tagert_num


    def str_to_dict(self,start_str):
        result = re.sub('map.*?},', '', start_str)
        pattern = re.compile(r'(\w+):')
        key_list = re.findall(pattern, result)
        if 'http' in key_list:
            key_list.remove('http')
        if 'https' in key_list:
            key_list.remove('https')
        for key in key_list:
            result = result.replace(key, '"{}"'.format(key))
        return  result
