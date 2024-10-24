# 字典 Dictionary   Key : Value 成一對
friend_age = {"ccf" : 22, "abc": 18, "AMB": 19}

# 字典列表  可以儲存更多資訊
friend = [
    {"name": "ccf" , "age": 22},
    {"name": "abc" , "age": 18},
    {"name": "AMB" , "age": 19},
]

print(friend[1])
print(friend[1]["name"])

# for 迴圈用在字典

student_attendance = {"ccf":96 , "abc": 70, "AMB": 89}
# 取得字典key值
for student in student_attendance:
    print(f"{student} : {student_attendance[student]}")

# 更好的寫法:
for student, attendance in student_attendance.items():
    print(f"{student} : {attendance}")


# 簡直某個值是否為字典的鍵之一
if "ccf" in student_attendance:
    print(f"ccf : {student_attendance["ccf"]}")
else:
    print("ccf is not a student in this class. ")

# 只想取出字典的value
attendance_value = student_attendance.values()
print(sum(attendance_value) / len(attendance_value))