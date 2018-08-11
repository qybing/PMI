import random
import re

import pymysql
import requests
import time

from parsel import Selector
from fake_useragent import UserAgent
from w3lib.html import remove_tags

proxies_ips = [
    'http://196.43.103.234:53281',
    'http://121.43.170.207:3128',
    'http://139.129.166.68:3128',
    'http://118.190.95.43:9001',
    'http://221.7.255.168:8080',
]

db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='jovan',
                     charset='utf8')
cursor = db.cursor()


# 获取url网页内容，start_url为目标网址
def get_html_content(start_url):
    for tries in range(5):
        ua = UserAgent()
        url = 'http://127.0.0.1:5000/get'
        proxies_ips = requests.get(url)
        # print(random.choice(proxies_ips))
        headers = {
            'User-Agent': '{}'.format(ua.random),
        }
        proxies = {
            "http": "http://{}".format(proxies_ips.text),
            # "https": "http://170.244.141.53:53281",
        }
        print(proxies)
        try:
            res = requests.get(url=start_url, headers=headers, proxies=proxies)
            # print(res)
            if res.status_code == 200:
                return res.text
        except:
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


def handler_detail_msm_xzl(detail_urls_content):
    if '访问验证-安居客' not in detail_urls_content:
        lat_lng = re.findall(r'lat: "(.*?)",.*?lng: "(.*?)"', detail_urls_content, re.S)
        real_lat_lng = lat_lng[0]
        xpath_css = Selector(text=detail_urls_content)
        total = xpath_css.xpath('//*[@id="j-triggerlayer"]/text()').extract_first()
        daily_hire = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[1]/span[2]/text()').extract_first()
        covered_area = xpath_css.xpath('//*[@id="fy_info"]/ul[2]/li[1]/span[2]/text()').extract_first()
        month_hire = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[2]/span[2]/text()').extract_first()
        get_house = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[3]/span[2]/text()').extract_first()
        station = xpath_css.xpath('//*[@id="fy_info"]/ul[2]/li[3]/span[2]/text()').extract_first()
        houses = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[4]/span[2]/a/text()').extract_first()
        property_management_fee = xpath_css.xpath('//*[@id="fy_info"]/ul[2]/li[4]/span[2]/text()').extract_first()
        address = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[5]/span[2]/text()').extract_first()
        subway = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[6]/span[2]/text()')
        describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract()
        real_describe = remove_tags(str(describes))
        # print(res_describe)
        public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
        house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
        type = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[1]/span[2]/text()').extract_first()
        single_layer_area = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[1]/span[2]/text()').extract_first()
        total_floor = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[2]/span[2]/text()').extract_first()
        room_rate = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[2]/span[2]/text()').extract_first()
        completion_date = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[3]/span[2]/text()').extract_first()
        property_company = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[3]/span[2]/text()').extract_first()
        lobby_height = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[4]/span[2]/text()').extract_first()
        standard_floor_hegiht = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[4]/span[2]/text()').extract_first()

        air_conditioning_type = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[5]/span[2]/text()').extract_first()
        elevator = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[5]/span[2]/text()').extract_first()
        parking_space = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[6]/span[2]/text()').extract_first()
        is_foregin = xpath_css.xpath(
            '//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[6]/span[2]/text()').extract_first()
        deatil_mss = (total.strip(), daily_hire, covered_area, month_hire, get_house, station,
                      houses, property_management_fee, address, subway, real_describe,
                      str(public_time).replace('\t', ''), str(house_number).replace('\t', ''), type, single_layer_area,
                      total_floor, room_rate, completion_date, property_company, lobby_height, standard_floor_hegiht,
                      air_conditioning_type
                      , elevator, parking_space, is_foregin)
        print(deatil_mss)
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
        xpath_css = Selector(text=detail_urls_content)
        city_lists = []
        citys = xpath_css.xpath('//*[@id="city_list"]/dl/dd/a/@href').extract()
        print(citys)
        print(len(citys))
        return citys
    else:
        print('有验证码')


def get_city_list_url(city_content):
    citys = []
    if '访问验证-安居客' not in city_content:
        xpath_css = Selector(text=city_content)

        citys = xpath_css.xpath('//*[@id="list-content"]/div[@class="list-item"]/@link').extract()
        print(citys)
        return citys
    else:
        print('有验证码')
        time.sleep(5)
        return citys


def get_city_area_list_url(city_content):
    if '访问验证-安居客' not in city_content:
        xpath_css = Selector(text=city_content)
        msm_lists = []
        citys = xpath_css.xpath(
            '/html/body/div[5]/div[2]/div/div[1]/div/a[not(contains(@class,"selected-item"))]/@href').extract()
        print(citys)
        print(len(citys))
        return citys
    else:
        print('有验证码')


def check_url():
    sql = 'select url from sp_url'
    cursor.execute(sql)
    rs = cursor.fetchall()
    urls = []
    for row in rs:
        urls.append(row[0])
    return urls


def save_to_mysql(new_urls):
    urls = check_url()
    # print(len(new_urls))
    real_new_urls = list(set(new_urls).difference(set(urls)))    #new_urls中有的urls中没有的
    # print(len(real_new_urls))
    if len(real_new_urls)>0:
        for real_new_url in real_new_urls:
            sql = 'insert into sp_url(url) values (%s)'
            try:
                cursor.execute(sql,(real_new_url))
                db.commit()
                # print('插入：{}成功'.format(real_new_url))
            except Exception as e:
                print('插入失败')
                print(e.args)
    else:
        print('已经存在')

if __name__ == '__main__':
    start_url = 'https://bj.sp.anjuke.com/zu/'
    start_url_content = get_html_content(start_url)
    citys = handler_detail_msm_sp(start_url_content, start_url)
    # all_urls = []
    # for i in range(1, 100):
    #     city_content = get_html_content('https://sh.sp.anjuke.com/zu/p{}'.format(i))
    #     urls = get_city_list_url(city_content)
    #     save_to_mysql(urls)
    #
    #     # all_urls.extend(urls)
    # print('执行完毕')
    # real_all_urls = list(set(all_urls))
    # save_to_mysql(real_all_urls)
        # get_city_area_list_url(city_content)
