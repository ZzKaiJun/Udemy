# 目的是讓寫程式更容易  例如生活中的椅子、桌子

class Student:
    # function in class called method
    def __init__(self, name, grades):       #初始化會執行的method 方法
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (80, 99 , 57, 64, 45))
print(student.name)
print(Student.average_grade(student))   # 使用 class 的 method 計算平均值
print(student.average_grade())          # 使用 class 的 method 計算平均值  (較為常用的方法)



