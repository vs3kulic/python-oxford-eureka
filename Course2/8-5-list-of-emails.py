#first working version
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0

for line in fh:
    words = line.split()
    if not line.startswith('From '): continue
    count = count + 1
    print(words[1])
    
print("There were", count, "lines in the file with From as the first word")


#another version of the for loop
for line in fhand:
    line = line.rstrip()
    if line == "": continue      
    words = line.split()
    if words[0] !="From": continue
    print(words[1])
    count = count+1

print ("There were", count, "lines in the file with From as the first word")

#another elegant solution with concatenated function
for line in fh:
    words = line.split()
    if line.startswith('From '): 
        word = line.strip().split()
        print(word[1])
    	count = count + 1
    
print("There were", count, "lines in the file with From as the first word")