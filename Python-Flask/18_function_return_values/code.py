
# function 預設回傳為 None
def add(x,y):
    print(x+y)

print(add(5,8))


# function 指定回傳值
def add(x,y):
    print(x+y)
    return x+y

print(add(5,8))


# function 遇到 return 就會停止往下運行
def add(x,y):
    return x+y
    print(x+y)
    
print(add(5,8))