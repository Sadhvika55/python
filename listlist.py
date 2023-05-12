student=['rani','roja','ravi',['88','89','94']]
student.insert(0,1)
print(student)
student.append(1)
print(student)
stud=['B','A','O']
student.extend(stud)
print("list as",student)
student[4].remove('88')
print(student)
student.pop(2)
print(student)
student[::-1]
print(student)
print(len(student))
print(student.count(94))


