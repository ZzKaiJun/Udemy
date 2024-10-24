# 將多個參數集合到一個變量的方法
def multiply(*args):       #乘法
    print(*args)
    total = 1
    for arg in args:
        total = total * arg
    
    return total

print(multiply(1,3,5))


# 將一個參數轉成多個變量，但是 argument 數量也要一樣
def add(x,y):
    return x+y

num = [3, 5]
print(add(*num))


# 字典的使用方法 key名稱和參數名稱一樣

nums = {"x":3 , "y":5}
print(add(x=nums["x"], y=nums["y"]))   #原先寫法
print(add(**nums))



# 所有位置參數集中到元組args，並且最後還有一個命名參數
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)      #需要加上 *  
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply(). "
    
print(apply(1,3,5,7, operator="+"))
print(apply(1,3,5,7, operator="*"))
