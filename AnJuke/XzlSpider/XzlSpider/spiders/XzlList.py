# -*- coding: utf-8 -*-
import re

import redis
import scrapy
from parsel import Selector
from scrapy import Request


class XzllistSpider(scrapy.Spider):
    name = 'XzlList'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']
    redis_key = "XzlList:start_urls"

    def parse(self, response):
        pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        city_content = response.text
        xpath_css = Selector(text=city_content)
        sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        if 'captcha-verify' in response.url:
            print('遇到验证码了，url放入待爬队列里面')
            urls = response.meta.get('redirect_urls')
            for url in urls:
                r.rpush('XzlList:start_urls', url)

        elif len(sp_urls) < 0 or '请换个搜索词或试试筛选吧' in city_content:
                print('本url:{}-----没有搜索结果'.format(response.url))
                r.rpush('not_url:xzl', response.url)
        else:
            sp_urls = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
            for sp_url in sp_urls:
                r.rpush('DetailSpider:start_urls', sp_url)
            print(sp_urls)
            print('一共{}个url已经入库完毕'.format(len(sp_urls)))
            next_page = xpath_css.xpath('//a[@class="aNxt"]/@href').extract_first()
            if next_page:
                try:
                    page = re.search(r'p(\d+)', next_page)
                    print('第{}页---网址为：{}'.format(page.group(1), next_page))
                except Exception as e:
                    print('出错原因：{}'.format(e.args))
                yield Request(url=next_page,callback=self.parse)
