# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
val = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        #split line into 'X-DSPAM-Confidence' and 'value'
        value = float(line.split(':')[-1])
        count = count + 1
        val = val+value
        avg = val/count
        #print(val)

print("Average spam confidence: ", avg)