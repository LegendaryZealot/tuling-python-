import requests
import sys
import json

payload = {'key': '87e8e3586df64daaac58aea0549b157e', 'info': sys.argv[1]}
r = requests.get('http://www.tuling123.com/openapi/api',params=payload)
result=json.loads(r.text)
print(result['text'])
