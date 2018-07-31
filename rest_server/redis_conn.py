import redis
import socket
ip = socket.gethostbyname('redis-server')
print ip
try:
    conn = redis.StrictRedis(
        host=ip,
        port=6379)
    print conn
    conn.ping()
    print 'Connected!'
except Exception as ex:
    print 'Error:', ex
    exit('Failed to connect, terminating.')
