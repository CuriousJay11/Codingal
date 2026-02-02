# Parent class
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def display(self):
        print(self.name)
        print(self.age)
        print(self.height)


# Child class
class Student(Person):
    def __init__(self, name, age, height, grade, school):
        Person.__init__(self, name, age, height)
        self.grade = grade
        self.school = school


stu1 = Student("vijay", 13, 5.1, 8, "abc school")
stu2 = Student("ravi", 13, 5.4, 8, "abc school")

class Doctor(Person):
    def __init__(self,name,age,height,degree,experience):
        Person.__init__(self,name,age,height)
        self.degree = degree
        self.experience = experience

doc1 = Doctor("Surya",41,5.5,"MD",7)
doc2 = Doctor("Mahesh",37,5.1,"DDS",9)



stu1.display()
stu2.display()
doc1.display()
