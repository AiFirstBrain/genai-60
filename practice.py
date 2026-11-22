class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages  
    def describe(self):
        return f"{self.title} ({self.pages} pages)"      
b1 = Book("python 101", 250)
b2 = Book("Ai Basics", 180)
print(b1.title)
print(b2.pages)
print(b1.describe())
print(b1.describe)
print(Book.describe(b1))