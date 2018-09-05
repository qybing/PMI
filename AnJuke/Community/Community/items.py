# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommunityItem(scrapy.Item):
    property_type = scrapy.Field()                                  #物业类型
    property_costs = scrapy.Field()                                 #物业费
    total_area = scrapy.Field()                                     #总建面积
    total_houses = scrapy.Field()                                   #总户数
    construction_age = scrapy.Field()                               #建造年代
    park = scrapy.Field()                                           #停车位
    volume_rate = scrapy.Field()                                    #容积率
    greening_rate = scrapy.Field()                                  #绿化率
    developer = scrapy.Field()                                      #开发商
    property_company = scrapy.Field()                               #物业公司
    school = scrapy.Field()                                           #物业公司
    price = scrapy.Field()                                          #价格
    address = scrapy.Field()                                        #地址
    lat_lng = scrapy.Field()                                        #经纬度
    province = scrapy.Field()                                       # 省
    city = scrapy.Field()                                           # 市
    county = scrapy.Field()                                         # 区
    community = scrapy.Field()                                      #小区
    community_name = scrapy.Field()                                     #小楼名
    url = scrapy.Field()                                            #本页URL
    sheet_name = scrapy.Field()                                     #表名