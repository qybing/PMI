# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XzlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     public_time = scrapy.Field()                    # 发布时间
     house_number = scrapy.Field()                   # 房源编号
     describe = scrapy.Field()                       # 房源描述


     url = scrapy.Field()                            # url
     lat_lng = scrapy.Field()                        #经纬度
     total = scrapy.Field()                          # 标题

     daily_hire = scrapy.Field()                     #日租金
     month_hire = scrapy.Field()                     #月租金
     get_house = scrapy.Field()                      #得房率
     house_name = scrapy.Field()                     #楼盘名
     address = scrapy.Field()                        #地址
     subway = scrapy.Field()                         #地铁
     covered_area = scrapy.Field()                   #建筑面积
     floor = scrapy.Field()                          #楼层
     station = scrapy.Field()                        #工位数
     property_management_fee = scrapy.Field()        #物业费
     type = scrapy.Field()                           #类型
     total_floor = scrapy.Field()                    #总楼层
     completion_date = scrapy.Field()                #竣工年月
     lobby_height = scrapy.Field()                   #大堂层高
     air_conditioning_type = scrapy.Field()          #空调类型
     parking_space = scrapy.Field()                  #车位
     every_area = scrapy.Field()                     #单层面积
    # get_house = scrapy.Field()
     property_company = scrapy.Field()               #物业公司
     standard_floor_hegiht = scrapy.Field()          #标准层高
     elevator = scrapy.Field()                       #电梯
     is_foregin = scrapy.Field()                     #是否涉外
     unit_price = scrapy.Field()                     #单价
     total_price = scrapy.Field()                    #总价
     area = scrapy.Field()                           #面积
     province = scrapy.Field()                       #省
     city = scrapy.Field()                           #市
     county = scrapy.Field()                         #区


     sheetname = scrapy.Field()                     #表名字


     estimated_monthly_expenditure = scrapy.Field()   #预估月支出
     # pass
