import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=2, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('sp_detail:start_urls')
    # n = r.smembers('crawl_town:start_urls')
    pool = redis.ConnectionPool(host='localhost', port=6379, db=10, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    count = 0
    for i in n:
        # print(i)
        # if i == 'https://zs.sp.anjuke.com/shou/zhangjiabian/':
        #     # print(i)
        #     print('找-到：{}'.format(i))
        # else:
        #     pass
            # print('没找到：{}'.format(i))
        # if count==30:
        #     break
        # if count==50:
        #     break
        a = r.sadd('sp_detail:start_urls',i)

        if a==1:
            count+=1
            print('成功')
        else:
            print('已经存在')


if __name__ == '__main__':
    redis_client()