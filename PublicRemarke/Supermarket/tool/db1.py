# from time import sleep
#
# import redis
#
#
# def redis_client():
#     while True:
#         pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
#         r = redis.Redis(connection_pool=pool)
#         n = r.smembers('ShopList:dupefilter')
#         for i in n:
#             r.srem('ShopList:dupefilter', i)
#             print('删除成功')
#         print('休息5秒')
#         sleep(5)
#
# if __name__ == '__main__':
is_50 = 50
#     redis_client()
page = is_50 if is_50 else '1111'
print(page)
# import execjs
# print(execjs.get().name)