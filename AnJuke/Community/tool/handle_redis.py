import redis


class RedisClient(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=4, decode_responses=True)
        self.r = redis.Redis(connection_pool=self.pool)

    def __del__(self):
        self.pool.disconnect()
        print('关闭了')

    def add_value(self, key, value):
        is_repeat = self.r.sadd(key, value)
        if is_repeat == 1:
            print('url:{}             插入成功'.format(value))
        else:
            print('url:{}             已经存在队列中'.format(value))
