#Description
print("This is leap year checker.\n")

#Variables
year  = int(input("What year do you want to check?\n"))

#Result
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("This is not a leap year.\n")
    else:
        print("This is leap year.\n")
else:
    print("This is not a leap year.\n")