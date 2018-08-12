import random
import re

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
house_config = {
    '日租金': 'daily_hire',
    '月租金': 'month_hire',
    '得房率': 'get_house',
    '楼盘名': 'house_name',
    '地址': 'address',
    '地铁': 'subway',
    '建筑面积': 'covered_area',
    '楼层': 'floor',
    '工位数': 'station',
    '物业费': 'property_management_fee',
    '类型': 'type',
    '总楼层': 'total_floor',
    '竣工年月': 'completion_date',
    '大堂层高': 'lobby_height',
    '空调类型': 'air_conditioning_type',
    '车位': 'parking_space',
    '单层面积': 'every_area',
    '物业公司': 'property_company',
    '标准层高': 'standard_floor_hegiht',
    '电梯': 'elevator',
    '是否涉外': 'is_foregin',
    '单价': 'unit_price',
    '总价': 'total_price',
    '面积': 'area',





}


sp_house_config = {
    '总价':'total_price',
    '单价':'unit_price',
    '预期租金收益':'expected_rental_income',
    '月租': 'monthly_rent',
    '转让费': 'transfer_fee',
    '物业费': 'property_management_fee',
    '面积': 'area',
    '面宽': 'face_width',
    '层高': 'layer_height',
    '进深': 'depth',
    '楼层': 'floor',
    '状态': 'status',
    '起租期': 'lease_period',
    '人群': 'crowd',
    '押付': 'pay',
    '免租期': 'rent_free_period',
    '地址': 'address',
    '是否临街': 'is_face_street',
    '商铺名字': 'shop_name',
    '开发商': 'developer',
    '物业公司': 'property_company',
    '统一管理': 'unified_management',
    '竣工时间': 'completion_time',
    '总楼层': 'total_floor',
    '总面积': 'total_area',

}

# 获取url网页内容，start_url为目标网址
def get_html_content(start_url):
    for tries in range(5):
        ua = UserAgent()
        # url = 'http://127.0.0.1:5000/get'
        # proxies_ips = requests.get(url)
        # print(random.choice(proxies_ips))
        headers = {
            'User-Agent': '{}'.format(ua.random),
        }
        # proxies = {
        #     "http": "http://{}".format(proxies_ips.text),
        #     # "https": "http://170.244.141.53:53281",
        # }
        # print(proxies)
        try:
            res = requests.get(url=start_url, headers=headers)
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
        # else:
        #     house_msgs_l = xpath_css.xpath('//*[@id="fy_info"]/ul[@class="litem"]/li')
        #     for house_msg in house_msgs_l:
        #         key1 = house_msg.xpath('./span[1]/text()').extract_first()
        #         key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
        #         item[key1] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()))
        #     house_msgs_r = xpath_css.xpath('//*[@id="fy_info"]/ul[@class="ritem"]/li')
        #     for house_msg in house_msgs_r:
        #         key1 = house_msg.xpath('./span[1]/text()').extract_first()
        #         key = house_config.get(house_msg.xpath('./span[1]/text()').extract_first())
        #         item[key1] = remove_tags(str(house_msg.xpath('./span[2]').extract_first()))
        #     house_resources_l = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="litem"]/li')
        #     for house_resource in house_resources_l:
        #         key1 = house_resource.xpath('./span[1]/text()').extract_first()
        #         key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
        #         item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
        #     house_resources_r = xpath_css.xpath('//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li')
        #     for house_resource in house_resources_r:
        #         key1 = house_resource.xpath('./span[1]/text()').extract_first()
        #         key = house_config.get(house_resource.xpath('./span[1]/text()').extract_first())
        #         if key1 == '得房率':
        #             continue
        #         else:
        #             item[key1] = remove_tags(str(house_resource.xpath('./span[2]').extract_first()))
        #     describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract_first()
        #     real_describe = remove_tags(str(describes))
        #     print(real_describe.strip())
        #     public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
        #     house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
        #     print(public_time, house_number)
        #     print(item)

        # if 'zu' in url:
        #     #标题
        #     total = xpath_css.xpath('//*[@id="j-triggerlayer"]/text()').extract_first()
        #     #日租金
        #     daily_hire = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[1]/span[2]/text()').extract_first()
        #     #建筑面积
        #     covered_area = xpath_css.xpath('//*[@id="fy_info"]/ul[2]/li[1]/span[2]/text()').extract_first()
        #     #月租金
        #     month_hire = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[2]/span[2]/text()').extract_first()
        #     #得房率
        #     get_house = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[3]/span[2]/text()').extract_first()
        #
        #     station = xpath_css.xpath('//*[@id="fy_info"]/ul[2]/li[3]/span[2]/text()').extract_first()
        #     houses = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[4]/span[2]/a/text()').extract_first()
        #     property_management_fee = xpath_css.xpath('//*[@id="fy_info"]/ul[2]/li[4]/span[2]/text()').extract_first()
        #     address = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[5]/span[2]/text()').extract_first()
        #     subway = xpath_css.xpath('//*[@id="fy_info"]/ul[1]/li[6]/span[2]/text()')
        #     describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract()
        #     real_describe = remove_tags(str(describes))
        #     # print(res_describe)
        #     public_time  = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
        #     house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
        #     type = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[1]/span[2]/text()').extract_first()
        #     single_layer_area = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[1]/span[2]/text()').extract_first()
        #     total_floor = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[2]/span[2]/text()').extract_first()
        #     room_rate = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[2]/span[2]/text()').extract_first()
        #     completion_date = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[3]/span[2]/text()').extract_first()
        #     property_company = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[3]/span[2]/text()').extract_first()
        #     lobby_height = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[4]/span[2]/text()').extract_first()
        #     standard_floor_hegiht = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[4]/span[2]/text()').extract_first()
        #
        #     air_conditioning_type = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[5]/span[2]/text()').extract_first()
        #     elevator = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[5]/span[2]/text()').extract_first()
        #     parking_space = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[1]/li[6]/span[2]/text()').extract_first()
        #     is_foregin = xpath_css.xpath('//*[@id="content"]/div/div[2]/div[1]/div[3]/div/ul[2]/li[6]/span[2]/text()').extract_first()
        #     deatil_mss = (total.strip(),real_lat_lng,daily_hire,covered_area,month_hire,get_house,station,
        #                   houses,property_management_fee,address,subway,real_describe,
        #                   str(public_time).replace('\t',''),str(house_number).replace('\t',''),type,single_layer_area,
        #                   total_floor,room_rate,completion_date,property_company,lobby_height,standard_floor_hegiht,air_conditioning_type
        #                   ,elevator,parking_space,is_foregin)
        #     print(deatil_mss)
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
        # print(url)
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
        shop_name = xpath_css.xpath('//div[@class="item-mod"]/h3/b/text()').extract_first().strip()
        print(shop_name)
        print(real_house_facilities)
        print(real_lat_lng)
        print(real_describe.strip())
        public_time = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root
        house_number = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root
        print(public_time, house_number)
        print(sp_item)




        # print(real_house_facilities)
        # 总价 = ''
        # 单价 = ''
        # 月租 = ''
        # 转让费 = ''
        # 预期租金收益 = ''
        # total = xpath_css.xpath('//*[@id="content"]/div/h1/text()').extract_first().strip()
        # 物业费 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[3]/span[2]/text()').extract_first().strip()
        # 面积 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[4]/span[2]/text()').extract_first().strip()
        # 面宽 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[5]/span[2]/text()').extract_first().strip()
        # 层高 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[6]/span[2]/text()').extract_first().strip()
        # if 'zu' in url:
        #     楼层 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[8]/span[2]/text()').extract_first().strip()
        #     if '层' not in 楼层:
        #         楼层 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[7]/span[2]/text()').extract_first().strip()
        #     进深 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[7]/span[2]/text()').extract_first().strip()
        #     if 'm' not in 进深:
        #         进深 = ''
        #     月租 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[1]/span[2]/text()').extract_first().strip()
        #     转让费 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[2]/span[2]/text()').extract_first().strip()
        #     状态 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[9]/span[2]/text()').extract_first().strip()
        #     起租期 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[10]/span[2]/text()').extract_first().strip()
        #     人群 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[11]/span[2]/text()').extract_first().replace(r'\n',
        #                                                                                                 '').strip()
        #     押付 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[12]/span[2]/text()').extract_first().strip()
        #     免租期 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[14]/span[2]/text()').extract_first()
        #     地址 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[13]/span[2]/@title').extract_first()
        #     is_street = xpath_css.xpath('//*[@id="fy_info"]/ul/li[15]/span[2]/text()').extract_first()
        #     if is_street:
        #         是否临街 = is_street.strip()
        #     else:
        #         try:
        #             是否临街 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[14]/span[2]/text()').extract_first().strip()
        #         except:
        #             是否临街 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[13]/span[2]/text()').extract_first().strip()
        #
        # else:
        #     楼层 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[7]/span[2]/text()').extract_first().strip()
        #     进深 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[8]/span[2]/text()').extract_first().strip()
        #     总价 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[1]/span[2]/text()').extract_first().strip()
        #     单价 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[2]/span[2]/text()').extract_first().strip()
        #     状态 = ''
        #     起租期 = ''
        #     人群 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[9]/span[2]/text()').extract_first().replace(r'\n',
        #                                                                                                '').strip()
        #     押付 = ''
        #     免租期 = ''
        #     地址 = xpath_css.xpath('//span[@class="desc addresscommu"]/@title').extract_first()
        #     预期租金收益 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[11]/span[2]/text()').extract_first()
        #     try:
        #         是否临街 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[13]/span[2]/text()').extract_first().strip()
        #     except:
        #         是否临街 = xpath_css.xpath('//*[@id="fy_info"]/ul/li[12]/span[2]/text()').extract_first()
        # 发布时间 = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[1].root.strip()
        # 房源编号 = xpath_css.xpath('//*[@id="xzl_desc"]/h3/div/text()')[2].root.strip()
        # describes = xpath_css.xpath('//*[@id="xzl_desc"]/div').extract()
        # 房源描述 = remove_tags(str(describes))
        #
        # 商铺小区名字 = xpath_css.xpath('//div[@class="item-mod"]/h3/b/text()').extract_first().strip()
        # 开发商 = xpath_css.xpath(
        #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[1]/span[2]/text()').extract_first()
        # 物业公司 = xpath_css.xpath(
        #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[2]/span[2]/text()').extract_first()
        # 物业费 = xpath_css.xpath(
        #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[3]/span[2]/text()').extract_first().replace(r'\n',
        #                                                                                                         '').strip()
        # 统一管理 = xpath_css.xpath(
        #     '//div[@class="itemCon clearfix"]/ul[@class="litem"]/li[4]/span[2]/text()').extract_first().replace(r'\n',
        #                                                                                                         '').strip()
        # 竣工时间 = xpath_css.xpath(
        #     '//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li[1]/span[2]/text()').extract_first()
        # 总楼层 = xpath_css.xpath(
        #     '//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li[2]/span[2]/text()').extract_first()
        # 总面积 = xpath_css.xpath(
        #     '//div[@class="itemCon clearfix"]/ul[@class="ritem"]/li[3]/span[2]/text()').extract_first()
        #
        # deatil_mss = (total, 月租, 转让费, 总价, 单价, 物业费, 面积, 面宽, 层高, 进深, 楼层, 状态, 起租期, 人群, 押付, 地址,
        #               免租期, 是否临街, 发布时间, 房源编号, 房源描述, 商铺小区名字, 开发商, 物业公司, 物业费, 统一管理, 竣工时间,
        #               总楼层, 总面积)
        #
        # rs = 'total:%s,月租:%s,转让费:%s,总价:%s,单价:%s,物业费:%s,面积:%s,面宽:%s,层高:%s,进深:%s,楼层:%s,状态:%s,起租期:%s,人群:%s ,押付:%s ,地址:%s,免租期:%s,是否临街:%s,发布时间:%s,房源编号:%s ,房源描述:%s ,商铺小区名字:%s,开发商:%s ,物业公司:%s ,物业费:%s,统一管理:%s,竣工时间:%s,总楼层:%s,总面积:%s' % (
        #     deatil_mss)
        # print(rs)
    else:
        print('有验证码')


if __name__ == '__main__':
    start_urls = ['https://bj.sp.anjuke.com/zu/58632051/?pt=2', 'https://bj.sp.anjuke.com/zu/59267202/?pt=2',
                  'https://bj.sp.anjuke.com/zu/59324737/?pt=2', 'https://bj.sp.anjuke.com/zu/59233021/?pt=2',
                  'https://bj.sp.anjuke.com/zu/59245229/?pt=2', 'https://bj.sp.anjuke.com/zu/59331314/?pt=2',
                 ]
    a = ['https://sh.sp.anjuke.com/zu/59391219/?pt=2']
    for start_url in a:
        start_url_content = get_html_content(start_url)
        if 'xzl' in start_url:
            handler_detail_msm_xzl(start_url_content, start_url)
        else:
            handler_detail_msm_sp(start_url_content, start_url)


'//div[@class="key-list"]/div[@class="item-mod"]/@data-link'