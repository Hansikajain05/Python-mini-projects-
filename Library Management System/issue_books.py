from utils import books, issued_books
def issue_book():
    if len(books) == 0:
        print("No Books Available..!!")
    else:
        book_name = input("Enter Book Name to issue :").strip().upper()
        if book_name in books:
            books.remove(book_name)
            issued_books.append(book_name)
            print(f"Book {book_name} issued successfully..!!")
        else:
            print(f"Book {book_name} is not available in library..!!")