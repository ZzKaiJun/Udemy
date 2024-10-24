import functools

user = {"username" : "Jose" , "access_level" : "admin"}

# 安全函數-3  將函數替換為安全函數
def make_secure(func):
    # 聲名是該func的包裝器，保存該函數的名稱和文檔，讓該函數不會被安全函數的資訊蓋過去，需放在安全函數最上方
    @functools.wraps(func)

    def secure_function(*args, **kwargs):       # 如果func 有傳入參數，可以使用 *args , **kwargs 來創建，這樣就不用常常修改
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            print(f"No user permissions for {user["username"]} !")
    return secure_function

# at 函數 ，將阻止函數被創建，而是創建它，並通過裝飾器傳遞它，一次完成。
@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "Bob":
        return "password"

# get_admin_password = make_secure(get_admin_password)

print(get_admin_password("Bob"))

print(get_admin_password.__name__)