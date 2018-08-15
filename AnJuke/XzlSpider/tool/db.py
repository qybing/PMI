import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('XinPan_spider:start_urls')
    pool = redis.ConnectionPool(host='localhost', port=6379, db=8, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    count = 0
    for i in n:
        # if count==30:
        #     break
        r.sadd('XinPan_spider:start_urls',i)
        # count+=1

if __name__ == '__main__':
    redis_client()