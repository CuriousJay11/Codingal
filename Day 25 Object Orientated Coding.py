sentence = ("I walked my fish in the park")
print(type(sentence))

class Dog():
    eyes=2
    tail=1
    skin = "flurry"
    can_fly=True
    legs=4

    def bark(self):
        print("RUFF-RUFF")

    def run(self):
        print("The dog runs fast")

husky=Dog()
german_shepard=Dog()
beagle=Dog()

print(husky.can_fly)
print(beagle.skin)

german_shepard.bark()