import redis

r=redis.Redis(host='127.0.0.1', port=6379)
f = open("a")
for line in f:
    r.lpush('proxies',line.strip())
    # print(line.strip())
    # a=f.read().decode()
# for i in a.split(r'//n'):
#     print(i)
#     r.lpush('proxies',a)
    # print(a)
