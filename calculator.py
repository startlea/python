operator = input("What do you want to do?[+,-,*,/] ")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
result = n1 + n2

if operator == "+":
    result = n1 + n2
    print(round(result, 2))
elif operator == "-":
    result = n1 - n2
    print(round(result, 2))
elif operator == "*":
    result = n1 * n2
    print(round(result, 2))
elif operator == "/":
    result = n1 / n2
    print(round(result, 2))
else:
    print(f"{operator} is not valid option.")
