import time

class Book:

    def __init__(self, title, author, genre, publisher, publish_year, is_borrowed, ISBN):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.publish_year = publish_year
        self._ISBN = ISBN
        self.is_borrowed = is_borrowed

    def update_borrwing_history(self, borrower):
        self.borrowing_history.append({'Title' : self.title, 'ISBN' : self._ISBN, 'Borrower' : borrower, 'Date' : time.asctime()}) #FIXME:

    def clear_borrowing_history(self):
        self.borrowing_history.clear()