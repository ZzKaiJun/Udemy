# ** 用來蒐集關鍵字參數 keyword argument  轉成字典
def name(**kwargs):
    print(kwargs)

name(name="Bob", age=25)


# ** 將字典 unpacking 至 關鍵字參數 keyword argument

def named(name , age):
    print(name, age)

details = {"name" : "Bob", "age" : 25 }
named(**details)


# 印出字典的值

def print_nicely(**kwargs):
    named(**kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_nicely(name="Bob" , age=25)


# 可以兩種一起使用 ， 帶*號通常用於接收不限數量的參數

def both(*args, **kwargs):
    print(args)     #位置參數
    print(kwargs)   #命名參數

both(1, 3, 5, name = "Bob" , age = 25)


# 錯誤的格式

def my_function(**kwargs):  
    print(kwargs)

my_function(**"name")
my_function(**None)