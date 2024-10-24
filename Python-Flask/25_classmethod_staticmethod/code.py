
class ClassTest:
    # 需要創建類才能呼叫method
    def instance_method(self):
        print(f"Called iinstance_method of {self} ")

    # class method
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls} ")

    # static method 靜態方法 ，不常使用
    def static_method():
        print(f"Called static method. ")


test = ClassTest()
test.instance_method()

# 類方法
ClassTest.class_method()

# static method 
ClassTest.static_method()




#--- class method 應用 -------

class Book:
    TYPES = ("hardcover" , "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"< Book {self.name} , {self.book_type} , weight {self.weight}g >"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
        return Book(name, Book.TYPES[0], page_weight + 100)       # 建議使用 cls 進行回傳

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
    

# 一般用法
book = Book("Harry Potter" , "hardcover" , 1500)
print(book.name)
print(book)


# 想要區分書本類型，使用class method
hard_book = Book.hardcover("Harry Potter", 1500)
print(hard_book)

paper_book = Book.paperback("Python 3.1", 600)
print(paper_book)




