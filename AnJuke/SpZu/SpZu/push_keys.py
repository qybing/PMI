import pymysql
import redis

# pool = redis.ConnectionPool(host='localhost', port=6379,db=1, decode_responses=True)
# r = redis.Redis(connection_pool=pool)
r = redis.Redis(host='127.0.0.1', port=6379,db=1)
db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='jovan',
                     charset='utf8')
cursor = db.cursor()
def check_url():
    sql = 'select id,url from sp_url where is_use=0'
    cursor.execute(sql)
    rs = cursor.fetchall()
    for row in rs:
        yield row

def up_data_by_id(id):
    sql = 'update sp_url set is_use=1 where id={}'.format(id)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('修改失败')
        print(e.args)

def push_to_redis():
    for id,url in check_url():
        try:
            r.lpush('sp_zu:start_urls',url)
            up_data_by_id(id)
        except Exception as e:
            print()

if __name__ == '__main__':
    push_to_redis()