import redis

# r=redis.Redis(host='127.0.0.1', port=6379,db=3)
# f = open("a.txt")
# for line in f:
#     r.lpush('proxies',line.strip())
#     print(line.strip())
    # print(line.strip())
    # a=f.read().decode()
# for i in a.split(r'//n'):
#     print(i)
#     r.lpush('proxies',a)
    # print(a)



pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# n=r.lrange('sp_detail:start_urls',0,-1)
# count = 0
# for i in n:
#     c = r.sadd("sp_detail_set:start_urls",i)
#     if c==1:
#         count+=1
#         print(i)
# print(count)
n = r.smembers('sp_detail_set:start_urls')
for i in n:
    r.rpush('sp_detail:start_urls',i)
print('----')