d = {"name": "Vijay", "age": 12, "city" : "Bangalore"}
print(d)
print(type(d))

student_records = [
    {'id': 101, 'name': 'Alice', 'class': '10th', 'subjects': ['Math', 'Physics']},
    {'id': 102, 'name': 'Bob', 'class': '10th', 'subjects': ['Chemistry', 'Biology']},
    {'id': 101, 'name': 'Alice', 'class': '10th', 'subjects': ['Math', 'Physics']}, 
    {'id': 103, 'name': 'Charlie', 'class': '11th', 'subjects': ['History', 'English']},
    {'id': 102, 'name': 'Bob', 'class': '10th', 'subjects': ['Chemistry', 'Biology']},
]
print(student_records)

unique_students = {}

for student_records in student_records:
    unique_students[student_records["id"]]=student_records

unique_list = list(unique_students.values())

print("Unique Student Records:")
for s in unique_list:
   print(s)