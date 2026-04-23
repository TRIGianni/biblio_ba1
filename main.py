from models.Book import Book
from models.Library import Library

def main():
    lib = Library()
    lib.add_book(Book("1984", "George Orwell", 1949))
    lib.add_book(Book("Dune", "Frank Herbert", 1965))
    for book in lib.list_books():
        print(book)
 
if __name__ == "__main__":
    main()
