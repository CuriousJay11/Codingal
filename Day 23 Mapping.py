def findsquare(num):
    return num*num

num= [67,420,69,6,7,3,5,2,7,54,32,3,12,45,190]
result=map(findsquare,num)
print(list(result))

def findcube(num2):
    return num2*num2*num2

num2 = [18,19,4,5,6,7,420,69,67,12,76.45]
result=map(findcube,num2)
print(list(result))

