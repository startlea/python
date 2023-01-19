#Description
print("This is BMI calculator")

#Variables
weight = int(input("Type in your weight: \n"))
height = float(input("Type in your height: \n"))

#Result
BMI = round(weight / height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are Underweight.\n")
elif BMI < 25:
    print(f"Your BMI is {BMI}. You have normal weight.\n")
elif BMI < 30:
    print(f"Your BMI is {BMI}. You are overweight.\n")
elif BMI < 35:
    print(f"Your BMI is {BMI}. You are obese.\n")
else BMI:
    print(f"Your BMI is {BMI}. You are clinically obeese.\n")