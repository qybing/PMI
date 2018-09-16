# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SupermarketItem(scrapy.Item):
    # define the fields for your item here like:
    # name =scrapy.Field()                 #     scrapy.Field()
    shopId = scrapy.Field()             # 商品ID
    shopName = scrapy.Field()           # 商品名字
    address = scrapy.Field()            # 商铺地址
    fullName = scrapy.Field()           # 商铺全名
    shopGlat = scrapy.Field()           # 商铺经度
    shopGlng = scrapy.Field()           # 商铺纬度
    commentCount = scrapy.Field()       # 评论总数
    rankStars = scrapy.Field()          # 商铺星级
    avgPrice = scrapy.Field()           # 人均消费
    productScore = scrapy.Field()       # 商铺产品评分
    environmentScore = scrapy.Field()   # 商铺环境评分
    serviceScore = scrapy.Field()       # 商铺服务评分
    telephone = scrapy.Field()          # 商铺电话
    shopHours = scrapy.Field()          # 营业时间
    province = scrapy.Field()           #省份
    city = scrapy.Field()               #市县区
    sheetName = scrapy.Field()          #表名字
    now_time = scrapy.Field()           #当前时间

    pass
