import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl

#ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#using BeautifulSoup library to crawl webpage
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')

tagSum = 0

#for loop to go through tags, return the contents, convert them to int and sum up  
for tag in tags:
	tagSum += int(tag.contents[0])
print(tagSum)

#sample code to look for parts of the tags
#for tag in tags:
	#print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

