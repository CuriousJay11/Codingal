class Laptops():
    Screen=1
    Keyboard=1
    def __init__ (self,colours,brands,sizes,graphics,usage):
        self.colour = colours
        self.brands = brands
        self.sizes = sizes
        self.graphics = graphics
        self.usage = usage
    
    def Watching(self):
        ("Lets watch something")

    def Gaming(self):
        ("Lets Play Some Games")

    def Display(self):
        print("Brand of the laptop is,",self.brands,",Colour of the laptop is,",self.colour,",Size of the Laptop is,",self.sizes,",Graphics used in the laptop is,",self.graphics,",The usage of the laptop is,",self.usage)


Object1 = Laptops("Red","Lenovo Legion","32x16","Radeon","Gaming")
Object2 = Laptops("Blue","HP Pavillion","34x18","NVIDIA GeForceRTX","MultiUse")
Object3 = Laptops("White","MacBook Pro","24x18","M4 Series","Studying")

Object1.Display()
Object2.Display()