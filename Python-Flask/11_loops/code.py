
number = 7
'''
使用 while 進行 loops
'''
# 1. 較為直觀的寫法，可以改寫成下面的程式碼
# user_input = input("Would you like to play? (Y/n) ")

# while user_input != "n":
#     user_number = int(input("Guess our number (1~10)"))
#     if user_number == number:
#         print("You guess correctly! ")
#     elif abs(user_number - number) == 1:
#         print("You were off by one.")
#     else:
#         print("Sorry, it's wrong! ")

#     user_input = input("Would you like to play? (Y/n) ")


# 2. 另外的寫法，若user輸入n 就會跳出迴圈
# while True:
#     user_input = input("Would you like to play? (Y/n) ")
#     if (user_input) == "n":
#         break

#     user_number = int(input("Guess our number (1~10)"))
#     if user_number == number:
#         print("You guess correctly! ")
#     elif abs(user_number - number) == 1:
#         print("You were off by one.")
#     else:
#         print("Sorry, it's wrong! ")

'''
使用 for 進行 loops
'''
friends = ["Rob", "ccf", "AMB", "AL"]

# 最常用的用法
for friend in friends:
    print(friend)

# range(number) 指定執行次數
for friend in range(4):
    print(f"{friends[friend]} is my friend. ")


grades = [10,42,45,95,75]
total = 0
amount = len(grades)

for grade in grades:
    total = total + grade  # total += grade
print(total)               # sum(grades)
print(total/amount)