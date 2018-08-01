from rq import Queue,Worker,use_connection
import redis
from word_count import count_words_at_url
import time

listen = ['high', 'default', 'low']

conn = redis.StrictRedis(
        host='192.168.118.137',
        port=6379)
# Tell RQ what Redis connection to use
redis_conn = conn
q = Queue(connection=redis_conn)  # no args implies the default queue
use_connection(conn)
#print len(q)
#queued_job_ids = q.job_ids
#print queued_job_ids
# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(count_words_at_url, 10)

#queued_job_ids = q.job_ids
#print queued_job_ids

print job.result   # => None
#worker = Worker(map(Queue,listen))
#worker.work()
# Now, wait a while, until the worker is finished
#rq worker
time.sleep(5)
print job.result 
