from datetime import datetime
import json

def lend_book(all_books):
    borrower_name = input("Enter borrower's name: ")
    phone_number = input("Enter borrower's phone number: ")
    book_title = input("Enter the title of the book to lend: ")
    
    # Find the book
    for book in all_books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] > 0:
                due_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                lend_info = {
                    "name": borrower_name,
                    "phone": phone_number,
                    "title": book["title"],
                    "due_date": due_date
                }
                # Save to lend file
                with open("lend_info.json", "a") as lend_file:
                    lend_file.write(json.dumps(lend_info) + "\n")
                
                # Reduce book quantity
                book["quantity"] -= 1
                print(f"Book '{book['title']}' has been lent to {borrower_name}. Return due date: {due_date}")
                return
            else:
                print("There are not enough books available to lend.")
                return
    
    print("Book not found in the library.")

def return_book(all_books):
    book_title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter borrower's name: ")
    
    updated_lend_data = []
    book_found = False
    
    try:
        with open("lend_info.json", "r") as lend_file:
            lend_data = lend_file.readlines()
        
        with open("lend_info.json", "w") as lend_file:
            for entry in lend_data:
                lend_info = json.loads(entry)
                if lend_info["title"].lower() == book_title.lower() and lend_info["name"].lower() == borrower_name.lower():
                    book_found = True
                else:
                    updated_lend_data.append(lend_info)
                    lend_file.write(entry)
    except FileNotFoundError:
        print("No lending records found.")
        return
    
    if book_found:
        for book in all_books:
            if book["title"].lower() == book_title.lower():
                book["quantity"] += 1
                print(f"Book '{book['title']}' has been successfully returned.")
                return
    else:
        print("No matching lending record found.")
