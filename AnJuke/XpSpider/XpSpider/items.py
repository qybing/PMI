# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XpspiderItem(scrapy.Item):
    # define the fields for your item here like:
    property_name= scrapy.Field()               #楼盘名称
    property_features = scrapy.Field()          #楼盘特点
    reference_unit_price = scrapy.Field()       #参考单价
    property_type = scrapy.Field()              #物业类型
    developer = scrapy.Field()                  #开发商
    regional_location= scrapy.Field()           #区域位置
    property_address= scrapy.Field()            #楼盘地址
    sales_office_phone = scrapy.Field()         #售楼处电话

    minimum_down_payment= scrapy.Field()        #最低首付
    opening_area= scrapy.Field()                #开间面积
    #-------------------------------
    office_area = scrapy.Field()                #办公室面积
    real_estate_type = scrapy.Field()          #楼盘户型
    tenant_group = scrapy.Field()              #招租客群
    near_cbd = scrapy.Field()                  #临近CBD
    contracted_tenant = scrapy.Field()         #已签约租户
    public_decoration =scrapy.Field()          #公共部分精装修
    standard_floor_area =scrapy.Field()        #标准层面积
    office_type = scrapy.Field()               #写字楼类型
    office_level = scrapy.Field()              #写字楼级别
    number_of_planned_households = scrapy.Field() #规划户数
    total_price_of_the_property =scrapy.Field() #楼盘总价
    greening_rate = scrapy.Field()             #绿化率

    building_type = scrapy.Field()  #建筑类型
    monthly_supply = scrapy.Field() #月供

    #----------------------------------
    commercial_area = scrapy.Field()            #商业面积
    total_surface_area = scrapy.Field()         #总建筑面积
    latest_opening= scrapy.Field()              #最新开盘
    delivery_time = scrapy.Field()              #交房时间
    business_mode= scrapy.Field()               #招商业态
    contracted_merchant= scrapy.Field()         #已签约商户
    near_business_district= scrapy.Field()      #临近商圈
    surrounding_crowd = scrapy.Field()          #周边人群
    sales_office_address= scrapy.Field()        #售楼处地址
    presale_permit = scrapy.Field()             #预售许可证
    year_of_property_rights = scrapy.Field()    #产权年限

    type_of_sale = scrapy.Field()               #出售类型
    toom_rate= scrapy.Field()                   #得房率
    total_number_of_sets= scrapy.Field()        #总套数
    floor_condition= scrapy.Field()             #楼层状况
    project_progress = scrapy.Field()           #工程进度
    property_management_fees =scrapy.Field()    #物业管理费
    property_company =scrapy.Field()            #物业公司
    number_of_car=scrapy.Field()                #车位数
    parking_ratio =scrapy.Field()               #车位比
    uniform_management=scrapy.Field()           #是否统一管理
    whether_to_split=scrapy.Field()             #是否分割



    type_of_rental=scrapy.Field()               #出租类型
    rent=scrapy.Field()                         #租金
    include_property_fees =scrapy.Field()       #是否包含物业费
    area_to_be_rented=scrapy.Field()            #待租面积
    number_of_rents_to_be_rented=scrapy.Field() #待租套数

    province = scrapy.Field()                   #省份
    city = scrapy.Field()                       #城市
    county = scrapy.Field()                     #区
    sheetname = scrapy.Field()                  #表名字
    pass
