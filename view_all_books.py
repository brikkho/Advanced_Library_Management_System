# def view_all_books(all_books):
    # if all_books != []:
    #     for book in all_books:
    #         print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
    # else:
    #     print("No Book found in program")

import json

def view_all_books(all_books):
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)

    if all_books != []:
        for book in all_books:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}\n")
        print(f"Total books in the Library as on todate: {len(all_books)}\n")
        #print(f"Total books available for lending as on {toDate}: {len(all_books)}")
    else:
        print("No Book found.\n")
