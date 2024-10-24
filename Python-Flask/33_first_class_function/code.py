# 一級函數

# 函數只是個變量，可以把參數給函數，並像使用其它變量一樣來使用

def divide(dividend , divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

# operator 是怎麼做為一個function來使用? python怎麼知道這個未定義的function?
def calculate(*value , operator):
    return operator(*value)

# divide不加() ，才能成功調用 
# 在此例中如果傳入參數大於2，也會回傳錯誤，因為divide只接受兩個參數
result = calculate(20, 4, operator=divide)
print(result)




#--------------------------------


# 搜尋函數
# sequence 搜尋的資料 ， expected 預期要的資料
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Couldn`t find an element with {expected}. ")


friends = [
    {"name" : "Rolf Smith" , "age" : 24},
    {"name" : "Adam Wool" , "age" : 30},
    {"name" : "Anne Pun" , "age" : 27},
]

# 想找到friend name = Rolf Smith ，必須先創立一個函數

def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith" , get_friend_name))
print(search(friends, "Rolf Smith" , lambda friend: friend["name"]))  # 使用lambda 函數達成

from operator import itemgetter
print(search(friends, "Rolf Smith" , itemgetter("name")))  # 引用python內建的itemgetter