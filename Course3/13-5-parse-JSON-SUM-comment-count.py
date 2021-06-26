import json
import urllib, urllib.request 


#url = 'http://py4e-data.dr-chuck.net/comments_1260893.json'

#passing url as parameter vs prompt as requested in assignment
url = 'http://py4e-data.dr-chuck.net/comments_1260893.json'

uh = urllib.request.urlopen(url)

#read the JSON data from that URL using urllib
data = uh.read()

#extract the comment counts from the JSON data
info = json.loads(data)
#print(json.dumps(info, indent=4))

sum = 0

#compute the sum of the numbers in the file and print the sum
for u in info['comments']:
    sum += u['count']  
print(sum)