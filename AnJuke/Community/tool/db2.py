import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=4, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('DetailHouse:start_urls')
    pool = redis.ConnectionPool(host='localhost', port=6379, db=5, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    count = 0
    for i in n:
        # if i == 'https://bj.xzl.anjuke.com/zu/yizhuang-p31/':
        #     print('找到了')
        # else:
        #     print(i)


        # print(i)
        # if i == 'https://zs.sp.anjuke.com/shou/zhangjiabian/':
        #     # print(i)
        #     print('找-到：{}'.format(i))
        # else:
        #     pass
            # print('没找到：{}'.format(i))
        # if count==30:
        #     break
        # if count==10000000:
        #     break
        a = r.sadd('DetailHouse:start_urls',i)

        if a == 1:
            count += 1
            print('成功')
        else:
            print('已经存在')
    print('一共完成{}'.format(count))

def xiugai_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=4, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('special:start_urls')
    count = 0
    for i in n:
        if i == r'https://guangzhou.anjuke.com/community/foshanf/':
            for x in range(1,5):
                c = r.sadd('HouseList:start_urls',i+'y{}'.format(x))
                if c == 1:
                    count+=1
            print('删除成功', count)
        else:
            a = ['m1','m2','m3','m4','m5','m6','m8',]
            for y in a:
                d = r.sadd('HouseList:start_urls', i + y)
                if d == 1:
                    count += 1
            print('删除成功', count)


if __name__ == '__main__':
    xiugai_client()
    # redis_client()