#fhand = open('mbox-short.txt')
#count = 0

#1 prints the whole file content
#for words in fhand:
#	print(words)

#2 counts the lines in the document
#for line in fhand: 
#	count = count + 1
#print("Line count: ", count)

#3 read the whole file incl. newlines and print length 
#inp = fhand.read()
#print("Number of symbols: ", len(inp))

#for line in fhand: 
#	line = line.rstrip()
	#skips lines that DON'T start with "From: "
#	if not line.startswith("From: "):
#		continue
#	print(line)

fname = input("Enter the file name:" )

#error handling
try:
	fhand = open(fname)
except:
	print("File", fname, "can't be found!")
	quit()

count = 0

#count and return the no. of lines starting with Subject:
for line in fhand: 
	if line.startswith("Subject:"):
		count = count+1
print("There were", count, "subject lines in", fname)