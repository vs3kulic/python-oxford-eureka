import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl

#ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#using BeautifulSoup library to crawl webpage
url = input('Enter URL: ')
position = int(input('Enter position: '))
repetitions = int(input('Enter number of repetitions: '))

#repeat desired number of times (request_number)
for i in range(repetitions): 
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	
	count = 0
	
	for tag in tags: 
		count += 1
		#stop at desired position
		if count > position:
			break
		url = tag.get('href', None)
		name = tag.contents[0]

print(name)