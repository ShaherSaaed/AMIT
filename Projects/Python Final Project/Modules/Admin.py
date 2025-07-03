from user_module import User
from library_module import Library

class Admin(User):
    
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def add_books_to_library(self, library, *books):
        for book in books:
            library.add_books(*books)
            print(f"Added book: {book.title} to the shelves.")

    def remove_books(self, library, *books):
        for book in books:
            library.remove_books(*book)
            print(f"Removed book: {book.title} from the shelves.")