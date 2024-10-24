
# 用戶資訊的列表元組
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "sdfosd"),
    (2, "Jose", "longsword"),
    (3, "username", "2342")
]


# 希望能做一個根據用戶名稱，然後顯示出用戶訊息的功能
# 字典解析   user[1]:key   user:value   放入字典是值為一對鍵值  key:value
username_mapping = {user[1]:user for user in users}

print(username_mapping)

# 知道其中一位用戶名稱，只需進入字典查詢就能得知資訊
print(username_mapping["Bob"])

# 應用: 請輸入者輸入相關資訊
username_input = input("Enter your name: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]   # id不重要所以用 _ 

if password_input == password:
    print("Your details are correct! ")
else:
    print("Your details are incorrect! ")
    
print(username)
print(password)
