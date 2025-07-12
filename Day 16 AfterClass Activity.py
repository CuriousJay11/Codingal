valid = False
while not valid:
    try:
        age = int(input("Enter your age: "))
        if age%2==0:
            print("Your age is a number and even")
        else: 
            print("Your age is a number and odd")
        valid = True
    except ValueError:
        print("Invalid")





 