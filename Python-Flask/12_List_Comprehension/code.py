# 要取得原本列表的2倍作為新列表，傳統只能寫 for迴圈 慢慢填入值
numbers = [1 ,3, 5]
doubles = []

for num in numbers:
    doubles.append(num * 2)


# python 中能使用 列表解析 list comprehension 快速達到此目的
'''
1. 把想加的值放入列表中                   doubles = [num * 2]    
2. for 循環加入列表中                    doubles = [num * 2 for num in numbers]    
3. python 會把 num * 2 放入列表中        doubles = [2, 6, 10]    
'''

numbers = [1, 3, 5]
doubles = [num * 2 for num in numbers]

print(doubles)



# --------------------

# example2:
friends = ["Sam", "AMB", "ccf", "Sofia", "Sandy"]
start_s = []

for friend in friends:
    if friend.startswith("S"):
        start_s.append(friend)

# 使用列表解析
'''
1. 把想加的值放入列表中                   start_s = [friend]    
2. for 循環加入列表中                    start_s = [friend for friend in friends]    
3. 添加 if 判斷條件                      start_s = [friend for friend in friends if friend.startswith("S")] 
3. python 會把 num * 2 放入列表中        start_s = ['Sam', 'Sofia', 'Sandy']    
'''

friends = ["Sam", "AMB", "ccf", "Sofia", "Sandy"]
start_s = [friend for friend in friends if friend.startswith("S")]

print(start_s)