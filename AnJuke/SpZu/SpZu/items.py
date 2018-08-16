# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpzuItem(scrapy.Item):
    # define the fields for your item here like:
    # name  =  scrapy.Field
    url  =  scrapy.Field()                #url
    lat_lng  =  scrapy.Field()       # 经纬度
    real_house_facilities  =  scrapy.Field() # 房屋设置
    # total_price  =  scrapy.Field()        # 总价
    # unit_price  =  scrapy.Field()         # 单价
    # monthly_rent  =  scrapy.Field()       # 月租
    # transfer_fee  =  scrapy.Field()       # 转让费
    # expected_rental_income  =  scrapy.Field() # 预期租金收益
    total  =  scrapy.Field()              # 标题
    # property_costs  =  scrapy.Field()     # 物业费
    # area  =  scrapy.Field()               # 面积
    # face_width  =  scrapy.Field()         # 面宽
    # layer_height  =  scrapy.Field()       # 层高
    # floor  =  scrapy.Field()              # 楼层
    # depth  =  scrapy.Field()              # 进深
    # status  =  scrapy.Field()             # 状态
    # lease_period  =  scrapy.Field()       # 起租期
    # crowd  =  scrapy.Field()              # 人群
    # pay  =  scrapy.Field()                # 押付
    # rent_free_period   =  scrapy.Field()  # 免租期
    # address  =  scrapy.Field()            # 地址
    # is_face_street  =  scrapy.Field()     # 是否临街
    public_time  =  scrapy.Field()        # 发布时间
    house_number  =  scrapy.Field()    # 房源编号
    describe  =  scrapy.Field()# 房源描述
    # shop_name  =  scrapy.Field()          # 商铺名字
    # developer  =  scrapy.Field()          # 开发商
    # property_company  =  scrapy.Field()   # 物业公司
    # property_costs  =  scrapy.Field()     # 物业费
    # unified_management  =  scrapy.Field() # 统一管理
    # completion_time  =  scrapy.Field()    # 竣工时间
    # total_floor  =  scrapy.Field()        # 总楼层
    # total_area   =  scrapy.Field()        # 总面积

    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    expected_rental_income = scrapy.Field()
    monthly_rent = scrapy.Field()
    transfer_fee = scrapy.Field()
    property_management_fee = scrapy.Field()
    area = scrapy.Field()
    face_width = scrapy.Field()
    layer_height = scrapy.Field()
    depth = scrapy.Field()
    floor = scrapy.Field()
    status = scrapy.Field()
    lease_period = scrapy.Field()
    crowd = scrapy.Field()
    pay = scrapy.Field()
    rent_free_period = scrapy.Field()
    address = scrapy.Field()
    is_face_street = scrapy.Field()
    shop_name = scrapy.Field()
    developer = scrapy.Field()
    property_company = scrapy.Field()
    unified_management = scrapy.Field()
    completion_time = scrapy.Field()
    total_floor = scrapy.Field()
    total_area = scrapy.Field()
    province = scrapy.Field()  # 省份
    city = scrapy.Field()  # 城市
    county = scrapy.Field()  # 区
    sheetname = scrapy.Field()  # 表名字

    pass
