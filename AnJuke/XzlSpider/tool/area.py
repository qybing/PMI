import chardet
import pymongo
from time import sleep

import pymysql
import requests

from fake_useragent import UserAgent
from parsel import Selector

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['China']
p = db['area']

def get_html_content(start_url):
    for tries in range(5):
        ua = UserAgent()
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
            if res.status_code == 200:
                return res.content
        except:
            if tries < (5 - 1):
                sleep(tries + 1)  # hava a rest
                print('retry:' + start_url)
                continue
            else:
                print('没有获取到网页数据')
                return ''


def main():
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
    res = get_html_content(url)
    enc = chardet.detect(res)
    html = res.decode(enc['encoding'],errors = 'ignore')
    xpath_css = Selector(text=html)
    all_urls = xpath_css.xpath('//tr[@class="provincetr"]/td/a')
    base = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    # print(len(all_urls))
    for url in all_urls[22:24]:
        province_url = base + url.xpath('./@href').extract_first()
        province = url.xpath('./text()').extract_first()
        res = get_html_content(province_url)
        enc = chardet.detect(res)
        html = res.decode(enc['encoding'],errors = 'ignore')
        xpath_css = Selector(text=html)
        city_code = xpath_css.xpath('//tr[@class="citytr"]/td[1]/a/text()').extract()
        city_list = xpath_css.xpath('//tr[@class="citytr"]/td[2]/a/text()').extract()
        city_urls = xpath_css.xpath('//tr[@class="citytr"]/td[1]/a/@href').extract()
        for i in range(len(city_urls)):
            url1 = base + city_urls[i]
            res = get_html_content(url1)
            enc = chardet.detect(res)
            html = res.decode(enc['encoding'],errors = 'ignore')
            xpath_css = Selector(text=html)
            county_code = xpath_css.xpath('//tr[@class="countytr"]/td[1]/a/text()').extract()
            county_list = xpath_css.xpath('//tr[@class="countytr"]/td[2]/a/text()').extract()
            county_urls = xpath_css.xpath('//tr[@class="countytr"]/td[1]/a/@href').extract()
            for j in range(len(county_urls)):
                # print('省：{}--市：{}--县：{}'.format(province,city_list[i],county_list[j]))
                url2 = url1[0:-9]+county_urls[j]
                res = get_html_content(url2)
                enc = chardet.detect(res)
                html = res.decode(enc['encoding'],errors = 'ignore')
                xpath_css = Selector(text=html)
                town_code = xpath_css.xpath('//tr[@class="towntr"]/td[1]/a/text()').extract()
                town_list = xpath_css.xpath('//tr[@class="towntr"]/td[2]/a/text()').extract()
                town_urls = xpath_css.xpath('//tr[@class="towntr"]/td[1]/a/@href').extract()
                for k in range(len(town_urls)):
                    # print('省：{}--市：{}--县：{}--镇：{}'.format(province,city_list[i],county_list[j],town_list[k]))
                    url3 = url2[0:-11] + town_urls[k]
                    print(url3)
                    res = get_html_content(url3)
                    enc = chardet.detect(res)
                    html = res.decode(enc['encoding'],errors = 'ignore')
                    xpath_css = Selector(text=html)
                    villagetr_code = xpath_css.xpath('//tr[@class="villagetr"]/td[1]/text()').extract()
                    villagetr_code1 = xpath_css.xpath('//tr[@class="villagetr"]/td[2]/text()').extract()
                    villagetr_list = xpath_css.xpath('//tr[@class="villagetr"]/td[3]/text()').extract()
                    for x in range(len(villagetr_list)):
                        print('省：{}  市：{}  县：{}  镇：{}  村：{}'.format(province, str(city_list[i]).replace('市辖区',province)+'--'+city_code[i],
                                                                    county_list[j]+'--'+county_code[j],
                                                                    town_list[k]+'--'+town_code[k],
                                                                    villagetr_list[x]+'--'+villagetr_code[x]+'--'+villagetr_code1[x]))
                        save_to_mysql(province, str(city_list[i]).replace('市辖区',province)+'--'+city_code[i],
                                                                    county_list[j]+'--'+county_code[j],
                                                                    town_list[k]+'--'+town_code[k],
                                                                    villagetr_list[x]+'--'+villagetr_code[x]+'--'+villagetr_code1[x])
def save_to_mysql(province,city,county,town,village):

    data = {
        'province': province,
        'city': city,
        'county': county,
        'town':town,
        'village':village
    }
    p.update({'village': data['village']}, {'$set': dict(data)}, True)
    print('成功')
def start():
    # url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/42/06/84/420684103.html'
    # res = get_html_content(url)
    # enc = chardet.detect(res)
    # print(enc)
    # html = res.decode(enc['encoding'],errors = 'ignore')
    # print(html)
    a = [1,2,3,4,5,6]
    print(a[0:1])
    print(a[1:2])

if __name__ == '__main__':
    # a = {}
    main()
    # start()

