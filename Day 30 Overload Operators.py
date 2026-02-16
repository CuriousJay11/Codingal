class A:
    def __init__(self,num1):
        self.num1=num1
    def __eq__(self,num2):
        if (self.num1==num2.num1):
            return "object 3 is equal to object4"
        else:
            return "object 4 is not equal the object3"
    def __lt__(self,num2):
        if (self.num1<num2.num1):
            return "object 1 is less than the object"
        else:
            return "object2 is less than the object1"

object1 = A(415)        
object2 = A(420)
object3 = A(67)
object4 = A(67)

print(object1 < object2)
print(object3 == object4 )
 



