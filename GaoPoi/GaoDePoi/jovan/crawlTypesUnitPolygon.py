# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:25:59 2018

@author: jasonai
"""

"""
通过高德地图爬取POI数据-分割中国地块
由于高德矩形获取POI智能返回10000条数据，
所以将中国地图版块分割成小与1000的矩形框
"""

import os
from pmipy.support import APIkeys
from threading import Thread
from random import choice
from pmipy import pmi
from pmipy import log
import numpy as np
import pandas as pd
import requests


GDkeys = APIkeys.GDkeysList3

logger = log.createLogger(__name__)
logger2 = log.createLogger("types_polygon失败记录")
codePath2 = 'GaodeCode_python.xlsx'
maxDocCounts = 850
storeFile = 'polygon_{}'.format(maxDocCounts)
if not os.path.exists(storeFile):
    os.mkdir(storeFile)

# 获取最小矩形框
class Rect:
    def __init__(self,xmin,ymin,xmax,ymax):
        self.xmin=xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax


class GetUnitPolygon(object):
    def __init__(self, types, maxDocCounts):
        # POI分类
        self.types = types
        # 最大记录条数
        self.maxDocCounts = maxDocCounts
        self.url = "http://restapi.amap.com/v3/place/polygon?"
        self.unitPloygon = []

    #切分地块
    def CutChina(self,rect):
        # 规则：经度和纬度用","分割，经度在前，纬度在后，坐标对用"|"分割。经纬度小数点后不得超过6位。
        polygon = "{:.6f},{:.6f}|{:.6f},{:.6f}".format(rect.xmin,rect.ymin,rect.xmax,rect.ymax)
        params = {'polygon':polygon, 'types':self.types, 'offset':3}
        count=self.getDocCounts(params)
        if count != 'fail':
            if count < self.maxDocCounts:
                self.unitPloygon.append([self.types, polygon, count])
                print("{}-[{}]的记录条数为：{}".format(self.types,polygon, count))
            else:
                middleX=(rect.xmin + rect.xmax) / 2
                middleY = (rect.ymin + rect.ymax) / 2
                rect1 = Rect(xmin=rect.xmin, ymin=rect.ymin, xmax=middleX, ymax=middleY)
                rect2 = Rect(xmin=middleX, ymin=rect.ymin, xmax=rect.xmax, ymax=middleY)
                rect3 = Rect(xmin=rect.xmin, ymin=middleY, xmax=middleX, ymax=rect.ymax)
                rect4 = Rect(xmin=middleX, ymin=middleY, xmax=rect.xmax, ymax=rect.ymax)
                #使用递归调用
                self.CutChina(rect=rect1)
                self.CutChina(rect=rect2)
                self.CutChina(rect=rect3)
                self.CutChina(rect=rect4)

        else:
            logger2.warning('"{}-{}"遇到错误，请调试后重新执行程序！'.format(self.types, polygon))

    # 获取记录条数
    @pmi.checkResult(keyword='fail', loopTime=30) 
    def getDocCounts(self, params, page=1):
        params['page'] = page
        params['key'] = choice(GDkeys)
        try:
            result = requests.get(url=self.url, params=params, timeout=10).json()
            if result['status'] == '1':
                result = int(result['count'])
            else:
                logger.warning('"{}-{}-{}"请求state为0，info为:{}!'.format(self.types,params['polygon'],page,result['info']))
                result = 'fail'
        except Exception as e:
            logger2.warning('"{}-{}-{}"错误信息为:{}!'.format(self.types,params['polygon'],page,e))
            result = 'fail'
        return result


def run_thread(df, colName):
    rect=Rect(xmin=71.234018,ymin=17.725738,xmax=136.139681,ymax=55.28893)
    for t in df[colName]:
        cut = GetUnitPolygon(t, maxDocCounts)
        cut.CutChina(rect)
        # 存储文件
        df2 = pd.DataFrame(cut.unitPloygon, columns=['types','polyygon','count'])
        #df2.to_csv('{}/{}_polygon.csv'.format(storeFile, t), index=False)
        df2.to_csv('{}/{}_polygon.csv'.format(storeFile, t), index=False)
    return

# 多线程
class MyThread(Thread):
    def __init__(self, df, arg1):
        Thread.__init__(self)
        self.df = df
        self.arg1 = arg1

    def run(self):
        self.result = run_thread(self.df, self.arg1)

    def get_result(self):
        return self.result
    

def storeTypePoly(df_split):
    # 构建多线程
    thd_list = []
    for df in df_split:
        thd = MyThread(df, 'NEW_TYPE')
        thd.start()
        thd_list.append(thd)
    
    for t in thd_list: # 等待所有线程执行完毕
        t.join()
    
    #res_list = []
    for t in thd_list:
        t.get_result()
        # print(t.get_result())
        #res_list.extend(res)
    #return res_list
    
def main(thread=10):
    #client = pmi.connOcm16()
    #coll = client['Gaode']['Gaode_180727']
    df_type = pd.read_excel(codePath2, sheetname='POI分类与编码（二级）',dtype={'NEW_TYPE':'str'})
    # df_type = df_type[df_type['state'].isnull()]
    isList = os.listdir(storeFile)
    if isList:
        isList = [i.split('_')[0] for i in isList]
        df_type = df_type[~df_type['NEW_TYPE'].isin(isList)]
    
    thread = min(thread, len(df_type))
    df_split = np.array_split(df_type, thread)
    storeTypePoly(df_split)

    

if __name__== "__main__":
    main(thread=50)
    print('程序结束！')
    
    
    """
    cut = GetUnitPolygon()
    #开始分割中国区域
    rect=Rect(xmin=71.234018,ymin=17.725738,xmax=136.139681,ymax=55.28893)
    cut.CutChina(rect)
    # 存储文件
    df = pd.DataFrame(cut.unitPloygon, columns=['ploygon','count'])
    df.to_excel('爬取高德POI的最小polygon.xlsx',index=False)
    print("程序完成结束")"""
    