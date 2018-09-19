# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:57:54 2018

@author: jasonai
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
import math


blankLoop = 5

logger = log.createLogger(__name__)
logger2 = log.createLogger("crawlGDPOIbyPoly空值问题(2)_循环%s" % blankLoop)
#logger3 = log.createLogger("crawlGDPOIbyPoly爬取成功率")

# 数据库
dbName = 'GDPOI_poly180729'
client = pmi.connOcm16()


GDkeys = APIkeys.GDkeysList3
GDkeys.extend(APIkeys.GDkeysList)
GDkeys.extend(APIkeys.GDkeysList2)
maxDoc = 20
params = {'offset':maxDoc,'extensions':'base'}
url_poly = "http://restapi.amap.com/v3/place/polygon?"

maxDocCounts = 850
storeFile = 'polygon_{}'.format(maxDocCounts)
AllUnitPolyFile = 'AllUnitPolygon_{}.csv'.format(maxDocCounts)


def combineUnitPolygon(storeFile):
    dfList = []
    for file in os.listdir(storeFile):
        df = pd.read_csv(os.path.join(storeFile, file), engine='python', dtype={'types':'str'})
        dfList.append(df)
    df_c = pd.concat(dfList)
    return df_c


def getAllUnitPolygon(storeFile):
    if os.path.exists(AllUnitPolyFile):
        df = pd.read_csv(AllUnitPolyFile, engine='python', dtype={'types':'str'})
    else:
        df = combineUnitPolygon(storeFile)
        # 去除count为0的Unit
        df = df[df['count']!=0]
        df = df.rename(columns={'polyygon':'polygon'})
        df.to_csv(AllUnitPolyFile,index=False)
    return df


def crawlTypeUnitPoly(types, poly, count):
    @pmi.checkResult(keyword='blank', loopTime=blankLoop)
    @pmi.checkResult(keyword='fail', loopTime=15) 
    def crawlPage(page):
        params['page'] = page
        params['key'] = choice(GDkeys)
        try:
            result = requests.get(url=url_poly, params=params,timeout=15).json()
            if result['status'] == '1':
                res = result['pois']
                if res:
                    return res
                else:
                    logger2.info('"{}-{}-{}/{}"：还没到最后一页已经遇到空值!'.format(types,poly,page,maxPage))
                    return 'blank'
            else:
                logger.warning('"{}-{}-{}"请求state为0，info为:{}!'.format(types,
                               params['polygon'],page,result['info']))
                return 'fail'
        except Exception as e:
            logger.warning('"{}-{}-{}"错误信息为:{}!'.format(types,params['polygon'],page,e))
            return 'fail'

    params['polygon'] = poly
    params['types'] = types
    maxPage = math.ceil(count/maxDoc)
    result = []
    for p in range(1, maxPage+1):
        res = crawlPage(p)
        if isinstance(res, list):
            result.extend(res)
    return result


def run_thread(df, df_typoly):
    # types的数据量 <==> 集合
    for t in df:
        dt = df_typoly[df_typoly['types']==t]
        result = []
        for poly, count in dt[['polygon','count']].values:
            res = crawlTypeUnitPoly(t, poly, count)
            result.extend(res)

        # 以types为最小单元，将数据上传至MongoDB
        @pmi.checkResult(keyword='fail', loopTime=3)
        def uploadDB():
            logger.info('POI类别"{}"上传至MongoDB的{}数据库...'.format(t,dbName))
            coll = client[dbName][t]
            try:
                coll.insert_many(result)
                return 'succ'
            except Exception as e:
                logger.error('类别"{}"的所属数据上传时出错:{}'.format(t,e))
                return 'fail'  
        uploadDB()

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
    

def existCollectList():
    # client = pmi.connOcm16(False)
    CollectList = client[dbName].collection_names()
    return CollectList
    
def main(storeFile, thread=20):
    df_typoly = getAllUnitPolygon(storeFile)
    df_type = df_typoly.groupby('types',as_index=False).sum()
    df_type = df_type.sort_values('count')
    df_type = df_type['types'].head(int(len(df_type)*0.8)) # 取前80%
    # 获取已经存在的集合名单，然后在df_type中排除
    CollectList = existCollectList()
    df_type = df_type[~df_type.isin(CollectList)]
    # 随机打乱
    df_type = df_type.sample(frac=1)
    # 构建多线程
    df_split= np.array_split(df_type, thread)
    thd_list = []
    for df in df_split:
        thd = MyThread(df, df_typoly)
        thd.start()
        thd_list.append(thd)
    
    for t in thd_list: # 等待所有线程执行完毕
        t.join()
    
    for t in thd_list:
        t.get_result()


# 当小types爬完，只留下超大时types使用！
def run_thread2(df, cols):
    result = []
    for types, poly, count in df[cols].values:
        res = crawlTypeUnitPoly(types, poly, count)
        result.extend(res)
    return result

# 多线程
class MyThread2(Thread):
    def __init__(self, df, arg1):
        Thread.__init__(self)
        self.df = df
        self.arg1 = arg1

    def run(self):
        self.result = run_thread2(self.df, self.arg1)

    def get_result(self):
        return self.result
    

def main2(storeFile, thread=20, tylist=[]):
    df_typoly = getAllUnitPolygon(storeFile)
    df_type = df_typoly.groupby('types',as_index=False).sum()
    df_type = df_type.sort_values('count')
    # 指定types进行更新，如指定的types已存在，则选择覆盖原数据
    if tylist:
        logger.info('指定types{}进行更新，如指定的types已存在，则选择覆盖原数据...'.format(tylist))
        df_type = df_type[df_type['types'].isin(tylist)]
    else:
        # 获取已经存在的集合名单，然后在df_type中排除
        CollectList = existCollectList()
        df_type = df_type[~df_type['types'].isin(CollectList)]
    # 随机打乱
    # df_type = df_type.sample(frac=1)
    # types的数据量 <==> 集合
    for ty in df_type['types']:
        result = []  # 早点释放内存
        dt = df_typoly[df_typoly['types']==ty]
        thread = min(thread, len(dt))  # 两者取小的
        # 构建多线程
        df_split= np.array_split(dt, thread)
        thd_list = []
        for df in df_split:
            thd = MyThread2(df, arg1=['types', 'polygon', 'count'])
            thd.start()
            thd_list.append(thd)
        
        for t in thd_list: # 等待所有线程执行完毕
            t.join()
        
        for t in thd_list:
            result.extend(t.get_result())
        
        # 以types为最小单元，将数据上传至MongoDB
        @pmi.checkResult(keyword='fail', loopTime=3)
        def uploadDB():
            logger.info('POI类别"{}"上传至MongoDB的{}数据库...'.format(ty,dbName))
            coll = client[dbName][ty]
            try:
                coll.insert_many(result)
                return 'succ'
            except Exception as e:
                logger.error('类别"{}"的所属数据上传时出错:{}'.format(ty,e))
                return 'fail'
        count = df_type[df_type['types']==ty]['count'].iloc[0]
        crawlcount = len(result)
        logger.info('"{}"总数据量为{}条，成功抓取{}条，爬取成功率为{:.2f}'.format(ty,
                     count, crawlcount, crawlcount/count))
        uploadDB()


if __name__== "__main__":
    #main(storeFile, thread=120)
    #tylist = ['060400','060401','060402','060403','060404','060405','060406',
    #'060407','060408','060409','060411','060413','060414','060415']
    main2(storeFile, thread=180)