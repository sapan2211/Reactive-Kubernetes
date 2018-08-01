from rq import Queue,Worker,use_connection
import socket
import redis
listen = ['high', 'default', 'low']

ip = socket.gethostbyname('redis-server')

conn = redis.StrictRedis(
        host=ip,
        port=6379)
# Tell RQ what Redis connection to use
redis_conn = conn
use_connection(conn)
worker = Worker(map(Queue,listen))
worker.work()
