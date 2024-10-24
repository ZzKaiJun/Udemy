# python中， 兩邊各有 __ 是特殊方法，也被稱為 magic method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 當想把對象轉成字符串，比如打印 就會執行
    def __str__(self):
        return f"Person {self.name} , {self.age} years old.  "
    
    # 與　__str__ 類似，但會優先採用 __str__，用於打印對象的明確表示
    def __repr__(self):
        return f"<Person('{self.name}' , {self.age})>"


bob = Person("Bob" , 25)

print(bob)

