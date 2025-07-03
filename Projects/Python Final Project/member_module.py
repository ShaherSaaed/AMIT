from user_module import User
from book_module import Book
import time

class Member(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.borrowed_books = []
        
    def borrow_books(self, *books):
        for book in books:
            if book.is_borrowed:
                print(f"Can't borrow {book.title} at the moment as the book is already borrowed.")
            elif book in self.borrowed_books:
                print("You already have the book, please return it first.")
            elif len(self.borrowed_books) == 3:
                print("You have reached your maximum allowance of three borrowed books, please return a book first.")
            else:
                self.borrowed_books.append({'Book' : book.title, 'Borrowing date' : time.asctime()})
                book.borrowing_history.append({'Book' : book.title, 'Borrowing date' : time.asctime()})
                is_borrowed = True
                print(f"Borrowed {book.title}.")

        
    def return_books(self, *books):
        for book in books:
            if book not in self.borrowed_books:
                print("Book is not borrowed.")
            else:
                self.borrowed_books.remove(book.title)
                book.is_borrowed = False
                print(f"Returned {book.title} back to the shelves.")

