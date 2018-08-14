# -*- coding: utf-8 -*-
import re

import redis
import scrapy
from parsel import Selector
from scrapy import Request

from tool.handle_redis import RedisClient


class DetaillistSpider(scrapy.Spider):
    name = 'DetailList'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "DetailList:start_urls"

    def parse(self, response):
        # pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
        # r = redis.Redis(connection_pool=pool)
        db = RedisClient()
        detail_urls_content = response.text
        xpath_css = Selector(text=detail_urls_content)
        if 'captcha-verify' in response.url:
            urls = response.meta.get('redirect_urls')
            print('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
            for url in urls:
                db.add_value('XinPanCity:start_urls', url)
        sp_urls = [str(sp_url).replace(r'loupan/', r'loupan/canshu-') for sp_url in
                   xpath_css.xpath('//*[@id="container"]/div[2]/div[1]/div[@class="key-list"]/div/@data-link').extract()]
        if len(sp_urls) > 0:
            for sp_url in sp_urls:
                db.add_value('DetailList:start_urls', sp_url)
        print(sp_urls)
        print('一共有{}个楼盘url,入库成功'.format(len(sp_urls)))
        next_page = xpath_css.xpath('//a[@class="next-page next-link"]/@href').extract_first()
        if next_page:
            try:
                page = re.search(r'p(\d+)', next_page)
                print('第{}页---网址为：{}'.format(page.group(1), next_page))
            except Exception as e:
                print('出错原因：{}'.format(e.args))
            yield Request(url=next_page, callback=self.parse)
