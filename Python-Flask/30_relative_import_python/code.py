# python 遇到 import 就會直接跳轉到該套件的內容，所以輸出順序才會這樣
# 相對導入 from ... import ...  需要有資料夾
# 絕對導入 無法使用from .. import .. 方法進行導入
import mymodule

print("code.py: " + __name__)



