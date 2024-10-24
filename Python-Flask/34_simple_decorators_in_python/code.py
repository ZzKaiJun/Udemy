# 用戶資訊 - 訪客 無訪問權限
user = {"username" : "Jose" , "access_level" : "admin"}

# 回傳密碼到管理面板 (不安全)
def get_admin_password():
    return "1234"


# 安全函數-1
# def secure_get_admin():
#     if user["access_level"] == "admin":
#         return "1234"
print(get_admin_password())

# 安全函數-2
def secure_get_admin(func):
    if user["access_level"] == "admin":
        return func
get_admin_password = secure_get_admin(get_admin_password)

# 安全函數-3  將函數替換為安全函數
def make_secure(func):
    def secure_get_admin():
        if user["access_level"] == "admin":
            return func()
        else:
            print(f"No user permissions for {user["username"]} !")
    return secure_get_admin

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

