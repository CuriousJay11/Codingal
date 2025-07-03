def add_number(num1, num2):
    sum_of_numbers = num1 + num2
    return sum_of_numbers

def sub_number(num1, num2):
    diff_of_numbers = num1 - num2
    return diff_of_numbers

def mul_number(num1, num2):
    mul_of_numbers = num1 * num2
    return mul_of_numbers

def div_number(num1, num2):
    div_of_numbers = num1 / num2
    return div_of_numbers

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

result_add = add_number(number1,number2)
result_diff = sub_number(number1,number2)
result_mul = mul_number(number1,number2)
result_div = div_number(number1,number2)

print('Addition of two numbers are : ', result_add)
print('Subtraction of two numbers are : ', result_diff)
print('Multiplication of two numbers are : ', result_mul)
print('Division of two numbers are : ', result_div)