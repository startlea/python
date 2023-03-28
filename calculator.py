def operator(operator):
    n1 = float(input("Give first number: "))
    n2 = float(input("Give second number: "))
    if operator == "1":
        result = n1 + n2
        print(round(result, 2))
    elif operator == "2":
        result = n1 - n2
        print(round(result, 2))
    elif operator == "3":
        result = n1 * n2
        print(round(result, 2))
    elif operator == "4":
        result = n1 / n2
        print(round(result, 2))
    else:
        print("Your operation pick is not valid.\n")
        return False
    return True


def calculate():
    is_operator_ok = False
    while not is_operator_ok:
        is_operator_ok = operator(input("""What do you want to do? [pick a number] 
        1. Sum
        2. Subtraction
        3. Multiply
        4. Divide
        Your pick : """))


def ask():
    repeat = "yes"
    while repeat == "yes" or repeat == "Yes":
        calculate()
        repeat = input("Do you want to repeat? [yes/no] ")

    
ask()
print("\nThank you and see you another time.")  
print("bye, bye...\n") 
