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
    urls_city.append((base+url.xpath('./@href').extract_first(),url.xpath('./text()').extract_first()))

# for url in urls_city:
# print(urls_city)