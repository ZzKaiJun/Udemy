from mymodule import divide

# 你運行的文件為dunder main  __name__會顯示 __main__
# 一旦導入其它文件，python會根據他們的路徑來定義它   __name__ 會顯示 mymodule

print(divide(10 , 2))



# Python怎麼知道mymodule在哪裡?
import sys     # python自帶的模組，解鎖某些清潔功能

# python 會先從當從路徑找尋有沒有 mymodule模組 ，如果找不到會再往下找，都查無結果則回傳Error
print(sys.path)
print(sys.modules)