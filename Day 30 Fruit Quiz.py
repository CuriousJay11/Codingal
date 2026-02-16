import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "orange": "orange",
            "banana": "yellow",
            "dragonfruit": "white",
            "lichi": "white",
            "watermelon": "green"
        }

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of the fruit:", fruit)
            choice = input("Enter the fruit color: ")

            if choice.lower() == color:
                print("Correct answer")
            else:
                print("Wrong answer... try next question")

            option = input("Do you want to play again? (y/n): ")
            if option.lower() == "n":
                break


# Run the quiz
game = FruitQuiz()
game.quiz()
