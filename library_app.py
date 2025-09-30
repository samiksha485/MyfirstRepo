# library_app.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"'{self.title}' by {self.author}"

book1 = Book("The Hobbit", "J.R.R. Tolkien")
print(book1.display_info())
