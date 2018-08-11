# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XzlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     public_time = scrapy.Field()  # 发布时间
     house_number = scrapy.Field()  # 房源编号
     describe = scrapy.Field()  # 房源描述


     url = scrapy.Field()  # url
     lat_lng = scrapy.Field()
     total = scrapy.Field()  # 标题

     daily_hire = scrapy.Field()
     month_hire = scrapy.Field()
     get_house = scrapy.Field()
     house_name = scrapy.Field()
     address = scrapy.Field()
     subway = scrapy.Field()
     covered_area = scrapy.Field()
     floor = scrapy.Field()
     station = scrapy.Field()
     property_management_fee = scrapy.Field()
     type = scrapy.Field()
     total_floor = scrapy.Field()
     completion_date = scrapy.Field()
     lobby_height = scrapy.Field()
     air_conditioning_type = scrapy.Field()
     parking_space = scrapy.Field()
     every_area = scrapy.Field()
    # get_house = scrapy.Field()
     property_company = scrapy.Field()
     standard_floor_hegiht = scrapy.Field()
     elevator = scrapy.Field()
     is_foregin = scrapy.Field()
     unit_price = scrapy.Field()
     total_price = scrapy.Field()
     area = scrapy.Field()
     pass
