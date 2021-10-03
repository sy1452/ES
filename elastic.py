# ES
from elasticsearch import Elasticsearch

# import librarires
from datetime import datetime
from dateutil import tz
import time
import random
import string

# ES connect
es = Elasticsearch('127.0.0.1:9200', http_auth= ('elastic', 'sks89898!!'))
es.info()

# create index
def create_index(index):
    if not es.indices.exists(index = index):
        return es.indices.create(index = index)

create_index('dash_1')
es.indices.delete(index='dash_6')

# insert data
def insert(index, doc_type, body):
    return es.index(index=index, doc_type= doc_type, body = body)


data_size = 1000
cnt = 0


while cnt < data_size +1 :
    
    document = {
         'time' : datetime(2020, 8, random.randrange(1, 21), random.randrange(9,18), random.randrange(1,50), random.randrange(1,31)).strftime('%Y-%m-%d %H:%M:%S') 
        ,'model': 'model' + str(random.randrange(1, 11))
        ,'tag': 'tag' + str(random.randrange(1, 6))
        ,'node': 'node' + str(random.randrange(1, 6))
        ,'label': {
             'epoch' : random.choice([0, 10, 100, 1000, 10000])
            ,'size': random.choice([100, 500, 1000, 5000, 10000, 50000])
            ,'iteration': random.choice([100, 500, 700, 1000, 1500, 1700, 2000])
        }
        ,'metric': {
             'elapse_time' : round(random.choice([1, 10, 100, 1000])* random.random(), 2)
            ,'accuracy': round(random.random(), 2)
 #           ,'metric_1' : round(random.choice([1, 10, 100])*random.random(), 2)
        }
    }

    result = es.index(index='dash_1', doc_type='dash_1', body=document)
    print(document)
    print(result)

    cnt += 1








########## bf ##########

data_size = 20

cnt =0
while cnt <= data_size:
    document = {
         'day'          : '2021-08-22' 
        ,'time'         : datetime.utcnow().strftime('%H:%M:%S')                                             # real time : year-month-day time
        ,'name'         : 'app' + str(random.randrange(1,101))                                               # app range : 1 ~ 100
        ,'id'           : ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(6))       # random security id : len(6)
        ,'node'         : 'node' + str(random.randrange(1,11))                                               # node range : 1 ~ 10
        ,'epoch'        : random.choice([10, 100, 1000, 10000])                                              # epoch in four cases
        ,'size'         : random.choice([5000, 10000, 15000, 20000, 250000])                                 # size in five cases
        ,'elapsed time' : random.randrange(1, 1001)                                                          # time range : 1 ~ 1000 ms
    }

    print(document)
    insert('sypark', 'test1', document)

    time.sleep(5)     # sleep time : 5 secondes
    cnt += 1



