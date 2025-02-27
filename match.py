x = int(input("enter number "))

match x:
    case 1:
        print("You enter one")
    case 2:
        print("You enter two")
    case 3:
        print("You enter three")
    case _:
        print("You enter number > 3")
