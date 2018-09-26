import json
import re
import time

import requests
from parsel import Selector

from xiecheng.tool.handle_redis import RedisClient

city_list = 'http://hotels.ctrip.com/domestic-city-hotel.html'
def get_html_content(start_url, data=None):
    for tries in range(5):
        # ua = UserAgent()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'Host': 'hotels.ctrip.com'
        }
        try:
            if data:
                res = requests.get(url=start_url, params=data, headers=headers)
                if res.status_code == 200:
                    return res.content.decode('utf-8')
            else:
                res = requests.get(url=start_url, headers=headers)
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


def get_city(content):
    base_url = 'http://hotels.ctrip.com/'
    html = Selector(text=content)
    url_list = html.xpath('//*[@id="base_bd"]/dl/dd/a/@href').extract()
    city_url = []
    # r = RedisClient()
    # redis_key = "CtripCity:start_urls"

    for i in url_list:
        num = re.findall('(\d+)',i)
        city_url.append(num[0])
        # r.add_value(redis_key,num[0])
    return city_url


def start():
    cityList = 'http://hotels.ctrip.com/domestic-city-hotel.html'
    content = get_html_content(cityList)
    city_id = get_city(content)
    print(city_id)


if __name__ == '__main__':
    start()
