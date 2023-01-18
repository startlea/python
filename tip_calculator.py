#Description
print("Welcome to the tip calculator ")

#Variables
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentege tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill? \n"))

#Result
pay = (bill + bill*(tip/100))/people
final_pay = round(pay, 2)

print(f"Each person should pay: {final_pay}")