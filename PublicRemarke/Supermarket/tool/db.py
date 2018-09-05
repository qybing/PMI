import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    n = r.smembers('Shop:start_urls')
    # n = r.smembers('crawl_town:start_urls')
    # pool = redis.ConnectionPool(host='localhost', port=6379, db=11, decode_responses=True)
    # r = redis.Redis(connection_pool=pool)
    # r.sdiffstore()
    count = 0
    for i in n:
        # if 'jump' in i:
        #     print(i)
        #     r.srem('sp_detail:start_urls', i)
        # if i == 'https://bj.xzl.anjuke.com/zu/yizhuang-p31/':
        #     print('找到了')
        # else:
        #     print(i)


        if i == 'http://www.dianping.com/shop/45636153':
            # print(i)
            print('找-到：{}'.format(i))
        else:
            pass
            # print('没找到：{}'.format(i))
        # if count==30:
        #     break
        # if count==10000000:
        #     break
    #     a = r.sadd('DetailSpider:start_urls',i)
    #     if a==1:
    #         # count+=1
    #         print('成功')
    #     else:
    #         print('已经存在')
    #         r.srem('DetailSpider:start_urls',i)
    #         print('删除成功')
    #         count+=1
    #     print(i)
    #     a = str(i).replace('www','m')
    #     r.sadd('MShop:start_urls',a)
    # print('删除成功:',count)

        # if i =='http://www.dianping.com/xinxiang/ch20/g187r13552p5':
        #     print('找到了')


if __name__ == '__main__':
    redis_client()