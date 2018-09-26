import json
import re
import time

import requests
from fake_useragent import UserAgent
from parsel import Selector
from selenium import webdriver
from w3lib.html import remove_tags

from xiecheng.tool.handle_redis import RedisClient

city_list = 'http://hotels.ctrip.com/domestic-city-hotel.html'

def get_html_content(start_url,data=None):
    for tries in range(5):
        # ua = UserAgent()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Host':'hotels.ctrip.com'
        }
        try:
            if data:
                res = requests.get(url=start_url,params=data,headers=headers)
                if res.status_code == 200:
                    return res.content.decode('utf-8')
            else:
                res = requests.get(url=start_url,headers=headers)
                if res.status_code == 200:
                    return res.content.decode('utf-8')
        except Exception as e:
            print(e.args)
            if tries < (5 - 1):
                time.sleep(tries + 1)  # hava a rest
                print('retry:' + start_url)
                continue
            else:
                print('没有获取到网页数据')
                return ''


def handler_mes(content):
    print(content)
    distance = re.findall("ajaxGetHotelAddtionalInfo:'(.*?),",content,re.DOTALL)[0]
    print(distance)
    # html = Selector(text=content)
    # room = html.xpath('//td[@class="child_name"]').extract()
    # name = html.xpath('//*[@id="J_htl_info"]/div[1]/h2[1]/text()').extract_first()
    # a = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_imgStar"]/@title').extract_first()
    # b = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_imgStar"]/@class').extract_first()
    # grade = a+'-'+b
    # city = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkCity"]/text()').extract_first()
    # area = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkLocation"]/text()').extract_first()
    # address = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lbAddress"]/text()').extract_first()
    # road_cross = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkRoadCross"]/text()').extract_first()
    # area_extra = html.xpath('//*[@id="ctl00_MainContentPlaceHolder_commonHead_lnkMapZone"]/text()').extract_first()
    # phone = html.xpath('//*[@id="J_realContact"]/@data-real').extract_first()
    # rating = html.xpath('//div[@class="htl_com_box basefix"]/a/p[1]/span/text()').extract_first()
    # recommend = html.xpath('//div[@class="htl_com_box basefix"]/a/p[2]/text()').extract_first()
    # reviews = html.xpath('//div[@class="htl_com_box basefix"]/a/span/span/text()').extract_first()
    # lat = html.xpath('//*[@id="aspnetForm"]/div[6]/meta[1]/@content').extract_first()
    # lng = html.xpath('//*[@id="aspnetForm"]/div[6]/meta[2]/@content').extract_first()
    # description = remove_tags(str(html.xpath('//*[@id="htlDes"]').extract_first()))
    # main_photo = html.xpath('//*[@id="topPicList"]/meta/@content').extract_first()
    # photo = html.xpath('//*[@id="topPicList"]/div/div/@_src').extract()
    # hotel_amenities = remove_tags(str(html.xpath('//*[@id="J_htl_facilities"]').extract_first()))
    # hotel_policy = remove_tags(str(html.xpath('//*[@id="hotel_info_comment"]/div/div[7]').extract_first()))
    # nearby_amenities = remove_tags(str(html.xpath('//*[@id="hotel_info_comment"]/div/div[8]').extract_first()))
    # traffic = remove_tags(str(html.xpath('//div[@class="traffic_side"]/div[@class="traffic_box"]/div').extract_first()))
    # v = html.xpath('//*[@id="topPicList"]/meta/@content').extract_first()
    # print(city)


def handler_url(content):
    html = json.loads(content)
    data_page = re.compile('data-pagecount=(\d+) name=')
    page = html['paging']
    page_count = re.findall(data_page,page)[0]
    value = html['HotelMaiDianData']['value']
    htllist = value['htllist'].replace("[","").replace("]","")
    print(page_count)
    htllists = htllist[1:-1].split('},{')
    for i in htllists:
        c = re.findall('"hotelid":"(\d+)","amount":"(\d+)"', i)
        print(c[0][0], c[0][1])
    print(len(htllists))
    print(type(htllist))


def get_city(content):
    base_url = 'http://hotels.ctrip.com/'
    html = Selector(text=content)
    url_list = html.xpath('//*[@id="base_bd"]/dl/dd/a/@href').extract()
    city_url = []
    db = RedisClient()
    for i in url_list:
        num = re.findall('(\d+)',i)[0]
        print(base_url+i)
        print(num)
        db.add_value('CtripCity:start_urls',num)

        city_url.append(num)
    print(len(city_url))


def start():
    api = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
    url = 'http://hotels.ctrip.com/hotel/6817123.html'
    cityList = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
    data = {
        'cityId': '59',
        'page': '1'
    }
    html = get_html_content(url)
    # driver_path = r'E:\ch\chromedriver.exe'
    # driver = webdriver.Chrome(executable_path=driver_path)
    # driver.get('http://hotels.ctrip.com/hotel/428365.html')
    # html = driver.page_source
    # driver.close()
    # print(html)
    handler_mes(html)
    # handler_url(content)
    # get_city(content)

if __name__ == '__main__':
    start()