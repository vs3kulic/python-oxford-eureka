serviceHours = input("Enter Open Hours: ")
serviceRate = input("Enter Service Cost per Hour: ")

try: 
	float_serviceHours = float(serviceHours)
	float_serviceRate = float(serviceRate)
except: 
	print("Please provide numeric inputs for Open Hours and Service Cost!")
	quit()

print(float_serviceHours, float_serviceRate)
if float_serviceHours > 40:
	regularPay = float_serviceHours*float_serviceRate
	overtimePay = (float_serviceHours-40.0) * (float_serviceRate*0.5)
	sumPay = regularPay+overtimePay
else: 
	sumPay = float_serviceRate*float_serviceHours

print("Your Overtime Pay for this month is: ", overtimePay)
print("Your Total Pay for this month is: ", sumPay)	