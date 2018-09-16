import random
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
driver_path = r'E:\ch\chromedriver.exe'


def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0

    while current < distance:
        if current < mid:
            # 加速度为正2
            a = 2
        else:
            # 加速度为负3
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track



url = ['http://www.dianping.com/shop/4019176',
       'http://www.dianping.com/shop/113265998',
       'http://www.dianping.com/shop/109280504',
       'http://www.dianping.com/shop/103332194',
       'http://www.dianping.com/shop/33220812',
       'http://www.dianping.com/shop/19591435',
       'http://www.dianping.com/shop/15192989']
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://www.dianping.com/shanghai/ch20/g187o2')
sleep(7)
driver.find_element_by_xpath('//*[@id="shop-all-list"]/ul/li[1]/div[2]/div[1]/a[1]/h4').click()
print(driver.current_url)
# driver.get(random.choice(url))
sleep(4)
try:
    div = driver.find_element_by_id("yodaBox")
    is_present = True
except:
    is_present = False
if True:
    tracks = get_track(200)
    ActionChains(driver).click_and_hold(on_element=div).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    sleep(0.5)
    ActionChains(driver).release().perform()
    # sleep(0.15)
    # ActionChains(driver).move_to_element_with_offset(to_element=div, xoffset=30, yoffset=0).perform()
    # sleep(0.15)
    # ActionChains(driver).move_to_element_with_offset(to_element=div, xoffset=100, yoffset=0).perform()
    # ActionChains(driver).move_to_element_with_offset(to_element=div, xoffset=200, yoffset=50).release().perform()
    sleep(20)
    driver.close()
else:
    print('没有到验证码页面')
