from rq import Queue,Worker,use_connection
import redis
listen = ['high', 'default', 'low']

conn = redis.StrictRedis(
        host='192.168.118.137',
        port=6379)
# Tell RQ what Redis connection to use
redis_conn = conn
use_connection(conn)
worker = Worker(map(Queue,listen))
worker.work()
