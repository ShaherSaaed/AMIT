import time
import Member

def main():
    while True:
        print("\n--- Member Menu ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Available Books")
        print("4. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            book = input("Enter the book's name: ")
            Member.borrow_book(book)
        elif choice == '2':
            book = input("Enter the book's name: ")
            Member.return_book(book)

        

if __name__ == '__main__':
    main()