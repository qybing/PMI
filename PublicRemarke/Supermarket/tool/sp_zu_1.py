from random import random
import math
import time
import re

import requests
import time

from parsel import Selector
from fake_useragent import UserAgent
from w3lib.html import remove_tags

# proxies_ips = [
#     'http://196.43.103.234:53281',
#     'http://121.43.170.207:3128',
#     'http://139.129.166.68:3128',
#     'http://118.190.95.43:9001',
#     'http://221.7.255.168:8080',
# ]
# house_config = {
#     '日租金': 'daily_hire',
#     '月租金': 'month_hire',
#     '得房率': 'get_house',
#     '楼盘名': 'house_name',
#     '地址': 'address',
#     '地铁': 'subway',
#     '建筑面积': 'covered_area',
#     '楼层': 'floor',
#     '工位数': 'station',
#     '物业费': 'property_management_fee',
#     '类型': 'type',
#     '总楼层': 'total_floor',
#     '竣工年月': 'completion_date',
#     '大堂层高': 'lobby_height',
#     '空调类型': 'air_conditioning_type',
#     '车位': 'parking_space',
#     '单层面积': 'every_area',
#     '物业公司': 'property_company',
#     '标准层高': 'standard_floor_hegiht',
#     '电梯': 'elevator',
#     '是否涉外': 'is_foregin',
#     '单价': 'unit_price',
#     '总价': 'total_price',
#     '面积': 'area',
#
#
#
#
#
# }
# sp_house_config = {
#     '总价':'total_price',
#     '单价':'unit_price',
#     '预期租金收益':'expected_rental_income',
#     '月租': 'monthly_rent',
#     '转让费': 'transfer_fee',
#     '物业费': 'property_management_fee',
#     '面积': 'area',
#     '面宽': 'face_width',
#     '层高': 'layer_height',
#     '进深': 'depth',
#     '楼层': 'floor',
#     '状态': 'status',
#     '起租期': 'lease_period',
#     '人群': 'crowd',
#     '押付': 'pay',
#     '免租期': 'rent_free_period',
#     '地址': 'address',
#     '是否临街': 'is_face_street',
#     '商铺名字': 'shop_name',
#     '开发商': 'developer',
#     '物业公司': 'property_company',
#     '统一管理': 'unified_management',
#     '竣工时间': 'completion_time',
#     '总楼层': 'total_floor',
#     '总面积': 'total_area',
#
# }

# 获取url网页内容，start_url为目标网址


def get_hcv():
    """
    计算cookies中的_hc.v
    """
    def n():
        def n():
            return str(hex(int(65536 * (1 + random()))))[3:]
        return '-'.join([n()+n(), n(), n(), n(), n()+n()+n()])
    def i():
        return n() + '.' + str(int(time.time()))
    return i()

def get_html_content(start_url):
    for tries in range(5):
        ua = UserAgent()
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "HE028T9448613Y4D"
        proxyPass = "9CFB203161ACD692"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        # url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        # proxies_ips = requests.get(url)
        # a = proxies_ips.text.replace('\r','').replace('\n','')
        # proxies = {
        #     "http": "http://{}".format('http://125.86.167.6:4697'),
        #     "https": "http://{}".format('http://125.86.167.6:4697'),
        # }
        # print(proxies)
        headers = {
            'Host': 'www.dianping.com',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': '_hc.v={};'.format(get_hcv())
        }
        try:
            res = requests.get(url=start_url,headers=headers)
            print(res.cookies)
            # print(res.headers['Location'])
            print(res)
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


# 获取所有列表url
def get_url_list(content, regular):
    xpath_css = Selector(text=content)
    urls = []
    url_lists = xpath_css.xpath(regular).extract()
    for url_list in url_lists:
        urls.append(url_list)
        # print(url_list)
    return urls


def handler_detail_msm_xzl(detail_urls_content, url):
    if '访问验证-安居客' not in detail_urls_content:
        lat_lng = re.findall(r'lat: "(.*?)",.*?lng: "(.*?)"', detail_urls_content, re.S)
        real_lat_lng = lat_lng[0]
        xpath_css = Selector(text=detail_urls_content)
        item = {}
        # if 'zu' in url:
        house_msgs_l = xpath_css.xpath('//*[@id="fy_info"]/ul[@class="litem"]/li')
        for house_msg in house_msgs_l:
            key1 = house_msg.xpath('./span[1]/text()').extract_first()
            key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
            item[key1] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()))
        house_msgs_r = xpath_css.xpath('//*[@id="fy_info"]/ul[@class="ritem"]/li')
        for house_msg in house_msgs_r:
            key1 = house_msg.xpath('./span[1]/text()').extract_first()
            key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
            if key1 == '预估月支出' and 'zu' in url:
                continue
            else:
                item[key1] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()))
        house_resources_l = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="litem"]/li')
        for house_resource in house_resources_l:
            key1 = house_resource.xpath('./span[1]/text()').extract_first()
            key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
            item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
        house_resources_r = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li')
        for house_resource in house_resources_r:
            key1 = house_resource.xpath('./span[1]/text()').extract_first()
            key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
            if key1 == '得房率':
                continue
            else:
                item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
        describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract_first()
        real_describe = remove_tags(str(describes))
        print(real_lat_lng)
        print(real_describe.strip())
        public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
        house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
        print(public_time, house_number)
        print(item)
    else:
        print('有验证码')


def main():
    # city_url = 'https://bj.sp.anjuke.com/shou/p1/'
    start_url = 'https://sh.sp.anjuke.com/shou/'
    start_url_content = get_html_content(start_url)
    if len(start_url_content) > 0:
        city_url_lists = get_url_list(start_url_content, '//*[@id="city_list"]/dl/dd/a/@href')
        for city_url_list in city_url_lists:
            for i in range(1, 10):
                city_url = city_url_list + 'p%s/' % i
                sleep_time = random.randint(2, 4)
                time.sleep(sleep_time)
                city_url_content = get_html_content(city_url)
                print(city_url_content)
                time.sleep(20)

                detail_urls = get_url_list(city_url_content, '//*[@id="list-content"]/div[@class="list-item"]/@link')
                for detail_url in detail_urls:
                    detail_urls_content = get_html_content(detail_url)
                    time.sleep(3)
                    result = handler_detail_msm_xzl(detail_urls_content)


def handler_detail_msm_sp(detail_urls_content, url):
    if '访问验证-安居客' not in detail_urls_content:
        lat_lng = re.findall(r'lat: "(.*?)",.*?lng: "(.*?)"', detail_urls_content, re.S)
        real_lat_lng = lat_lng[0]
        xpath_css = Selector(text=detail_urls_content)
        house_facilities = xpath_css.xpath('//ul[@class="mod-peitao clearfix"]/li[not(contains(@class,"gray"))]')
        real_house_facilities = []
        for rs in house_facilities:
            one = rs.xpath('./p/text()').extract_first()
            real_house_facilities.append(one)
        sp_item = {}
        sp_houses = xpath_css.xpath('//*[@id="fy_info"]/ul/li')
        for house_msg in sp_houses:
            key1 = str(house_msg.xpath('./span[1]/text()').extract_first()).replace('：','')
            key = sp_house_config.get(house_msg.xpath('./span[1]/text()').extract_first().replace('：',''))
            print(str(house_msg.xpath('./span[2]').extract_first()).replace('\n','').replace(' ',''))
            sp_item[key1] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()).replace('\n','').replace(' ',''))

        house_resources_l = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="litem"]/li')
        for house_resource in house_resources_l:
            key1 = house_resource.xpath('./span[1]/text()').extract_first()
            key = sp_house_config.get(house_resource.xpath('./span[1]/text()').extract_first().replace('：',''))
            sp_item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()).replace('\n','').replace(' ',''))
        house_resources_r = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li')
        for house_resource in house_resources_r:
            key1 = house_resource.xpath('./span[1]/text()').extract_first()
            key = sp_house_config.get(house_resource.xpath('./span[1]/text()').extract_first().replace('：',''))
            sp_item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
        describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract_first()
        real_describe = remove_tags(str(describes))
        shop_name = xpath_css.xpath('//div[@class="item-mod"]/h3/b/text()').extract_first().strip()
        print(shop_name)
        print(real_house_facilities)
        print(real_lat_lng)
        print(real_describe.strip())
        public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
        house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
        print(public_time, house_number)
        print(sp_item)




    else:
        print('有验证码')


if __name__ == '__main__':
    start_urls = ['http://www.dianping.com/shop/19421407']
    a = ['http://www.ip138.com/ips1388.asp']
    for start_url in start_urls:
        start_url_content = get_html_content(start_url)
        print(start_url_content)
        print('=========')

        # if 'xzl' in start_url:
        #     handler_detail_msm_xzl(start_url_content, start_url)
        # else:
        #     handler_detail_msm_sp(start_url_content, start_url)
