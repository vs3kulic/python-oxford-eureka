from urllib import request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1260892.xml'

#retrieve url and read the XML string, store it in a variable and print the no. of characters  
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

#create a tree from the string variable, find all comment tags and print the no. of comment(s)
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount=len(results)
print("Count:", icount)

isum=0

#for each result, find the count tag and its text  
for result in results:
    isum += float(result.find('count').text)

print("Sum:", isum)