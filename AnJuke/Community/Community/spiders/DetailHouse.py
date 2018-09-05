# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy_redis.spiders import RedisSpider
from xpinyin import Pinyin

from Community.items import CommunityItem
from tool.get_province import get_key
from tool.handle_redis import RedisClient


class DetailhouseSpider(RedisSpider):
    name = 'DetailHouse'
    # allowed_domains = ['anjuke.com']
    # start_urls = ['https://nanjing.anjuke.com/community/view/346221?from=Filter_1&hfilter=filterlist#']
    redis_key = "DetailHouse:start_urls"

    def parse(self, response):
        db = RedisClient()
        item = CommunityItem()
        html = response.text
        if 'verify' in response.url or 'params' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            url = response.meta.get('redirect_urls')[0]
            db.add_value(self.redis_key, url)
        elif r'abuyun.com' not in html and len(html) > 600 and '您要查看的页面丢失了' not in html:
            from scrapy.conf import settings
            ho = settings['HOUSE']
            try:
                price = re.findall('"comm_midprice":"(.*?)","area_midprice"', html, re.S)[0]
            except:
                price = re.findall('"comm_midprice":(.*?),"area_midprice"', html, re.S)[0]
            print(price)
            # print(price)
            item['price'] = price
            try:
                l2 = re.findall('lat : "(.*?)",.*?lng : "(.*?)"', html, re.S)
                lat_lng = [float(l2[0][0]), float(l2[0][1])]
            except:
                lat_lng=[0,0]
            # print(lat_lng)
            item['lat_lng'] = lat_lng
            detali_dt = response.xpath('//*[@id="basic-infos-box"]/dl/dt')
            address = response.xpath('//span[@class="sub-hd"]/text()').extract_first()
            all_add = response.xpath('//div[@class="p_1180 p_crumbs"]/a/text()').extract()
            city = all_add[1].replace('小区', '')
            county = all_add[2]
            community = all_add[3]
            community_name = all_add[4]
            pin = Pinyin()
            province = self.gen_address(city)
            sheet_name = pin.get_pinyin(province, "").replace('sheng', '').replace('shi', '')
            item['sheet_name'] = sheet_name
            print(province, city, county, community, community_name)
            item['province'] = province
            item['city'] = city
            item['county'] = county
            item['community'] = community
            item['community_name'] = community_name
            # print(address)
            item['address'] = address
            dt = []
            for i in detali_dt:
                key1 = i.xpath('./text()').extract_first().replace('\xa0', '').replace('：', '')
                key = ho.get(key1)
                dt.append(key)
            detali_dd = response.xpath('//*[@id="basic-infos-box"]/dl/dd')
            dd = []
            for i in detali_dd:
                dd.append(i.xpath('./text()').extract_first())
            house_mes = dict(zip(dt, dd))
            item.update(house_mes)
            item['url'] = response.url
            print('这是结果：{}'.format(item))
            yield item
        elif r'abuyun.com' in html:
            print('IP出问题了，该URL：{}需要重新入队列'.format(response.url))
            print('返回状态：{}，返回内容：{}'.format(response.status, html))
            db.add_value(self.redis_key, response.url)
        else:
            print('当前URL：{}'.format(response.url))
            print('这是个严重错误，请查看详情:{}   该网页内容：{}'.format(response.url, html))
    def gen_address(self,every_address):
        province = every_address + '市'
        real_province = get_key(province)
        return real_province