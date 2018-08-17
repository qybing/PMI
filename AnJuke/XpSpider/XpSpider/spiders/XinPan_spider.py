# -*- coding: utf-8 -*-
import redis
import scrapy
from parsel import Selector
from scrapy_redis.spiders import RedisSpider
from w3lib.html import remove_tags
from xpinyin import Pinyin
from scrapy.conf import settings

from tool.get_province import get_key
from tool.handle_redis import RedisClient


class XinpanSpiderSpider(RedisSpider):
    name = 'XinPan_spider'
    # allowed_domains = ['anjuke.com']
    start_urls = ['https://sh.fang.anjuke.com/loupan/canshu-416560.html',
                  'https://cd.fang.anjuke.com/loupan/canshu-435586.html',
                  'https://tj.fang.anjuke.com/loupan/canshu-415747.html',
                  'https://nn.fang.anjuke.com/loupan/canshu-431791.html',
                  'https://wh.fang.anjuke.com/loupan/canshu-413510.html',
                  'https://wh.fang.anjuke.com/loupan/canshu-410664.html',
                  'https://gz.fang.anjuke.com/loupan/canshu-410505.html',
                  'https://wh.fang.anjuke.com/loupan/canshu-410510.html',
                  'https://wh.fang.anjuke.com/loupan/canshu-437396.html',
                  'https://wx.fang.anjuke.com/loupan/canshu-413451.html',
                  ]
    redis_key = "XinPan_spider:start_urls"


    def parse(self, response):
        if 'verify' in response.url:
            db = RedisClient()
            urls = response.meta.get('redirect_urls')[0]
            print('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
            db.add_value('XinPan_spiders:start_urls', urls)
        else:
            item = {}
            start_url_content = response.text
            detail_urls_content = start_url_content
            xpath_css = Selector(text=detail_urls_content)
            every_address = [str(ad).replace('楼盘', '') for ad in xpath_css.xpath('//*[@id="header"]/div[2]/div[1]/a/text()').extract()[1:3]]
            if len(every_address)>0:
                new_address = self.gen_address(every_address)
                item['province'], item['city'], item['county'] = new_address[0], new_address[1], new_address[2]
                item['url'] = response.url
                pin = Pinyin()
                item['sheetname'] = pin.get_pinyin(item['province'], "").replace('sheng','').replace('shi','')
                house_msgs_l = xpath_css.xpath('//*[@id="container"]/div[1]/div[1]/div/div[2]/ul/li')[:-2]
                new_house = settings['NEWHOUSE']
                print(len(house_msgs_l),type(house_msgs_l))
                for house_msg in house_msgs_l:
                    key1 = house_msg.xpath('./div[1]/text()').extract_first()
                    key2 = new_house.get(key1)
                    if key2 == 'None':
                        print(key1)

                    if 'property_features' == key2:
                        item[key2] = [i for i in str(
                            remove_tags(str(house_msg.xpath('./div[2]').extract_first())
                                        .replace('\n', ''))).strip().split(
                            ' ') if i]
                    else:
                        item[key2] = remove_tags(
                            str(house_msg.xpath('./div[2]').extract_first())
                                        .replace('\n', '').replace(' ', '').replace(r'[价格走势]', '')
                                        .replace(r'[查看地图]', '').replace(r'[房贷计算器]','')
                                        .replace(r'[查看详情]', '').replace(r'[查看详情]', '')
                                        )
                print(item)



            else:
                print('这是个严重的错误')
                print(response.url)
                db = RedisClient()
                urls = response.meta.get('redirect_urls')[0:1]
                print(urls)
                print('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
                for url in urls:
                    db.add_value('XinPan_spider:start_urls', url)

    # def get_comment(self,response):
    #     print('到get_comment')
    #     if 'captcha-verify' in response.url:
    #         db = RedisClient()
    #         urls = response.meta.get('redirect_urls')
    #         print('遇到验证码了，url:{}重新放入待爬队列里面'.format(urls))
    #         # for url in urls:
    #             # db.add_value('XinPan_spider:start_urls', url)
    #     else:
    #         html = response.text
    #         xpath_css = Selector(text=html)
    #         comment_number = xpath_css.xpath('//div[@class="total-comment"]/div[1]/h3/a[1]/text()').extract_first()
    #         item = response.meta.get('item')
    #         item['点评'] = comment_number
    #         print(item)
    #         yield item



    def gen_address(self,every_address):
        every_address[0] = every_address[0]+'市'
        province = get_key(every_address[0])
        every_address.insert(0,province)
        return every_address