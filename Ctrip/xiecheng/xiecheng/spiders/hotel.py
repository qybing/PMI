# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy_redis.spiders import RedisSpider
from w3lib.html import remove_tags
from scrapy.http import Request


class HotelSpider(RedisSpider):
    name = 'hotel'
    # allowed_domains = ['hotels.ctrip.com']
    # start_urls = ['http://hotels.ctrip.com/']
    redis_key = "hotel:start_urls"


    def parse(self, response):
        distance = re.findall("ajaxGetHotelAddtionalInfo:'(.*?),", response.text, re.DOTALL)[0]
        base_url = 'http://hotels.ctrip.com'
        distance_url = base_url + distance
        low_price = response.meta['low_price']
        hotel_id = response.meta['hotel_id']
        html = response
        room = html.xpath('//td[@class="child_name"]').extract()
        name = html.xpath('//*[@id="J_htl_info"]/div[1]/h2[1]/text()').extract_first()
        a = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_imgStar"]/@title').extract_first()
        b = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_imgStar"]/@class').extract_first()
        grade = a+'-'+b
        city = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkCity"]/text()').extract_first()
        area = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkLocation"]/text()').extract_first()
        address = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lbAddress"]/text()').extract_first()
        road_cross = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkRoadCross"]/text()').extract_first()
        area_extra = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkMapZone"]/text()').extract_first()
        phone = html.xpath('//*[@id="J_realContact"]/@data-real').extract_first()
        rating = html.xpath('//div[@class="htl_com_box basefix"]/a/p[1]/span/text()').extract_first()
        recommend = html.xpath('//div[@class="htl_com_box basefix"]/a/p[2]/text()').extract_first()
        reviews = html.xpath('//div[@class="htl_com_box basefix"]/a/span/span/text()').extract_first()
        lat = html.xpath('//*[@id="aspnetForm"]/div[6]/meta[1]/@content').extract_first()
        lng = html.xpath('//*[@id="aspnetForm"]/div[6]/meta[2]/@content').extract_first()
        description = remove_tags(str(html.xpath('//*[@id="htlDes"]').extract_first()))
        main_photo = html.xpath('//*[@id="topPicList"]/meta/@content').extract_first()
        photo = html.xpath('//*[@id="topPicList"]/div/div/@_src').extract()
        hotel_amenities = remove_tags(str(html.xpath('//*[@id="J_htl_facilities"]').extract_first()))
        hotel_policy = remove_tags(str(html.xpath('//*[@id="hotel_info_comment"]/div/div[7]').extract_first()))
        nearby_amenities = remove_tags(str(html.xpath('//*[@id="hotel_info_comment"]/div/div[8]').extract_first()))
        traffic = remove_tags(str(html.xpath('//div[@class="traffic_side"]/div[@class="traffic_box"]/div').extract_first()))
        v = html.xpath('//*[@id="topPicList"]/meta/@content').extract_first()
        yield Request(url=distance_url, callback=self.parse,meta=traffic)

        print(city)

