import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=11, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('not_url:sp_detail')
    # n = r.smembers('crawl_town:start_urls')
    pool = redis.ConnectionPool(host='localhost', port=6379, db=3, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    # r.sdiffstore()
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
        a = r.sadd('DetailSpider:start_urls',i)

        if a==1:
            count+=1
            print('成功')
        else:
            print('已经存在')
            r.srem('DetailSpider:start_urls',i)
            print('删除成功')
            count+=1
    print('删除成功',count)


if __name__ == '__main__':
    redis_client()