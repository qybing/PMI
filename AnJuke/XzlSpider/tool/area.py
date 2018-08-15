import requests

from fake_useragent import UserAgent
from parsel import Selector

ua = UserAgent()
agent = ua.random
headers = {
    'User-Agent':agent
}
res = requests.get('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html',headers=headers).content
html = res.decode('gbk')
xpath_css = Selector(text=html)
all_urls = xpath_css.xpath('//tr[@class="provincetr"]/td/a')
urls_city = []
dict = {}
base = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
for url in all_urls:
    province_url = base+url.xpath('./@href').extract_first()
    province = url.xpath('./text()').extract_first()
    res = requests.get(province_url, headers=headers).content
    html = res.decode('gbk')
    xpath_css = Selector(text=html)
    city_code = xpath_css.xpath('//tr[@class="citytr"]/td[1]/a/text()').extract()
    city_list = xpath_css.xpath('//tr[@class="citytr"]/td[2]/a/text()').extract()

    print(province,city_list)