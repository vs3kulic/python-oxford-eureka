largest = None
smallest = None
list=[]

while True:
    num = input("Enter a number: ")

    if num == "done":
        break
    try:
		fnum = float(num)
    except:
		print("Invalid input")
		continue

    list.append(fnum)

for value in list: 
    if smallest is None:
        smallest=value
    elif value < smallest:
        smallest=value
    elif largest is None:
        largest=value
    elif value > largest:
        largest=value
        
print("Maximum is", int(largest))
print("Minimum is", int(smallest))