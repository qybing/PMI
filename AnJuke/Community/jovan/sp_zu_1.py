import random
import re

import requests
import time

from parsel import Selector
from fake_useragent import UserAgent
from w3lib.html import remove_tags

from tool.get_province import get_key
from xpinyin import Pinyin

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
            # 'cookie':'aQQ_ajkguid=C141A079-79E2-5DF0-5D8C-B7DB051B55FE; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DrQ3-9-em6KV5g6zUY4KO3wT3nkXsDYJ1xF_O1ZVaFq2BXm9f6srRKVWUFf5E-LMp%26ck%3D3630.2.95.230.187.210.180.240%26shh%3Dwww.baidu.com%26wd%3D%26eqid%3Db083a0ff00006fc7000000045b8e394d; twe=2; sessid=1B8CE2D8-FF9E-3333-12F1-3C0C3AE5C017; _ga=GA1.2.1630890121.1536047440; _gid=GA1.2.40381559.1536047440; 58tj_uuid=68ecc76e-2707-4941-a119-0e96e0fa5663; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DrQ3-9-em6KV5g6zUY4KO3wT3nkXsDYJ1xF_O1ZVaFq2BXm9f6srRKVWUFf5E-LMp%2526ck%253D3630.2.95.230.187.210.180.240%2526shh%253Dwww.baidu.com%2526wd%253D%2526eqid%253Db083a0ff00006fc7000000045b8e394d; new_uv=1; als=0; new_session=0; wmda_uuid=285a492576171f171d22c6ec7d1162f3; wmda_new_uuid=1; wmda_session_id_6289197098934=1536047453259-9775b076-be6d-f946; wmda_visited_projects=%3B6289197098934; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1536047458; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1536050004; ctid=14'
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


def get_city_list(start_url_content):
    html = Selector(text=start_url_content)
    url_lists = html.xpath('//div[@class="letter_city"]/ul/li/div[@class="city_list"]/a/@href').extract()
    urls = []
    end = r'/community/?from=navigation'
    print(url_lists)
    print(len(url_lists))
    for url_list in url_lists:
        urls.append(url_list+end)
    print(len(urls))
    print(urls)
    # return urls


def get_area_list(start_url_content):
    html = Selector(text=start_url_content)
    count = html.xpath('//span[@class="tit"]/em[2]/text()').extract_first()
    print('一共有{}个'.format(count))
    if int(count)<3000:
        print('直接把URL存到list列表中')
    else:
        print('细分到区')
        areas = html.xpath('//div[@class="div-border items-list"]/div[1]/span[2]/a/@href').extract()[1:]
        # for area in areas:
        #     print('存进去{}'.format(area))
        print(areas)
        print('一共有{}个地区'.format(len(areas)))

    pass


def get_add_list(start_url_content):
    html = Selector(text=start_url_content)
    count = html.xpath('//span[@class="tit"]/em[2]/text()').extract_first()
    print('一共有{}个'.format(count))
    if int(count) < 3000:
        print('直接把URL存到list列表中')
    else:
        print('细分到地点')
        areas = html.xpath('//div[@class="sub-items"]/a/@href').extract()[1:]
        # for area in areas:
        #     print('存进去{}'.format(area))
        print(areas)
        print('一共有{}个地点'.format(len(areas)))
ho = {
    '物业类型':'property_type',
    '物业费':'property_costs',
    '总建面积':'total_area',
    '总户数':'total_houses',
    '建造年代':'construction_age',
    '停车位':'park',
    '容积率':'volume_rate',
    '绿化率':'greening_rate',
    '开发商':'developer',
    '物业公司':'property_company',
}

def get_house_list(start_url_content):
    html = Selector(text=start_url_content)
    count = html.xpath('//span[@class="tit"]/em[2]/text()').extract_first()
    print('一共有{}个'.format(count))
    if int(count) < 3000:
        print('直接把URL存到list列表中')
    else:
        print('细分到地点')
        areas = html.xpath('//*[@id="list-content"]/div[@class="li-itemmod"]/@link').extract()[1:]
        # for area in areas:
        #     print('存进去{}'.format(area))
        print(areas)
        print('一共有{}个地点'.format(len(areas)))

def gen_address(every_address):
    every_address = every_address + '市'
    province = get_key(every_address)
    # every_address.insert(0, province)
    return province

def get_hous_detail(start_url_content):
    try:
        price = re.findall('"comm_midprice":"(.*?)","area_midprice"',start_url_content,re.S)[0]
    except:
        price = re.findall('"comm_midprice":(.*?),"area_midprice"',start_url_content,re.S)[0]
    print(price)
    l2 = re.findall('lat : "(.*?)",.*?lng : "(.*?)"',start_url_content,re.S)
    lat_lng= [float(l2[0][0]), float(l2[0][1])]
    print(lat_lng)
    html = Selector(text=start_url_content)
    detali_dt = html.xpath('//*[@id="basic-infos-box"]/dl/dt')
    address = html.xpath('//span[@class="sub-hd"]/text()').extract_first()
    all_add = html.xpath('//div[@class="p_1180 p_crumbs"]/a/text()').extract()
    city = all_add[1].replace('小区','')
    county = all_add[2]
    community = all_add[3]
    community_name = all_add[4]
    pin = Pinyin()
    province = gen_address(city)
    sheet_name = pin.get_pinyin(province, "").replace('sheng', '').replace('shi', '')
    print(province,city,county,community,community_name)
    print(address)
    dt = []
    for i in detali_dt:
        key1 = i.xpath('./text()').extract_first().replace('\xa0','').replace('：','')
        key = ho.get(key1)
        dt.append(key)
        # print('{}{}'.format(i.xpath('./dt/text()').extract_first(),i.xpath('./dd/text()').extract_first()))
        # print('{}'.format(i.xpath('./text()').extract_first()))
    detali_dd = html.xpath('//*[@id="basic-infos-box"]/dl/dd')
    dd = []
    for i in detali_dd:
        dd.append(i.xpath('./text()').extract_first())
        # print('{}{}'.format(i.xpath('./dt/text()').extract_first(),i.xpath('./dd/text()').extract_first()))
        # print('{}'.format(i.xpath('./text()').extract_first()))

    a = dict(zip(dt,dd))
    print(a)
    # for i in a:
    #     print(i)
    # print(a)

if __name__ == '__main__':
    start_urls = ['https://bj.sp.anjuke.com/zu/58632051/?pt=2', 'https://bj.sp.anjuke.com/zu/59267202/?pt=2',
                  'https://bj.sp.anjuke.com/zu/59324737/?pt=2', 'https://bj.sp.anjuke.com/zu/59233021/?pt=2',
                  'https://bj.sp.anjuke.com/zu/59245229/?pt=2', 'https://bj.sp.anjuke.com/zu/59331314/?pt=2',
                 ]
    # a = 'https://shanghai.anjuke.com/community/view/820074?from=Filter_1&hfilter=filterlist'
    a = 'https://nanjing.anjuke.com/community/view/346221?from=Filter_1&hfilter=filterlist'
    b = 'https://dingxi.anjuke.com/community/view/995609#'
    # fordata = {
    #     'commid':'820074',
    #     'useflg':'onlyForAjax',
    # }
    # for start_url in a:
    start_url_content = get_html_content(a)
    print(start_url_content)
    # citys = get_city_list(start_url_content)
    # get_area_list(start_url_content)
    # get_add_list(start_url_content)
    # get_house_list(start_url_content)
    get_hous_detail(start_url_content)

        # if 'xzl' in start_url:
        #     handler_detail_msm_xzl(start_url_content, start_url)
        # else:
        #     handler_detail_msm_sp(start_url_content, start_url)


