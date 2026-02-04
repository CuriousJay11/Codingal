class Family():
    #__init__ is for initialization, Using selfkeyword you can refer to the values of your own class
    def __init__(self,name,age,height,relation):
        self.name = name
        self.age = age
        self.relation= relation
        self.height = height

    def eating(self):
        print("Lets have dinner together")
    def __len__(self):
        return int(self.age)
    def __str__(self):
        return str(self.name)

son1=Family("vijay",14,5.4,"son")
mother=Family("Amudha",47,5.8,"mother")

print("The age of the son is",son1.age)
print("The height of the son is",son1.height)
print("The mother's relation is",mother.relation)

son1.eating()
print(len(son1))
print(str(mother))