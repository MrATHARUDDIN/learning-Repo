Date = int(input("Today date : "))
Month = str(input("Month name : ")) # january
# Do this exersice for undertanding of Mach

match Date:
    case 1 if Month == "january": #just use a normal if condition to know that we can also use condition in \\ match \\
        print("Saturday of January")
    case 1 :
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thusday")
    case 7:
        print("Friday")

