# 合成  ，比遺傳更常用到，遺傳的限制較多，需要兩者之間有關聯性，像是書和書架就不適合用遺傳

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    
book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book , book2)

print(shelf)
print(shelf.books)












