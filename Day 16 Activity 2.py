try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    result = num1/num2
    print("Result is:",result)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter numerical value")
except NameError as ex:
    print("The exception is",ex)
except:
    print("Your device hates u")
finally:
    print("I will execute no matter what happens")
