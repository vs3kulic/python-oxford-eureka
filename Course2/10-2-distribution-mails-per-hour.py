#program to figure out the distribution by hour of the day for each of the messages

#file handler
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()

counts=dict()

#loop through the file line-by-line, take each line starting with 'From' and strip the space at the end and split it
#pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon
for line in handle:
    if line.startswith("From "):
        line=line.strip().split()
        hours=line[5]
        hours=hours[:2]
        lst.append(hours)

#accumulate the counts for each hour and store them in lst
for hour in lst :
    counts[hour]=counts.get(hour,0)+1

#sort the hours and print
for k,v in sorted(counts.items()) :
    print(k,v)