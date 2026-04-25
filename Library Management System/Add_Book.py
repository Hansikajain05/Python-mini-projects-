from utils import books
def add_book():
    book_name = input("Enter Book Name to add :").strip().upper()
    books.append(book_name)
    print(f"Book {book_name} has been added")