class Bird:
    def __init__(self):
        print("The bird is ready")
    def fly(self):
        print("Flap Flap")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

peng1 = Penguin()



