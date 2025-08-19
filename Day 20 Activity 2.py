t = (1, 2, 3, 3, 2, 1)

if t == t[::-1]:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")


def palindrome(r):
    s = 0
    e=len(r)-1
    while(s>e):
        if(r[s]!=r[e]):
            return False
        s = s + 1
        e = e-1

    return True
r = (6,7,8,9,10)
if (palindrome(r)):
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")
