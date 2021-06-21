serviceHours = input("Enter Open Hours: ")
serviceRate = input("Enter Service Cost per Hour: ")

try: 
	float_serviceHours = float(serviceHours)
	float_serviceRate = float(serviceRate)
except: 
	print("Invalid input")

print("Your Pay is:", float_serviceHours-40.0 * float_serviceRate*1.5)