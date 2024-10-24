# 傳入參數與function定義的參數量要相同
def add(x,y):   # x,y 稱為參數 parameters
    result = x + y
    print(result)

add(5,3)  # 5,3 稱為參數 arguments


# 指定參數的傳入值 keyword argument
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello(surname="Bob", name="Smith")

# positional argument 必須優先於 keyword argument

say_hello("Bob", surname="Smith")
# say_hello(name = "Bob", "Smith")   #錯誤寫法