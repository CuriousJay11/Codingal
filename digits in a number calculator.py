number = input("Enter a number: ")
count = 0
i = 0

while i < len(number):
    if number[i] >= '0' and number[i] <= '9':
        count = count + 1
    i = i + 1

print("Total number of digits:", count)