import requests
import time
import threading
import pandas as pd



headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Referer': 'https://opendata.cbs.nl/statline/portal.html?_la=nl&_catalog=CBS&tableId=84286NED&_theme=243',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

params = {
    '$select':'*',
    '$skip':'10000'
}

url = 'https://opendata.cbs.nl/ODataFeed/odata/84286NED/UntypedDataSet'
s = requests.Session()
json = s.get(url = url,headers = headers, params = params).json()

import pandas as pd

data = pd.DataFrame(json).value.apply(pd.Series)
data.to_csv('cbs.csv')
print(data.shape)


'''
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['cbs_buurt']
collection = db['data']

collection.insert(json)

'''



