import User
import time
import Book

class Member(User):
    def __init__(self):
        super().__init__()
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if Book.is_borrowed:
            raise("Can't borrow at the moment as the book is already borrowed.")
        elif book in self.borrowed_books:
            raise("Book already borrowed.")
        else:
            self.borrowed_books.append({'Book' : book, 'Borrowing date' : time.asctime()})
            Book.borrowing_history.append({'Book' : book, 'Borrowing date' : time.asctime()})
            is_borrowed = True

        
    def return_book(self, book):
        if book not in self.borrowed_books():
            raise("Book is not borrowed")
        else:
            self.borrowed_books.remove(book['Book'])
            is_borrowed = False

