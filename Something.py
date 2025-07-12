def anything(n):
    if n == "A1":
        return("You have recieved a lottery ticket")
    elif n == "B2":
        return("You recieved a scratcher for a lottery ticket")
    elif n == " C3":
        return("You recieved eyes to see the number on the lottery ticket")
    elif n == "XX":
        return("Your lottery ticket blew up everthing in a 180 mile radius including you")
    else:
        return("Your lazy to be writing that")

Snack = input("Enter a code: ")

print(anything(Snack))

    


