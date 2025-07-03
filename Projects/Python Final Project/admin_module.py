from user_module import User
from library_module import Library

class Admin(User):
    
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def add_books_to_library(self, library, book):
          library.add_books(book)

    def remove_books(self, library, book):
          library.remove_books(book)