class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' has been added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' has been removed from the library.")
        else:
            print(f"Book '{book}' is not available in the library.")

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

    def search_book(self, keyword):
        results = []
        keyword = keyword.lower()
        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book)
        if results:
            print(f"Search results for '{keyword}':")
            for book in results:
                print(book)
        else:
            print(f"No books found matching '{keyword}'.")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        availability = "Available" if self.available else "Not available"
        return f"{self.title} by {self.author} ({availability})"


def main():
    library_name = input("Enter the name of the library: ")
    library = Library(library_name)

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display books")
        print("4. Search for a book")
        print("5. Mark a book as borrowed")
        print("6. Mark a book as returned")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            title = input("Enter the title of the book: ")
            book = Book(title, "")
            library.remove_book(book)

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            keyword = input("Enter the title or author of the book to search: ")
            library.search_book(keyword)

        elif choice == "5":
            title = input("Enter the title of the book to mark as borrowed: ")
            found_book = None
            for book in library.books:
                if book.title.lower() == title.lower():
                    found_book = book
                    break
            if found_book:
                if found_book.available:
                    found_book.available = False
                    print(f"Book '{found_book}' has been marked as borrowed.")
                else:
                    print(f"Book '{found_book}' is already borrowed.")
            else:
                print(f"Book '{title}' is not available in the library.")

        elif choice == "6":
            title = input("Enter the title of the book to mark as returned: ")
            found_book = None
            for book in library.books:
                if book.title.lower() == title.lower():
                    found_book = book
                    break
            if found_book:
                if not found_book.available:
                    found_book.available = True
                    print(f"Book '{found_book}' has been marked as returned.")
                else:
                    print(f"Book '{found_book}' is already returned.")
            else:
                print(f"Book '{title}' is not available in the library.")

        elif choice == "7":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
