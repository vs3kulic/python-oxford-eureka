#create a file handler 
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#create an empty list, look for 'From ' lines, take the second word of those lines (person who sent the mail) and store it in the list
lst = list()
for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

#create empty dictionary and map the sender's mail address to a count of the number of times they appear in the list
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

#create empty variables 
bigcount = None
bigword = None

#reads through the dictionary using a maximum loop to find the most prolific committer
for word, count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
            
print(bigword, bigcount)