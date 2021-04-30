import os
import psutil
import json
import requests

responce = requests.get('https://httpbin.org/get').content
tmp = json.loads(responce)
#newJson = json.dumps(tmp, indent=4) # для отображения удобного, indent=4 - 4 отступа
#print(newJson)

for variable in tmp['headers']:
    print(variable['Accept'])



numbers = tmp['headers']['Host']
#if numbers == 'httpbin.org':
    #print('true')
#else:
    #print('false')
#print(tmp['headers']['Accept'])
#print(numbers)


