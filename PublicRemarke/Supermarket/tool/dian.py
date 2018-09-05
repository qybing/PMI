# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:58:50 2018

@author: jasonai
"""

import re
import time
import random
import requests
import pandas as pd
from pmipy import pmi
from pmipy import log
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

logger = log.createLogger(__name__)

ua = UserAgent()
basic_url = "http://www.dianping.com"
shopping_file = 'shopping_dianping.txt'

df_ip = pd.read_excel(r'IP.xlsx')
# 确保IP不重复
df_ip = df_ip.drop_duplicates()
ip_pool = df_ip['代理IP'].tolist()


def check_ip(ip):
    test_url = 'https://www.baidu.com/'
    proxy = {'http': ip}
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    try:
        response = requests.get(test_url, headers=headers, proxies=proxy, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def getHtmlOld(url):
    # 伪装请求头部
    # 有了Cookie不怕不让爬
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Cookie': '_lxsdk_cuid=15eea339434c8-0d2cff6b34e61c-c313760-100200-15eea339434c8; _lxsdk=15eea339434c8-0d2cff6b34e61c-c313760-100200-15eea339434c8; _hc.v=cec4c6d7-039d-1717-70c0-4234813c6e90.1507167802;\
            s_ViewType=1; __mta=218584358.1507168277959.1507176075960.1507176126471.5; JSESSIONID=48C46DCEFE3A390F647F52FED889020D; aburl=1; cy=2; cye=beijing; _lxsdk_s=15eea9307ab-17c-f87-123%7C%7C48',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': 'www.dianping.com'
    }
    html = requests.get(url, headers=headers).content
    # 转换编码
    html = html.decode('utf-8')
    return html


def getHtml(url):
    # 伪装请求头部
    # 有了Cookie不怕不让爬
    ip = random.choice(ip_pool)
    proxy = {'https': ip}
    # user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': ua.random}
    try:
        response = requests.get(url, headers=headers, proxies=proxy, timeout=5)
        if response.status_code == 200:
            text = response.content.decode('utf-8')
            # response.encoding = response.apparent_encoding
            return text
        else:
            logger.warning('{}访问时响应为：{}！'.format(ip, response.status_code))
            return getHtml(url)
    except:
        logger.warning('{}连接出错！'.format(ip))
        return getHtml(url)


# a=getHtml("http://www.dianping.com/shop/41476534")

def getStoreInfo(html):
    soup = BeautifulSoup(html, "lxml")
    infoDict = {}
    infoDictStr = re.findall(r'window.shop_config=({.*?})', html)[0]
    pattern = r'{}: ?"(.*?)",'
    res1 = soup.find('div', class_='brief-info')
    # 获取电话号码
    res2 = soup.find('p', class_='expand-info tel')
    try:
        # 获取基本信息
        infoDict['shopId'] = re.findall(pattern.format('shopId'), infoDictStr)[0]
        infoDict['shopName'] = re.findall(pattern.format('shopName'), infoDictStr)[0]
        infoDict['address'] = re.findall(pattern.format('address'), infoDictStr)[0]
        infoDict['fullName'] = re.findall(pattern.format('fullName'), infoDictStr)[0]
        infoDict['shopGlat'] = float(re.findall(pattern.format('shopGlat'), infoDictStr)[0])
        infoDict['shopGlng'] = float(re.findall(pattern.format('shopGlng'), infoDictStr)[0])
        infoDict['commentCount'] = re.findall(r'id="reviewCount">(.*?)</span>', str(res1))[0]
        infoDict['productScore'] = re.findall(r'产品:(.*?)</span>', str(res1))[0]
        infoDict['telephone'] = re.findall(r'</span> ?(.*?) ?<[a/]', str(res2))[0]
    except IndexError:
        infoDict['shopId'] = re.findall(r'window.shop_config.shopId=(.*?)', html)
        infoDict['fullName'] = re.findall(r'<h1 class="shop-name">\n? *(.*?)\n', html)[0]
        infoDict['shopName'] = infoDict['fullName'].split('(')[0]
        res = soup.find('span', itemprop="street-address")
        infoDict['address'] = res['title']
        ll = re.findall(r'{(lng:.*?)}', html)[0]
        ll = re.split(r'[:,]', ll)
        infoDict['shopGlng'] = float(ll[1])
        infoDict['shopGlat'] = float(ll[-1])
        infoDict['productScore'] = re.findall(r'效果:(.*?)</span>', str(res1))[0]
        try:
            infoDict['commentCount'] = re.findall(r'> ?(.*?条评论) ?</span>', str(res1))[0]
        except IndexError:
            infoDict['commentCount'] = '0条评论'
        try:
            infoDict['telephone'] = re.findall(r'</span> ?(.*?) ?<[a/]', str(res2))[0]
        except IndexError:
            infoDict['telephone'] = re.findall(r'itemprop="tel">(.*?)</span>', str(res2))[0]

    # 获取评论数、评分等信息
    infoDict['rankStars'] = re.findall(r'<span class="mid-rank-stars mid-str(.*?)"', str(res1))[0]
    infoDict['avgPrice'] = re.findall(r'消费:(.*?)</span>', str(res1))[0]
    infoDict['environmentScore'] = re.findall(r'环境:(.*?)</span>', str(res1))[0]
    infoDict['serviceScore'] = re.findall(r'服务:(.*?)</span>', str(res1))[0]

    # 获取营业状态--是否闭店
    if soup.find_all('p', class_='shop-closed'):
        infoDict['operatingStatus'] = 'open'
    else:
        infoDict['operatingStatus'] = 'shop-closed'
    return infoDict


def getPointInPage(soup):
    res = soup.find_all('a',
                        onclick=re.compile("'moduleClick', 'shopname'"))  # 或result = soup.find_all('div', class_='tit')
    for r in res:
        try:
            url = r['href']
            html = getHtml(url)
            infoDict = getStoreInfo(html)
            coll.insert_one(infoDict)
            logger.info('“{}”商铺信息更新成功！'.format(infoDict['fullName']))
        except Exception as e:
            cont = re.findall(r'.*(..无法访问)', str(soup))
            if cont:
                logger.warning(cont[0])
            logger.warning('“{}”地址无法爬取！，报错信息为：{}'.format(url, e))


def getSuperCVS(city):
    sp_url = "http://www.dianping.com/{}/ch20/g187".format(city)
    html = getHtml(sp_url)
    soup = BeautifulSoup(html, "lxml")
    result = soup.find('div', id='region-nav')
    result2 = result.find_all('a')
    # 按区爬取
    for r in result2:
        url = r['href']
        html = getHtml(url)
        soup = BeautifulSoup(html, "lxml")
        res1 = soup.find('div', id='region-nav-sub')
        res2 = res1.find_all('a')
        # 按商圈爬取
        for r2 in res2[1:]:  # 去除“不限”
            time.sleep(random.random())
            url2 = r2['href']
            html2 = getHtml(url2)
            soup2 = BeautifulSoup(html2, "lxml")
            getPointInPage(soup2)
            page = soup2.find('div', class_="page")
            if page:
                nextPage = page.find('a', title="下一页")
                if nextPage:
                    nextUrl = nextPage['href']
                    nextHtml = getHtml(nextUrl)
                    nextSoup = BeautifulSoup(nextHtml, "lxml")
                    getPointInPage(nextSoup)


if __name__ == '__main__':
    import sys

    city = sys.argv[1]
    testDB = 'ClaudiusTest'
    collection = city
    client16 = pmi.connOcm16()
    coll = client16[testDB][collection]
    getSuperCVS(city)
    # getHtml("http://www.dianping.com/nanjing/ch20/g187")

"""
# 获取并存储超市/便利店信息（id, name）
def getHotelInfo(shopping_file):
    # 网站上显示酒店页面有50页，事实上，只能爬取13页，之后的页面为空
    for i in range(1, 51):
        html = download_page(sp_url)
        soup = BeautifulSoup(html, "lxml")
        result = soup.find_all(attrs={"title":cate})
        if len(result) == 1:
            aim_url = basic_url + result[0]['href']
        else:
            raise SystemError('<%s>标签不唯一！'%cate)


        # 如："action": "click","content":"/shop/8025450","title":"速8酒店"
        re_result = re.compile(r'<a href=(.*)alt="超市/便利店" title="超市/便利店"(.*);">超市/便利店</a>').findall(page)
        txt = ""
        for x in re_result:
            txt += x[0] # /shop/(/d)+格式
            txt += ' ' + x[1] # 酒店名称
            txt += "\n"
        writeToFile(hotel_file, txt)
        print("第%d页OK....." % i)
        i += 1
        # 下一页的网址
        aim_url = "http://www.dianping.com/beijing/hotel/p" + str(i)

# 往文件中写content
def writeToFile(file_name, content):
    with open(file_name, 'a+', encoding='utf-8') as fp:
        fp.write(content)

# 获取每个评论页的所有评论
def getScore(page):
    # 对于评分需要使用BeautifulSoup，直接使用正则表达式无法判断数据是哪个用户的
    score_list = []
    soup = BeautifulSoup(page, 'html.parser')
    comment_rst_list = soup.find_all('div', attrs = {'class': 'comment-rst'})
    # 对于各个用户的评论
    for comment_rst in comment_rst_list:
        rst_list = comment_rst.find_all('span', attrs={'class': 'rst'})
        # 记录某个用户的各项评分，默认为零，前五项分别是房间、位置、服务、卫生和设施，最后一项为冗余项。
        single_score_dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
        # 对于各个类型的评论
        for rst in rst_list:
            comment = rst.getText()
            type_ = comment[:2]
            score = comment[2]
            if type_ == "房间":
                single_score_dic[0] = score
            elif type_ == "位置":
                single_score_dic[1] = score
            elif type_ == "服务":
                single_score_dic[2] = score
            elif type_ == "卫生":
                single_score_dic[3] = score
            elif type_ == "设施":
                single_score_dic[4] = score
            else:
                single_score_dic[5] = score
        score_list.append(single_score_dic)
    return score_list

# 中文字符和英文、数字占用的空间不同，为了输出显示友好，user_name不能简单的以%30s格式输出
def setProperFormat(user_name):
    re_result = re.compile(r'(\d|[A-Z]|[a-z]|\_)').findall(user_name)
    len_eng = len(re_result)
    total_len = len(user_name)
    len_cha = total_len - len_eng
    real_len = len_eng + len_cha * 2
    blank_len = 30 - real_len
    txt = "%s" % (" " * blank_len + user_name)
    return txt

# 获取每一条评论
def getEveryComment(hotel_file):
    # 打开hotel_file文件
    with open(hotel_file, 'r', encoding='utf-8') as fp:
        num_hotel = 1
        # 对于每家酒店
        for line in fp:
            # 获取酒店url, id和name
            hotel_url = line.split(' ')[0]
            hotel_name = line.split(' ')[1][:-1] # 去掉最后的'\n'
            hotel_id = hotel_url.split('/')[2]
            # 设置存储用户评论的文件的文件名
            store_file = "%s_%scomments.txt" % (hotel_id, hotel_name)
            # 存入header
            txt = "%12s%12s%30s%15s%15s%15s%15s%15s%15s\n" % ("hotel_id", "user_id", "user_name", "rate_room", "rate_position", "rate_service", "rate_health", "rate_facility", "rate_others")
            writeToFile(store_file, txt)
            # 获取评论页url
            business_url = basic_url + hotel_url + '/review_more'
            page = download_page(business_url)
            # 计算出评论页数
            total_comments = re.compile(r'全部</a><em class="col-exp">\((\d+)\)</em>', re.DOTALL).findall(page)
            print(total_comments)
            pages = int(int(total_comments[0]) / 20) + 1
            # 对于每一页的评论
            for n in range(1, pages+1):
                comment_url = business_url + '?pageno=%s' % n
                print(comment_url)
                page = download_page(comment_url)
                # 如：<a target="_blank" title="" href="/member/1158824000">HpointK</a>
                # (id, userName)
                user_info = re.compile(r'<a target="_blank" title="" href="/member/(\d+)">(.*?)</a>', re.DOTALL).findall(page)
                score_list = getScore(page)
                txt = ""
                try:
                    for i, info in enumerate(user_info):
                        txt += "%12s%12s" % (hotel_id, info[0])
                        txt += setProperFormat(info[1])
                        txt += "%15s%15s%15s%15s%15s%15s\n" % (score_list[i][0], score_list[i][1], score_list[i][2], score_list[i][3], score_list[i][4], score_list[i][5])
                except  Exception as e:
                    print(e)
                    print(len(user_info))
                    break
                # 每次往文件中写网页中的评论
                writeToFile(store_file, txt)
                print("第%d页已存储，共%d页" % (n, pages))
                break
            print("第%s家酒店的评论已存储", num_hotel)
            num_hotel += 1
            break

getHotelInfo(hotel_file)
getEveryComment(hotel_file)
"""