#
default_y = 3

def add(x, y=default_y):   #不好的寫法，因為y的值只會抓 funtion 創建的數值，之後更改不會影響 default_y
    sum = x+y
    print(sum)

add(2)

default_y = 4
add(2)
