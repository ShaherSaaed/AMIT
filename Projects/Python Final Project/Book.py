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
        self.borrowing_history = []

    def update_borrwing_history(self, borrower):
        self.borrowing_history.append({'Title' : self.title, 'ISBN' : self._ISBN, 'Borrower' : borrower, 'Date' : time.asctime()}) #FIXME:

    def clear_borrowing_history(self):
        self.borrowing_history.clear()

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author:  {self.author}")
        print(f"ISBN: {self._ISBN}")
        print(f"Genre: {self.genre}")
        print(f"Publisher: {self.publisher}")
        print(f"Publish Year: {self.publish_year}")
        print(f"Is borrowed: {self.is_borrowed}")
        print(f"Borrowing history: {self.borrowing_history}")