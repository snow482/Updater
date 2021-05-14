import os
import psutil
import json
import requests

def archiveSaving():
    responce = requests.get('https://dungeon.su/gallery/articles/78_7_1522772236.jpg')
    if os.path.exists(r'C:\Scada2\Downloads'):
        with open(r'C:\Scada2\Downloads\image2.png', 'wb') as way:
            way.write(responce.content)
    else:
        os.mkdir(r'C:\Scada2\Downloads')
        with open(r'C:\Scada2\Downloads\image2.png', 'wb') as way:
            way.write(responce.content)

        
    
    
    


#print(newJson[1])
#numbers = tmp['headers']['Host']
#m = '188.170.85.58'
#m = 'httpbin.org'
#if m == tmp['headers']['Host']:
#    print('true')

n = list()
for variable in tmp['headers']['Host']:
    n.append(variable)
print(n)

if m == "".join(map(str, n)):
    print('true')
else:
    print('smtg wrong')

'''for variable in tmp['origin']:
    n.append(variable)
print(n)

if m == "".join(map(str,n)):
        print('true')
else: 
    print('false')'''


#print(m)
#for variable in tmp['headers']:
#    print(variable)


#if numbers == 'httpbin.org':
    #print('true')
#else:
    #print('false')
#print(tmp['headers']['Accept'])
#print(numbers)


