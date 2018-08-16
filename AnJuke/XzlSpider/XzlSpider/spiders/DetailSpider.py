# -*- coding: utf-8 -*-
import logging
import re

import redis
import scrapy
from parsel import Selector
from scrapy.conf import settings
from scrapy_redis.spiders import RedisCrawlSpider
from w3lib.html import remove_tags
from xpinyin import Pinyin

from XzlSpider.items import XzlspiderItem
from tool.get_province import get_key
from tool.handle_redis import RedisClient


# house_config ={
#     '日租金':'daily_hire',
#     '月租金':'month_hire',
#     '得房率':'get_house',
#     '楼盘名':'house_name',
#     '地址':'address',
#     '地铁':'subway',
#     '建筑面积':'covered_area',
#     '楼层':'floor',
#     '工位数':'station',
#     '物业费':'property_management_fee',
#     '类型':'type',
#     '总楼层':'total_floor',
#     '竣工年月':'completion_date',
#     '大堂层高':'lobby_height',
#     '空调类型':'air_conditioning_type',
#     '车位':'parking_space',
#     '单层面积':'every_area',
#     # '得房率':'get_house',
#     '物业公司':'property_company',
#     '标准层高':'standard_floor_hegiht',
#     '电梯':'elevator',
#     '是否涉外':'is_foregin',
#     '单价':'unit_price',
#     '总价':'total_price',
#     '面积':'area',
#     '省份':'province',
#     '市':'city',
#     '县':'county',
# }
logger = logging.getLogger(__name__)

class DetailspiderSpider(scrapy.Spider):
    # class DetailspiderSpider(RedisCrawlSpider):

    name = 'DetailSpider'
    # allowed_domains = ['anjuke.com']
    redis_key = "DetailSpider:start_urls"
    start_urls = ['https://hz.xzl.anjuke.com/shou/59251819/?pt=2']

    def parse(self, response):
        if 'verify' in response.url:
            logger.info('遇到验证码了，url放入待爬队列里面')
            db = RedisClient()
            urls = response.meta.get('redirect_urls')
            for url in urls:
                db.add_value('DetailSpider:start_urls', url)
        else:
            detail_urls_content = response.text
            lat_lng = re.findall(r'lat: "(.*?)",.*?lng: "(.*?)"', detail_urls_content, re.S)
            real_lat_lng = lat_lng[0]
            xpath_css = Selector(text=detail_urls_content)
            item = XzlspiderItem()
            every_address = [str(ad).replace('写字楼出租', '').replace('房产网', '').replace('写字楼出售', '') for ad in
                             xpath_css.xpath('/html/body/div[2]/a/text()').extract()[1:3]]
            new_address = self.gen_address(every_address)
            item['province'], item['city'], item['county'] = new_address[0], new_address[1], new_address[2]
            item['url'] = response.url
            pin = Pinyin()
            item['sheetname'] = pin.get_pinyin(item['province'], "").replace('sheng', '').replace('shi', '')
            item['total'] = xpath_css.xpath('//*[@id="j-triggerlayer"]/text()').extract_first()
            house_msgs_l = xpath_css.xpath('//*[@id="fy_info"]/ul[@class="litem"]/li')
            house_config = settings['NEWHOUSE']
            for house_msg in house_msgs_l:
                key1 = house_msg.xpath('./span[1]/text()').extract_first()
                key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
                item[key] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()))
            house_msgs_r = xpath_css.xpath('//*[@id="fy_info"]/ul[@class="ritem"]/li')
            for house_msg in house_msgs_r:
                key1 = house_msg.xpath('./span[1]/text()').extract_first()
                key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
                if key1 == '预估月支出' and 'zu' in response.url:
                    continue
                else:
                    item[key] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()))
            house_resources_l = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="litem"]/li')
            for house_resource in house_resources_l:
                key1 = house_resource.xpath('./span[1]/text()').extract_first()
                key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
                item[key] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
            house_resources_r = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li')
            for house_resource in house_resources_r:
                key1 = house_resource.xpath('./span[1]/text()').extract_first()
                key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
                if key1 == '得房率':
                    continue
                else:
                    item[key] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
            describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract_first()
            real_describe = remove_tags(str(describes))
            item['describe'] = real_describe.strip()
            item['lat_lng'] = real_lat_lng
            public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
            item['public_time'] = public_time
            house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
            item['house_number'] = house_number
            # logger.info(item)
            yield item

    def gen_address(self, every_address):
        every_address[0] = every_address[0] + '市'
        province = get_key(every_address[0])
        every_address.insert(0, province)
        return every_address
