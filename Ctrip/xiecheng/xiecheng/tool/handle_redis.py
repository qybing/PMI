import logging

import redis

logger = logging.getLogger(__name__)

class RedisClient(object):
    def __init__(self):
        # password = '420319'
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=15,decode_responses=True)
        self.r = redis.Redis(connection_pool=self.pool)

    # def __del__(self):
    #     self.pool.disconnect()
    #     logger.info('关闭了')

    def add_value(self, key, value):
        is_repeat = self.r.sadd(key, value)
        if is_repeat == 1:
            logger.info('url:{}            插入成功'.format(value))
        else:
            logger.info('url:{}           已经存在队列中'.format(value))