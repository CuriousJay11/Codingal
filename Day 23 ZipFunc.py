#zip function

students= ['vijay','renuka','aarav','rohan','rahul','arjun']
rollno= [4,6,2,8,10,12]

combined = zip(students,rollno)

print(list(combined))

items = ['Pizza','Burger','Pasta','Salad','Soda','Taco']
prices = [12.99,8.50,10.00,7.25,6.7,2.50]

#combing item names with their respective prices
order = zip(items,prices)
print(list(order))