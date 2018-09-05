from pymongo import MongoClient
import copy
import time

# 连接OCM1.6
def connOcm16(LAN=True):
    IP_LAN = '192.168.0.21:27017'
    IP_PN = 'www.parramountain.com:47017'
    IP = IP_LAN if LAN else IP_PN
    uri = 'mongodb://laocheng:laocheng@{0}'.format(IP)
    client = MongoClient(uri)
    return client


class MyMongoOperator(object):
    def __init__(self,):
        self.client = connOcm16()

    # 指定数据库和集合
    def connect2DB_COLL(self, dbname, collection):
        self.collection = self.client[dbname][collection]
        return self.collection

    def find(self, *args, **kwargs):
        return self.collection.find(*args, **kwargs)

    def findOne(self, query):
        return self.collection.find_one(query)

    def closeConn(self):
        self.client.close()


def getEWSN(lv1Name=None, lv2Name=None, lv3Name=None):
        '''
        获得指定地区的临界坐标, 全为None则返回中国的临界坐标,此函数只是为了得到中国最东南西北的经纬度
        :param lv1Name: 省
        :param lv2Name: 市
        :param lv3Name: 区
        :return: (e,w,s,n) 边界经纬度
        '''
        mongo = MyMongoOperator()
        mongo.connect2DB_COLL(dbname='Claudius', collection='GeoBoundary')
        result = mongo.find({"lv1Name": lv1Name, "lv2Name": lv2Name, "lv3Name": lv3Name}, {'boundaries': 1})
        try:
            each = result.__next__()
            each = each['boundaries']
            # 经度
            e_lng = map(lambda item: float(item['lng']), each)
            w_lng = copy.deepcopy(e_lng)
            # 纬度
            s_lat = map(lambda item: float(item['lat']), each)
            n_lat = copy.deepcopy(s_lat)
            e = max(e_lng)  # 东
            w = min(w_lng)  # 西
            s = min(s_lat)  # 南
            n = max(n_lat)  # 北
        except:
            raise
        finally:
            mongo.closeConn()
        return e, w, s, n


def getMatrix(meters=1000):
        '''
        对全国进行划分
        :param meters: 网格宽度,默认是一公里
        :return: 格子
        '''
        e, w, s, n = getEWSN()
        # 以上海作為長寬的基準距離(不同經緯度的長寬其實不同)
        width = 0.00001 * meters  # 即1网格宽度（米）转化为经度
        height = 0.000009 * meters

        def TernaryOperator(op1, op2, refer, res1, res2):
            if op1 % op2 > refer:
                return res1
            else:
                return res2

        lngSize = int((e - w) / width) + TernaryOperator((e - w), width, 0, 1, 0) + 1 # 计算横向的网格数
        latSize = int((n - s) / height) + TernaryOperator((n - s), height, 0, 1, 0) + 1 # lngSize*latSize = 24278280

        lngs = []
        for i in range(lngSize):
            lngs.append(w + (i * width))
        lats = []
        for i in range(latSize):
            lats.append(s + (i * height))

        return lngs, lats





def getTileName(lng, lat):
        '''
        根据经纬度获得tileName
        :param lng: 经度
        :param lat: 纬度
        :return: 成功: tileName
                 失败: None
        '''

        if not isinstance(lng, float) or not isinstance(lat, float):
            # logger.warning("{}或{}不是数值型，将返回空值！".format(lng,lat)) # raise TypeError('lng or lat must "float"')
            print("*"*30)
            return ''
        # if not hasattr('lngs'):
        #     raise AttributeError("'{}' object has no attribute '{}'".format('LatLng', 'lngs'))
        # if not hasattr('lats'):
        #     raise AttributeError("'{}' object has no attribute '{}'".format('LatLng', 'lats'))

        for i in range(len(lngs) - 1):  # 0-9,只遍历0-8
            if lngs[i] <= lng and lng < lngs[i + 1]:
                for j in range(len(lats) - 1):
                    if lats[j] <= lat and lat < lats[j + 1]:
                        return '{}-{}'.format(i, j)


input_file = open(r"test.csv", 'r', encoding='utf-8')
output_file = open(r"旺旺需求_result.txt", 'a+', encoding='utf-8')
lngs, lats = getMatrix()
# print(len(input_file.readlines()[1:]))
# print(lngs)
for line in input_file.readlines()[1:]:
    # time.sleep(1)
    # a = line.split(',')
    # print(float(a[1].replace('"','')))
    # print(float(a[1].replace('\t','')))

    try:
        # time.sleep(1)
        bd_lon = float(line.split(',')[1].replace('"',''))
        bd_lat = float(line.split(',')[2].replace('"',''))
        # print(bd_lat)
        # print(bd_lon)
        result = getTileName(bd_lon, bd_lat)
        print(result)
        # print(bd_lon)
        # print(bd_lat)
        # print(line)
        # result = bd09_to_gcj02(bd_lon, bd_lat)
        output_file.write(result + '\n')
        print('写进去了')
        # print(result)
        # print(line.split()[0] + '\t' + str(result[1]) + '\t' + str(result[0]) + '\n')
    except:
        # time.sleep(1)
        print(line)
        output_file.write(line)
        print('抱错')
        # print(line)
# bd_lon = 117.0364843
# bd_lat = 30.10799597


# var = getEWSN()
# var = getMatrix()
# var = getTileName(117.03100006683525, 30.100999791739635)
# print(var)

