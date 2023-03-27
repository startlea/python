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
        print("This is not valid option.")
        return operator
    

def repeat():
    repeat = input("Do you want to repeat?[yes/no] ")
    if repeat == "yes":
        operator(input("""What do you want to do?[pick a number] 
        1. Sum
        2. Subtraction
        3. Multiply
        4. Devide
        Your pick : """))
    elif repeat == "no":
        print("Thank you and see you another time.")  
    else:
        print("Check your answer")
        return repeat
  
print("""What do you want to do?[pick a number] 
    1. Sum
    2. Subtraction
    3. Multiply
    4. Devide""")
operator(input("Your pick : "))

repeat()