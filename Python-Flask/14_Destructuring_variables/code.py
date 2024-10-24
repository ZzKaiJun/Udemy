# 解構變量
t = 5,11   # 5,11 可以視為元組
x,y = t   #  x,y = 5,11
print(x)
print(y)



# 應用在字典中
student_attendance = {"ccf":96 , "abc": 70, "AMB": 89}
print(list(student_attendance.items()))     # 印出元組列表

for t in student_attendance.items():
    print(t)   # 會印出元組


# 解構元組陣列的方法
people = [("ccf", 16, "student"), ("abc", 18, "Mechanic"), ("amb", 22, "Artist")]

for name, age, profession in people:
    print(f"Name:{name}, Age:{age}, Profession:{profession}")

# 可以忽略某些元組的值，只需要某些特定值
person = ("ccf", 16, "studnet")
name, _, profession = person     # _ 變數不會做使用

print(name, profession)

# 所有值放到同個地方
head, *tail = [1,2,3,4,5]
print(head)
print(tail)
