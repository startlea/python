def how_r_u(how_r_u):
    if how_r_u == "good":
        print("That's great! \nI'm happy for you.")
    elif how_r_u == "ok":
        print("That's ok, it will be good. \nFingers crossed for it")
    elif how_r_u == "bad":
        print("Ooh I'm so sorry for you. \nHugging you tightly so you could feel better")
    else:
        print("Check your answer")
        return how_r_u

def repeat():
    repeat = input("Do you want to repeat?[yes/no] ")
    if repeat == "yes":
        how_r_u(input("How are you doing today? [good/ok/bad] "))
        print("Thank you for the contact.") 
    elif repeat == "no":
        print("Thank you for the contact.")  
    else:
        print("Check your answer")
        return repeat
     
     
print("Hello Beautiful!")
how_r_u(input("How are you doing today? [good/ok/bad] "))
repeat()
