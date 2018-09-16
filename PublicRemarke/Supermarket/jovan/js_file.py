import random

import execjs
import os
from fake_useragent import UserAgent


def get_lxsdk_s():
    a = random.randint(4, 50)
    node = execjs.get()
    js_file_path = os.path.join(os.path.dirname(__file__), 'dianping2.js')
    jsctx = node.compile(open(js_file_path, encoding='UTF-8').read())
    js = 'res()'
    lxsdk_s = jsctx.eval(js) + '%7C%7C{}'.format(a)
    return lxsdk_s


def get_lxsdk_cuid(useragent):
    node = execjs.get()
    js_file_path = os.path.join(os.path.dirname(__file__), 'pinglun.js')
    jsctx = node.compile(open(js_file_path, encoding='UTF-8').read())
    fenbianlv = [(1080, 1920), (768, 1366), (900, 1440), (900, 1600), (768, 1024), (1024, 1280)]
    params = random.choice(fenbianlv)
    # print(params[0],params[1])
    # ua = UserAgent()
    # agent = ua.random
    # useragent = agent
    # print(useragent)
    js = 'Or("{0}","{1}","{2}")'.format(params[0], params[1], useragent)
    lxsdk_cuid = jsctx.eval(js)
    return lxsdk_cuid


def get_hc():
    a = random.randint(12, 50)
    node = execjs.get()
    js_file_path = os.path.join(os.path.dirname(__file__), 'pingdian_hc.js')
    jsctx = node.compile(open(js_file_path, encoding='UTF-8').read())
    js = 'Ti()'
    hc_ = jsctx.eval(js)
    return hc_

def get_ver():
    node = execjs.get()
    js_file_path = os.path.join(os.path.dirname(__file__), 'dianping.js')
    jsctx = node.compile(open(js_file_path, encoding='utf-8').read())
    request_code = '4537075565804dcfb8d58c9d544bcb35'
    js = 'getCaptchaUrl("{0}")'.format(request_code)
    a = jsctx.eval(js)
    print(a)
    # return lxsdk_cuid


if __name__ == '__main__':
    # useragent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    # same = get_lxsdk_cuid(useragent)
    # cook = '_lxsdk_cuid={}; _lxsdk={}; _hc.v={}; _lxsdk_s={}'.format(
    #     same, same, get_hc(), get_lxsdk_s())
    # cook1 = 'cy=1236; cityid=1236; cye=huixian; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=165c6b8e911c8-0383cc5ec3114e-37664109-144000-165c6b8e91289; _lxsdk=165c6b8e911c8-0383cc5ec3114e-37664109-144000-165c6b8e91289; _hc.v=0c84e8b5-c945-5c86-bb54-94e4936012e5.1536637332; s_ViewType=10; cye=beijing; _lxsdk_s=165cb7d7e23-268-18-f1%7C%7C87'
    # print(cook)
    # get_lxsdk_cuid(useragent)
    # print(get_lxsdk_s())

    get_ver()