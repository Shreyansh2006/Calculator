import time
d = input("y or n")
Userinput1 = float(input("Enter The First Number :\n"))
Userinput2 = float(input("Enter The Second Number :\n"))
bodmas = str(input("Enter what you want to do ADD, SUBTRACT, MULTIPLICATION and DIVISION\npress +, -, * or /..."))

if d == "y":
    if bodmas=="+":
        print(f"The Sum is {Userinput1 + Userinput2}")
    elif bodmas=="-":
        print(f"The Difference is {Userinput1 - Userinput2}")
    elif bodmas=="*":
        print(f"The Product is {Userinput1 * Userinput2}")
    elif bodmas=="/":
        print(f"The Quotient is {Userinput1 / Userinput2}")
    time.sleep(20)
else:
    exit()
