import re

#read the file
hand = open("regex_sum_1260888.txt")
x=list()

#look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and put them in the x list
for line in hand:
     y = re.findall('[0-9]+',line)
     x += y

#converting the extracted strings to integers and summing up the integers
sum=0
for z in x:
    sum += int(z)

print(x)
print(sum)