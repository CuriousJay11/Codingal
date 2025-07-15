import random
playing = True
number = str(random.randint(10,15))

print("I will generate a number from 10 - 15, and you have to guess the number")

while playing:
    guess = input("Give your best shot: ")
    if guess == number:
        print("Good Job")
        print("The number was",number)
        break
    elif guess < number:
        print("Close but higher,You can do better!")
    elif guess > number:
        print("Almost there but lower")

    else:
        print("Too Bad So Sad")
