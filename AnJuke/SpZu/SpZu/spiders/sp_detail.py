# -*- coding: utf-8 -*-
import re
from time import sleep

import redis
import scrapy
from parsel import Selector
from scrapy.conf import settings
from scrapy_redis.spiders import RedisSpider
from w3lib.html import remove_tags
from xpinyin import Pinyin

from SpZu.items import SpzuItem


# class SpDetailSpider(scrapy.Spider):
from tools.get_province import get_key
from tools.handle_redis import RedisClient


class SpDetailSpider(RedisSpider):
    name = 'sp_detail'
    allowed_domains = ['anjuke.comm']
    start_urls = ['https://sh.sp.anjuke.com/zu/59378052/?pt=2',
                  'https://sh.sp.anjuke.com/zu/59483743/?pt=2',
                  'https://sh.sp.anjuke.com/shou/59536706/?pt=2']
    redis_key = "sp_detail:start_urls"
    # allowed_domains = ['anjuke.com']

    # start_urls = ['https://sh.sp.anjuke.com/zu/58513492/']
    # pool = redis.ConnectionPool(host='localhost', port=6379,db=1, decode_responses=True)
    # r = redis.Redis(connection_pool=pool)

    # custom_settings = {
    #     # 指定redis数据库的连接参数
    #     'REDIS_HOST': '127.0.0.1',
    #     'REDIS_PORT': 6379,
    #
    #     # 指定 redis链接密码，和使用哪一个数据库
    #     'REDIS_PARAMS': {
    #         # 'password': '',
    #         'db': 1
    #     },
    # }

    # sp_house_config = {
    #     '总价': 'total_price',
    #     '单价': 'unit_price',
    #     '预期租金收益': 'expected_rental_income',
    #     '月租': 'monthly_rent',
    #     '转让费': 'transfer_fee',
    #     '物业费': 'property_management_fee',
    #     '面积': 'area',
    #     '面宽': 'face_width',
    #     '层高': 'layer_height',
    #     '进深': 'depth',
    #     '楼层': 'floor',
    #     '状态': 'status',
    #     '起租期': 'lease_period',
    #     '人群': 'crowd',
    #     '押付': 'pay',
    #     '免租期': 'rent_free_period',
    #     '地址': 'address',
    #     '是否临街': 'is_face_street',
    #     '商铺名字': 'shop_name',
    #     '开发商': 'developer',
    #     '物业公司': 'property_company',
    #     '统一管理': 'unified_management',
    #     '竣工时间': 'completion_time',
    #     '总楼层': 'total_floor',
    #     '总面积': 'total_area',
    # }

    def parse(self, response):
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            # r = redis.Redis(connection_pool=pool)
            db = RedisClient()
            urls = response.meta.get('redirect_urls')
            for url in urls:
                db.add_value('sp_detail:start_urls', url)
        else:
            detail_urls_content = response.text
            item = SpzuItem()
            lat_lng = re.findall(r'lat: "(.*?)",.*?lng: "(.*?)"', detail_urls_content, re.S)
            real_lat_lng = lat_lng[0]
            item['url'] = response.url
            xpath_css = Selector(text=detail_urls_content)
            every_address = [str(ad).replace('商铺出租', '').replace('房产网', '').replace('商铺出售', '') for ad in
                             xpath_css.xpath('/html/body/div[2]/a/text()').extract()[1:3]]
            new_address = self.gen_address(every_address)
            print(new_address)
            item['province'], item['city'], item['county'] = new_address[0], new_address[1], new_address[2]
            pin = Pinyin()
            item['sheetname'] = pin.get_pinyin(item['province'], "").replace('sheng', '').replace('shi', '')
            item['total'] = xpath_css.xpath('//*[@id="content"]/div/h1/text()').extract_first()
            house_facilities = xpath_css.xpath('//ul[@class="mod-peitao clearfix"]/li[not(contains(@class,"gray"))]')
            real_house_facilities = []
            for rs in house_facilities:
                one = rs.xpath('./p/text()').extract_first()
                real_house_facilities.append(one)
            item['real_house_facilities'] = real_house_facilities
            new_house = settings['NEWHOUSE']
            sp_houses = xpath_css.xpath('//*[@id="fy_info"]/ul/li')
            for house_msg in sp_houses:
                key1 = house_msg.xpath('./span[1]/text()').extract_first()
                key = new_house.get(house_msg.xpath('./span[1]/text()').extract_first().replace('：', ''))
                item[key] = remove_tags(
                    str(house_msg.xpath('./span[2]').extract_first()).replace('\n', '').replace(' ', ''))

            house_resources_l = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="litem"]/li')
            for house_resource in house_resources_l:
                key1 = house_resource.xpath('./span[1]/text()').extract_first()
                key = new_house.get(
                    house_resource.xpath('./span[1]/text()').extract_first().replace('：', ''))
                item[key] = remove_tags(
                    str(house_resource.xpath('./span[2]').extract_first()).replace('\n', '').replace(' ', ''))
            house_resources_r = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li')
            for house_resource in house_resources_r:
                key1 = house_resource.xpath('./span[1]/text()').extract_first()
                key = new_house.get(
                    house_resource.xpath('./span[1]/text()').extract_first().replace('：', ''))
                item[key] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
            # house_msgs_r = xpath_css.xpath('//*[@id="fy_info"]/ul[@class="ritem"]/li')
            # for house_msg in house_msgs_r:
            #     key1 = house_msg.xpath('./span[1]/text()').extract_first()
            #     key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
            #     if key1 == '预估月支出' and 'zu' in url:
            #         continue
            #     else:
            #         sp_item[key1] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()))
            # house_resources_l = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="litem"]/li')
            # for house_resource in house_resources_l:
            #     key1 = house_resource.xpath('./span[1]/text()').extract_first()
            #     key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
            #     sp_item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
            # house_resources_r = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li')
            # for house_resource in house_resources_r:
            #     key1 = house_resource.xpath('./span[1]/text()').extract_first()
            #     key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
            #     if key1 == '得房率':
            #         continue
            #     else:
            #         sp_item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
            describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract_first()
            real_describe = remove_tags(str(describes))
            item['describe'] = real_describe.strip()
            shop_name = xpath_css.xpath('//div[@class="item-mod"]/h3/b/text()').extract_first().strip()
            item['shop_name'] = shop_name
            print(real_house_facilities)
            item['lat_lng'] = real_lat_lng
            public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
            item['public_time'] = public_time
            house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
            item['house_number'] = house_number
            # item['real_house_facilities'] = real_house_facilities
            # # print(real_house_facilities)
            # item['total_price'] = ''
            # item['unit_price'] = ''
            # item['monthly_rent'] = ''
            # item['transfer_fee'] = ''
            # item['expected_rental_income'] = ''
            # item['total'] = xpath_css.xpath('//*[@id="content"]/div/h1/text()').extract_first().strip()
            # item['property_costs'] = xpath_css.xpath(
            #     '//*[@id="fy_info"]/ul/li[3]/span[2]/text()').extract_first().strip()
            # item['area'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[4]/span[2]/text()').extract_first().strip()
            # item['face_width'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[5]/span[2]/text()').extract_first().strip()
            # item['layer_height'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[6]/span[2]/text()').extract_first().strip()
            # if 'zu' in response.url:
            #     item['floor'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[8]/span[2]/text()').extract_first().strip()
            #     if '层' not in item['floor']:
            #         item['floor'] = xpath_css.xpath(
            #             '//*[@id="fy_info"]/ul/li[7]/span[2]/text()').extract_first().strip()
            #     item['depth'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[7]/span[2]/text()').extract_first().strip()
            #     if 'm' not in item['depth']:
            #         item['depth'] = ''
            #     item['monthly_rent'] = xpath_css.xpath(
            #         '//*[@id="fy_info"]/ul/li[1]/span[2]/text()').extract_first().strip()
            #     item['transfer_fee'] = xpath_css.xpath(
            #         '//*[@id="fy_info"]/ul/li[2]/span[2]/text()').extract_first().strip()
            #     item['status'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[9]/span[2]/text()').extract_first().strip()
            #     item['lease_period'] = xpath_css.xpath(
            #         '//*[@id="fy_info"]/ul/li[10]/span[2]/text()').extract_first().strip()
            #     item['crowd'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[11]/span[2]/text()').extract_first().replace(
            #         r'\n',
            #         '').strip()
            #     item['pay'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[12]/span[2]/text()').extract_first()
            #     item['rent_free_period'] = xpath_css.xpath(
            #         '//*[@id="fy_info"]/ul/li[14]/span[2]/text()').extract_first()
            #     item['address'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[13]/span[2]/@title').extract_first()
            #     is_street = xpath_css.xpath('//*[@id="fy_info"]/ul/li[15]/span[2]/text()').extract_first()
            #     if is_street:
            #         item['is_face_street'] = is_street.strip()
            #     else:
            #         try:
            #             item['is_face_street'] = xpath_css.xpath(
            #                 '//*[@id="fy_info"]/ul/li[14]/span[2]/text()').extract_first().strip()
            #         except:
            #             item['is_face_street'] = xpath_css.xpath(
            #                 '//*[@id="fy_info"]/ul/li[13]/span[2]/text()').extract_first()
            #
            # else:
            #     item['floor'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[7]/span[2]/text()').extract_first().strip()
            #     item['depth'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[8]/span[2]/text()').extract_first().strip()
            #     item['total_price'] = xpath_css.xpath(
            #         '//*[@id="fy_info"]/ul/li[1]/span[2]/text()').extract_first().strip()
            #     item['unit_price'] = xpath_css.xpath(
            #         '//*[@id="fy_info"]/ul/li[2]/span[2]/text()').extract_first().strip()
            #     item['status'] = ''
            #     item['lease_period'] = ''
            #     item['crowd'] = xpath_css.xpath('//*[@id="fy_info"]/ul/li[9]/span[2]/text()').extract_first().replace(
            #         r'\n',
            #         '').strip()
            #     item['pay'] = ''
            #     item['rent_free_period'] = ''
            #     item['address'] = xpath_css.xpath('//span[@class="desc addresscommu"]/@title').extract_first()
            #     item['expected_rental_income'] = xpath_css.xpath(
            #         '//*[@id="fy_info"]/ul/li[11]/span[2]/text()').extract_first()
            #     try:
            #         item['is_face_street'] = xpath_css.xpath(
            #             '//*[@id="fy_info"]/ul/li[13]/span[2]/text()').extract_first().strip()
            #     except:
            #         item['is_face_street'] = xpath_css.xpath(
            #             '//*[@id="fy_info"]/ul/li[12]/span[2]/text()').extract_first()
            # item['public_time'] = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root.strip()
            # item['property_number'] = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root.strip()
            # describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract()
            # item['listing_description'] = remove_tags(str(describes))
            #
            # item['shop_name'] = xpath_css.xpath('//div[@class="item-mod"]/h3/b/text()').extract_first().strip()
            # item['developer'] = xpath_css.xpath(
            #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[1]/span[2]/text()').extract_first()
            # item['property_company'] = xpath_css.xpath(
            #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[2]/span[2]/text()').extract_first()
            # item['property_costs'] = xpath_css.xpath(
            #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[3]/span[2]/text()').extract_first().replace(
            #     r'\n', '').strip()
            # item['unified_management'] = xpath_css.xpath(
            #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[4]/span[2]/text()').extract_first().replace(
            #     r'\n', '').strip()
            # item['completion_time'] = xpath_css.xpath(
            #     '//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li[1]/span[2]/text()').extract_first()
            # item['total_floor'] = xpath_css.xpath(
            #     '//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li[2]/span[2]/text()').extract_first()
            # item['total_area'] = xpath_css.xpath(
            #     '//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li[3]/span[2]/text()').extract_first()

            # deatil_mss = (total, 月租, 转让费, 总价, 单价, 物业费, 面积, 面宽, 层高, 进深, 楼层, 状态, 起租期, 人群, 押付, 地址,
            #               免租期, 是否临街, 发布时间, 房源编号, 房源描述, 商铺小区名字, 开发商, 物业公司, 物业费, 统一管理, 竣工时间,
            #               总楼层, 总面积)
            #
            # rs = 'total:%s,月租:%s,转让费:%s,总价:%s,单价:%s,物业费:%s,面积:%s,面宽:%s,层高:%s,进深:%s,楼层:%s,状态:%s,起租期:%s,人群:%s ,押付:%s ,地址:%s,免租期:%s,是否临街:%s,发布时间:%s,房源编号:%s ,房源描述:%s ,商铺小区名字:%s,开发商:%s ,物业公司:%s ,物业费:%s,统一管理:%s,竣工时间:%s,总楼层:%s,总面积:%s' % (
            #     deatil_mss)
            yield item

    def gen_address(self,every_address):
        every_address[0] = every_address[0]+'市'
        province = get_key(every_address[0])
        every_address.insert(0,province)
        return every_address