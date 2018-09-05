from time import sleep

import redis


def redis_client():
    while True:
        pool = redis.ConnectionPool(host='localhost', port=6379, db=4, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        n = r.smembers('ShopList:dupefilter')
        for i in n:
            r.srem('ShopList:dupefilter', i)
            print('删除成功')
        print('休息5秒')
        sleep(5)

if __name__ == '__main__':
    redis_client()