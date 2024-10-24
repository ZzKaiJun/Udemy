# 繼承至ValueError
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name:str, page_count:int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name} , read {self.pages_read} pages out of {self.page_count} >"
        )

    def read(self, pages:int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {pages + self.pages_read} pages, but this book only have {self.page_count}"
            )
        self.pages_read = pages
        print(f"You have read {self.pages_read} pages out of {self.page_count}.")


python101 = Book("Python101" , 50)
HarryPotter = Book("HarryPotter", 80)
print(python101)
print(HarryPotter)

python101.read(35)
HarryPotter.read(50)
print(python101)
print(HarryPotter)

try:
    python101.read(20)
    HarryPotter.read(35)
except TooManyPagesReadError as e:
    print(e)
