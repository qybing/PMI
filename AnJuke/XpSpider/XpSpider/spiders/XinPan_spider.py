# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from w3lib.html import remove_tags


class XinpanSpiderSpider(scrapy.Spider):
    name = 'XinPan_spider'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.fang.anjuke.com/loupan/canshu-443800.html']
    redis_key = "XinPan_spider:start_urls"

    def parse(self, response):
        if 'captcha-verify' in response.url:
            pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            urls = response.meta.get('redirect_urls')
            print('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
            for url in urls:
                r.rpush('XinPan_spider:start_urls', url)
        else:
            start_url_content = response.text
            detail_urls_content = start_url_content
            xpath_css = Selector(text=detail_urls_content)
            item = {}
            house_msgs_l = xpath_css.xpath('//*[@id="container"]/div[1]/div[1]/div/div[2]/ul/li')[:-2]
            for house_msg in house_msgs_l:
                key1 = house_msg.xpath('./div[1]/text()').extract_first()
                if '楼盘特点' in key1:
                    item[key1] = [i for i in str(
                        remove_tags(str(house_msg.xpath('./div[2]').extract_first()).replace('\n', ''))).strip().split(
                        ' ') if i]
                else:
                    # key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
                    item[key1] = remove_tags(
                        str(house_msg.xpath('./div[2]').extract_first()).replace('\n', '').replace(' ', ''))
            print(item)
