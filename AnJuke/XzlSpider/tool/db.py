import redis


def redis_client():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r