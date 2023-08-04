print("Welcome to the PizzaPlaza Deliveries!")
size = input("What pizza size do you want? S, M or L? \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want estra cheese? Y or N \n")

bill = 0

if size == "S" or "s":
    bill+=15
elif size == "M" or "m":
    bill += 20
elif size == "L" or "l":
    bill += 25
else:
    print("Choose the correct size ")       

if add_pepperoni == "Y" or "y":
    if size == "S" or "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y" or "y":
    bill += 1

print(f"Your final bill is ${bill}")
