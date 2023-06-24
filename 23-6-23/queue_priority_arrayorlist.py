students_grade=[]
students_grade.append((1,"Akash"))
students_grade.append((2,"anitha"))
students_grade.append((3,"raj"))
students_grade.append((4,"tej"))
print("priority queue is")
students_grade.sort(reverse=True)
print(students_grade)
print("original queue is")
while students_grade:
    print(students_grade.pop())