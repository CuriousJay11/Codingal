a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

a, b, c = b, c, a

print("After swapping:", a, b, c)