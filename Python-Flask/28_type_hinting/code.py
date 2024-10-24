
from typing import List

# 提示資料類型應該是哪一種 ，傳入應為list ，傳出值為float
def list_avg(sequence : List) -> float:
    return sum(sequence) / len(sequence)

print(list_avg([1,2,3]))


# 善用提示類型可以幫助寫code，減少出錯的機率
class Book():
    def __init__(self, name : str , number = int):
        self.name = name
        self.number = number


