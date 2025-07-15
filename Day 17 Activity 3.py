# ROCK PAPER SCISSORS

import random

options = ("Rock","Paper","Scissor")

Your_Choice = input("Think hard and choose from Rock, Paper, Scissor,(Btw its rigged i always win):  ")

Computer_Choice = random.choice(options)

if Computer_Choice == Your_Choice:
    print("You beat the system")
elif Computer_Choice == "Rock" and Your_Choice == "Scissor":
    print("You lose, Rock beats Scissor")
elif Computer_Choice == "Paper" and Your_Choice == "Rock":
    print("You lose, Paper beats Rock")
elif Computer_Choice == "Scissor" and Your_Choice == "Paper":
    print("You lose, Scissor beats Paper")
elif Your_Choice == "Rock" and Computer_Choice == "Scissor":
    print("You Win, Rock beats Scissor")
elif Your_Choice == "Paper" and Computer_Choice == "Rock":
    print("You Win, Paper beats Rock")
elif Your_Choice == "Scissor" and Computer_Choice == "Paper":
    print("You Win, Scissor beats Paper")
else:
    print("You can never beat me :)")

