def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubles = [x * 2 for x in sequence]  # 列表解析
doubles = [double(x) for x in sequence] # function方法
doubles = list(map(double, sequence))   # map 方法 ，某些語言沒有支援列表解析，可以使用map來達成效果
print(doubles)

# lambda 返回根據其參數計算出的值，用於map方法居多
doubles = [(lambda x:x*2)(x) for x in sequence]
doubles = list(map(lambda x:x*2, sequence))
print(doubles)
