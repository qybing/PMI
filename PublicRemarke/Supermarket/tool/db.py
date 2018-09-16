import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('Shop:start_urls')
    pool = redis.ConnectionPool(host='localhost', port=6379, db=2, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    count = 0
    for i in n:
        a = r.sadd('Shop:start_urls',i)
        if a==1:
            count+=1
        else:
            print('失败')
    print(count)


if __name__ == '__main__':
    redis_client()