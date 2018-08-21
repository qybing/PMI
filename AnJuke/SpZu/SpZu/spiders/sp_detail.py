# -*- coding: utf-8 -*-
import logging
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

logger = logging.getLogger(__name__)
class SpDetailSpider(RedisSpider):
    name = 'sp_detail'
    allowed_domains = ['anjuke.comm']
    start_urls = ['https://cd.sp.anjuke.com/shou/59431181/',
                  'https://cq.sp.anjuke.com/shou/57046164/',
                  'https://sh.sp.anjuke.com/shou/59203429/']
    redis_key = "sp_detail:start_urls"

    def parse(self, response):
        db = RedisClient()
        if 'verify' in response.url:
            logger.info('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')[0]
            db.add_value('sp_detail:start_urls', urls)
        else:
            detail_urls_content = response.text
            if '您要查看的页面丢失了' not in response.text:
                try:
                    item = SpzuItem()
                    lat_lng = re.findall(r'lat: "(.*?)",.*?lng: "(.*?)"', detail_urls_content, re.S)
                    real_lat_lng = lat_lng[0]
                    item['url'] = response.url
                    xpath_css = Selector(text=detail_urls_content)
                    every_address = [str(ad).replace('商铺出租', '').replace('房产网', '').replace('商铺出售', '') for ad in
                                     xpath_css.xpath('/html/body/div[2]/a/text()').extract()[1:3]]
                    new_address = self.gen_address(every_address)
                    logger.info(new_address)
                    item['province'], item['city'], item['county'] = new_address[0], new_address[1], new_address[2]
                    pin = Pinyin()
                    item['sheetname'] = pin.get_pinyin(item['province'], "").replace('sheng', '').replace('shi', '')
                    item['total'] = xpath_css.xpath('//*[@id="content"]/div/h1/text()').extract_first().strip()
                    house_facilities = xpath_css.xpath('//ul[@class="mod-peitao clearfix"]/li[not(contains(@class,"gray"))]')
                    real_house_facilities = []
                    for rs in house_facilities:
                        one = rs.xpath('./p/text()').extract_first()
                        real_house_facilities.append(one)
                    item['real_house_facilities'] = real_house_facilities
                    new_house = settings['SP_HOSER']
                    sp_houses = xpath_css.xpath('//*[@id="fy_info"]/ul/li')
                    for house_msg in sp_houses:
                        key1 = house_msg.xpath('./span[1]/text()').extract_first().split('：')[0]
                        print(key1)
                        key = new_house.get(key1)
                        item[key] = remove_tags(
                            str(house_msg.xpath('./span[2]').extract_first()).replace('\n', '').replace(' ', ''))

                    house_resources_l = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="litem"]/li')
                    for house_resource in house_resources_l:
                        key1 = house_resource.xpath('./span[1]/text()').extract_first().split('：')[0]
                        key = new_house.get(key1)
                        item[key] = remove_tags(
                            str(house_resource.xpath('./span[2]').extract_first()).replace('\n', '').replace(' ', ''))
                    house_resources_r = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li')
                    for house_resource in house_resources_r:
                        key1 = house_resource.xpath('./span[1]/text()').extract_first().split('：')[0]
                        key = new_house.get(key1)
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
                    item['describe'] = real_describe.replace('\xa0','').replace('\t','').strip()
                    shop_name = xpath_css.xpath('//div[@class="item-mod"]/h3/b/text()').extract_first().strip()
                    item['shop_name'] = shop_name
                    logger.info(real_house_facilities)
                    item['lat_lng'] = real_lat_lng
                    public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
                    item['public_time'] = public_time.strip()
                    house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
                    item['house_number'] = house_number.strip()
                    yield item
                except Exception as e:
                    logger.error('严重错误看日志',e.args)
                    if 'antispam' in response.url or 'jump' in response.url:
                        url = response.meta.get('redirect_urls')[0]
                    else:
                        url = response.url
                    logger.error('出现异常下载，可能IP有问题---------------：{}'.format(url))
                    logger.error('重新入库')
                    db.add_value('sp_detail:start_urls', url)
            else:
                logger.error('该URL已经失效：{}'.format(response.url))
                db.add_value('not_url:sp_detail', response.url)

    def gen_address(self,every_address):
        every_address[0] = every_address[0]+'市'
        province = get_key(every_address[0])
        every_address.insert(0,province)
        return every_address