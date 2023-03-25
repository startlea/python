print("Hello Beautiful!")
def how_r_u():
    how_r_u = input("How are you doing today? [good/ok/bad] ")
    if how_r_u == "good":
        print("That's great! \nI'm happy for you.")
    elif how_r_u == "ok":
        print("That's ok, it will be good. \nFingers crossed for it")
    elif how_r_u == "bad":
        print("Ooh I'm so sorry for you. \nHugging you tightly so you could feel better")
    else:
        print("Check your answer")

def repeat():
    repeat = input("Do you want to repeat?[yes/no] ")
    if repeat == "yes":
        how_r_u()
        print("Thank you! Have a nice day.") 
    elif repeat == "no":
        print("Thank you! Have a nice day.")  
    else:
        print("Check your answer")
         
how_r_u()
repeat()
