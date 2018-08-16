import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=4, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('crawl_sp_list:start_urls')
    # n = r.smembers('crawl_town:start_urls')
    # pool = redis.ConnectionPool(host='localhost', port=6379, db=8, decode_responses=True)
    # r = redis.Redis(connection_pool=pool)
    count = 0
    for i in n:
        # print(i)
        if i == 'https://zs.sp.anjuke.com/shou/zhangjiabian/':
            # print(i)
            print('找-到：{}'.format(i))
        else:
            pass
            # print('没找到：{}'.format(i))
        # if count==30:
        #     break
        # r.sadd('XinPan_spider:start_urls',i)
        # count+=1

if __name__ == '__main__':
    redis_client()