from book_module import Book
from admin_module import Admin

class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []
        self.admins = []
        self.members = []
        self.IDs = []

    def add_books(self, *books):
        for book in books:
            if book in self.available_books:
                print(f"{book.title} is already available.")
            else:
                self.available_books.append(book)
                print(f"Added book: {book.title} to the shelves.")

    def remove_books(self, *books):
        for book in books:
            if book not in self.available_books:
                print(f"{book.title} is not available, please add it first.")
            else:
                self.available_books.remove(book.title)
                print(f"Removed book: {book.title} from the shelves.")

    def add_members(self, *members):
        for member in members:
            if member.get_id() not in self.IDs:
                self.members.append(member)
                self.IDs.append(member.get_id())
                print(f"{member.last_name}, {member.first_name} added successfully.")
            else:
                print(f"You are already registred with ID: {member.get_id}.")

    def remove_members(self, *members):
        for member in members:
            if member.get_id() in self.IDs:
                self.members.remove(member)
                print(f"Successfully removed {member.last_name}, {member.first_name}.")
            else:
                print(f"{member.last_name}, {member.first_name} is not registered.")
