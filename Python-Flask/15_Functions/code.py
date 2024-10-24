# 定義function， def 並不會執行這個變量，僅僅只是告訴Python你有創建一個 hello()變量
def hello():
    print("Hello!")

hello()

#
def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

# user_age_in_seconds()


# 在funtion內部會優先使用內部的變量，如果沒有才會往外部找

friends = ["ccf", "abc"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    # friends = friends + [friend_name]      # 這寫法會出錯，因為friends 是在function內部定義，會優先被使用
    f = friends + [friend_name]
    print(f)

add_friend()


# function 必須先定義才能使用它

# add_friends()

# def add_friends():
#     friends.append("Rolf")