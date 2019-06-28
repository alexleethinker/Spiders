import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['cbs_buurt']
collection = db['data']


file = 'cbs.json'

data = []
with open(file,'r') as f:
    for line in f:
        data.append(json.loads(line))
        
try:
    collection.insert(data)
except:
    pass