# student class
from Student import Student

student1=Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.5, True)
# print(student1.gpa)
# print(student2.major, student2.name)
# student2.gpa = 5
# print(student2.gpa)

print(student1.name, student1.on_honor_roll())
print(student2.name, student2.on_honor_roll())