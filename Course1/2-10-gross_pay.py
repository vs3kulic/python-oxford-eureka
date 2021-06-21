#prompt user for inputs
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

#convert input string to float to enable calculation
gross_pay = float(hrs)*float(rate)

#print result
print("Pay:", gross_pay)