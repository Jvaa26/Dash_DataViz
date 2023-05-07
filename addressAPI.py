import requests
import json

TOKEN='oa.927a80ab1c0941ec71328626ca79ec09aa6cfbc4c8574ccfe606a8791d48ae7b'

re=requests.get('https://batch.openaddresses.io/api/export').json()

ids = []

for e in re['exports']:
    if 'br' in e['source_name'] and 'statewide' in e['source_name']:
        print(e['id'],e['source_name'])
        ids.append(e['id'])
print(ids)
        

