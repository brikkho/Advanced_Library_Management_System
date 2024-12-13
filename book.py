import add_books
import view_all_books
import restore_books_file
from datetime import datetime
import update_book_file, delete_book_file
import lend_book_file

def main():
    print("----------Library Management System----------")
    print("***************************************************")
  
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend Book")
    print("6. Return Book")
    print("0. Exit\n")
    
    all_books = []
    
    while True:
        all_books = restore_books_file.restore_all_books(all_books)
        choice = input("Enter your choice: ")
        if choice == "1":
            all_books = add_books.add_books(all_books)
        elif choice == "2":
            view_all_books.view_all_books(all_books)
        elif choice == "3":
            update_book_file.update_books(all_books)
        elif choice == "4":
            delete_book_file.delete_books(all_books)
        elif choice == "5":
            lend_book_file.lend_book(all_books)
        elif choice == "6":
            lend_book_file.return_book(all_books)
            
        elif choice == "0":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
