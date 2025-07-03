num = int(input("Enter any number: "))
flag = False

for i in range(2,num):
    if (num % i) == 0:
        flag = True
        break
if flag:
    print(num,"It is not a prime number")
else:
    print(num,"It is a prime number")