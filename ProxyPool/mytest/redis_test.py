import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
a=[3,4,5]
r.rpush("list1",a)
# print(r.lrange('list1', 1, -2))

