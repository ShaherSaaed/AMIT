from library_module import Library
from book_module import Book
from admin_module import Admin
from member_module import Member
import time

def display_menu(role):
    """Display menu based on user role"""
    print("\n" + "="*50)
    print(f"{'Library Management System':^50}")
    print("="*50)
    print(f"Logged in as: {role}")
    
    if role == "Admin":
        print("1. Add Books to Library")
        print("2. Remove Books from Library")
        print("3. Add Members")
        print("4. Remove Members")
        print("5. View All Books")
        print("6. View All Members")
        print("7. Exit")
    else:  # Member
        print("1. Borrow Books")
        print("2. Return Books")
        print("3. View My Borrowed Books")
        print("4. View All Available Books")
        print("5. Exit")

def create_sample_data(library):
    """Create some sample data for testing"""
    # Create sample books
    book1 = Book("Python Crash Course", "Eric Matthes", "Programming", "No Starch Press", 2019, False, "978-1593279288")
    book2 = Book("Clean Code", "Robert Martin", "Programming", "Prentice Hall", 2008, False, "978-0132350884")
    book3 = Book("The Pragmatic Programmer", "Andrew Hunt", "Programming", "Addison-Wesley", 1999, False, "978-0201616224")
    
    # Add books to library
    library.add_books(book1, book2, book3)
    
    # Create sample admin
    admin = Admin("Library", "Admin", 35)
    
    # Create sample members
    member1 = Member("John", "Doe", 25)
    member2 = Member("Jane", "Smith", 30)
    
    # Add members to library
    library.add_members(member1, member2)
    
    return admin, member1

def main():
    print("Welcome to the Library Management System")
    
    # Initialize library and create sample data
    library = Library()
    admin, member = create_sample_data(library)
    
    while True:
        # Login screen
        print("\n" + "="*50)
        print(f"{'Login':^50}")
        print("="*50)
        print("1. Admin Login")
        print("2. Member Login")
        print("3. Exit System")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            # Admin login
            current_user = admin
            role = "Admin"
            
            while True:
                display_menu(role)
                choice = input("Enter your choice (1-7): ")
                
                if choice == "1":
                    # Add Books
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    genre = input("Enter genre: ")
                    publisher = input("Enter publisher: ")
                    publish_year = int(input("Enter publish year: "))
                    isbn = input("Enter ISBN: ")
                    
                    new_book = Book(title, author, genre, publisher, publish_year, False, isbn)
                    admin.add_books_to_library(library, new_book)
                    
                elif choice == "2":
                    # Remove Books
                    print("\nAvailable Books:")
                    for i, book in enumerate(library.available_books, 1):
                        print(f"{i}. {book.title} by {book.author}")
                    
                    try:
                        book_num = int(input("Enter book number to remove: ")) - 1
                        if 0 <= book_num < len(library.available_books):
                            admin.remove_books(library, library.available_books[book_num])
                        else:
                            print("Invalid book number!")
                    except ValueError:
                        print("Please enter a valid number!")
                
                elif choice == "3":
                    # Add Members
                    first_name = input("Enter member's first name: ")
                    last_name = input("Enter member's last name: ")
                    age = int(input("Enter member's age: "))
                    
                    new_member = Member(first_name, last_name, age)
                    library.add_members(new_member)
                
                elif choice == "4":
                    # Remove Members
                    if not library.members:
                        print("No members registered!")
                        continue
                        
                    print("\nRegistered Members:")
                    for i, member in enumerate(library.members, 1):
                        print(f"{i}. {member.first_name} {member.last_name}")
                    
                    try:
                        member_num = int(input("Enter member number to remove: ")) - 1
                        if 0 <= member_num < len(library.members):
                            library.remove_members(library.members[member_num])
                        else:
                            print("Invalid member number!")
                    except ValueError:
                        print("Please enter a valid number!")
                
                elif choice == "5":
                    # View All Books
                    print("\nAll Books in Library:")
                    print("-"*50)
                    for i, book in enumerate(library.available_books, 1):
                        print(f"{i}. {book.title} by {book.author}")
                        print(f"   ISBN: {book._ISBN}, Available: {not book.is_borrowed}")
                    print("-"*50)
                    for i, book in enumerate(library.borrowed_books, len(library.available_books)+1):
                        print(f"{i}. {book.title} by {book.author}")
                        print(f"   ISBN: {book._ISBN}, Available: {not book.is_borrowed}")
                
                elif choice == "6":
                    # View All Members
                    print("\nRegistered Members:")
                    print("-"*50)
                    for i, member in enumerate(library.members, 1):
                        print(f"{i}. {member.first_name} {member.last_name}")
                        print(f"   Age: {member.age}, ID: {member.get_id()}")
                
                elif choice == "7":
                    print("Logging out as Admin...")
                    break
                
                else:
                    print("Invalid choice! Please try again.")
                
                input("\nPress Enter to continue...")
        
        elif choice == "2":
            # Member login
            if not library.members:
                print("No members registered yet!")
                continue
                
            print("\nAvailable Members:")
            for i, member in enumerate(library.members, 1):
                print(f"{i}. {member.first_name} {member.last_name}")
            
            try:
                member_num = int(input("Select member (enter number): ")) - 1
                if 0 <= member_num < len(library.members):
                    current_user = library.members[member_num]
                    role = "Member"
                else:
                    print("Invalid member number!")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                continue
            
            while True:
                display_menu(role)
                choice = input("Enter your choice (1-5): ")
                
                if choice == "1":
                    # Borrow Books
                    available_books = [b for b in library.available_books if not b.is_borrowed]
                    if not available_books:
                        print("No books available for borrowing!")
                        continue
                        
                    print("\nAvailable Books:")
                    for i, book in enumerate(available_books, 1):
                        print(f"{i}. {book.title} by {book.author}")
                    
                    try:
                        book_nums = input("Enter book numbers to borrow (comma separated): ")
                        book_nums = [int(num.strip())-1 for num in book_nums.split(",")]
                        
                        for num in book_nums:
                            if 0 <= num < len(available_books):
                                current_user.borrow_books(available_books[num])
                                library.borrowed_books.append(available_books[num])
                                library.available_books.remove(available_books[num])
                            else:
                                print(f"Invalid book number: {num+1}")
                    except ValueError:
                        print("Please enter valid numbers!")
                
                elif choice == "2":
                    # Return Books
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                        continue
                        
                    print("\nYour Borrowed Books:")
                    for i, book in enumerate(current_user.borrowed_books, 1):
                        print(f"{i}. {book['Book']} borrowed on {book['Borrowing date']}")
                    
                    try:
                        book_nums = input("Enter book numbers to return (comma separated): ")
                        book_nums = [int(num.strip())-1 for num in book_nums.split(",")]
                        
                        for num in book_nums:
                            if 0 <= num < len(current_user.borrowed_books):
                                book_title = current_user.borrowed_books[num]['Book']
                                # Find the actual book object
                                for book in library.borrowed_books:
                                    if book.title == book_title:
                                        current_user.return_books(book)
                                        library.available_books.append(book)
                                        library.borrowed_books.remove(book)
                                        break
                            else:
                                print(f"Invalid book number: {num+1}")
                    except ValueError:
                        print("Please enter valid numbers!")
                
                elif choice == "3":
                    # View My Borrowed Books
                    if not current_user.borrowed_books:
                        print("You haven't borrowed any books!")
                    else:
                        print("\nYour Borrowed Books:")
                        print("-"*50)
                        for i, book in enumerate(current_user.borrowed_books, 1):
                            print(f"{i}. {book['Book']}")
                            print(f"   Borrowed on: {book['Borrowing date']}")
                
                elif choice == "4":
                    # View All Available Books
                    available_books = [b for b in library.available_books if not b.is_borrowed]
                    if not available_books:
                        print("No books available at the moment!")
                    else:
                        print("\nAvailable Books:")
                        print("-"*50)
                        for i, book in enumerate(available_books, 1):
                            print(f"{i}. {book.title} by {book.author}")
                            print(f"   Genre: {book.genre}, Year: {book.publish_year}")
                
                elif choice == "5":
                    print("Logging out as Member...")
                    break
                
                else:
                    print("Invalid choice! Please try again.")
                
                input("\nPress Enter to continue...")
        
        elif choice == "3":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()