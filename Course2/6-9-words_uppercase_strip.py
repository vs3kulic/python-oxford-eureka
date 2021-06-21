# Use words.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

for words in fh: 
    up = words.upper()
    print(up.rstrip())