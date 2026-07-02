# ============================================================
# LIBRARY MANAGEMENT SYSTEM
# ============================================================
# This program demonstrates:
# 1. Classes and Inheritance
# 2. Polymorphism and Method Overriding
# 3. Data Structures (Lists)
# 4. Conditionals
# 5. Error Handling
# 6. Text-Based Menu Interface
# ============================================================


# ============================================================
# BASE CLASS
# ============================================================
class LibraryItem:
    """
    Parent class representing a generic library item.

    Attributes:
        title (str): Title of the item
        author (str): Author/creator of the item
        year (int): Publication year
        available (bool): Availability status
    """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        # True means item can be borrowed
        self.available = True

    def display_info(self):
        """
        Displays common information shared by all library items.
        This method will be overridden in child classes.
        """

        status = "Available" if self.available else "Borrowed"

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Status: {status}")


# ============================================================
# BOOK CLASS (INHERITS FROM LibraryItem)
# ============================================================
class Book(LibraryItem):
    """
    Child class representing a book.

    Additional attribute:
        genre (str)
    """

    def __init__(self, title, author, year, genre):
        # Call parent constructor
        super().__init__(title, author, year)

        self.genre = genre

    # Method overriding (Polymorphism)
    def display_info(self):
        """
        Overrides LibraryItem.display_info() to include book-specific information.
        """

        status = "Available" if self.available else "Borrowed"

        print("\n--- Book Information ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
        print(f"Status: {status}")


# ============================================================
# MAGAZINE CLASS (INHERITS FROM LibraryItem)
# ============================================================
class Magazine(LibraryItem):
    """
    Child class representing a magazine.

    Additional attribute:
        issue_number (int)
    """

    def __init__(self, title, author, year, issue_number):
        # Call parent constructor
        super().__init__(title, author, year)

        self.issue_number = issue_number

    # Method overriding (Polymorphism)
    def display_info(self):
        """
        Overrides LibraryItem.display_info() to include magazine-specific information.
        """

        status = "Available" if self.available else "Borrowed"

        print("\n--- Magazine Information ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Issue Number: {self.issue_number}")
        print(f"Status: {status}")


# ============================================================
# LIBRARY CLASS
# ============================================================
class Library:
    """
    Manages all library operations.
    Uses a list as the primary data structure for storing library items.
    """

    def __init__(self):
        self.items = []

    # --------------------------------------------------------
    # ADD ITEM
    # --------------------------------------------------------
    def add_item(self, item):
        """
        Adds a Book or Magazine object to the library.
        """

        self.items.append(item)
        print(f"\n'{item.title}' added successfully.")

    # --------------------------------------------------------
    # REMOVE ITEM
    # --------------------------------------------------------
    def remove_item(self, title):
        """
        Removes an item by title.
        """

        for item in self.items:
            if item.title.lower() == title.lower():
                self.items.remove(item)
                print(f"\n'{title}' removed successfully.")
                return

        print("\nItem not found.")

    # --------------------------------------------------------
    # VIEW AVAILABLE ITEMS
    # --------------------------------------------------------
    def view_available_items(self):
        """
        Displays all items that are currently available.
        """

        available_items = [item for item in self.items if item.available]

        if not available_items:
            print("\nNo available items.")
            return

        print("\n===== AVAILABLE ITEMS =====")

        for item in available_items:
            item.display_info()

    # --------------------------------------------------------
    # BORROW ITEM
    # --------------------------------------------------------
    def borrow_item(self, title):
        """
        Allows a user to borrow an item.

        Conditions:
        - Item must exist.
        - Item must be available.
        """

        for item in self.items:

            if item.title.lower() == title.lower():

                if item.available:
                    item.available = False
                    print(f"\nYou borrowed '{item.title}'.")
                else:
                    print("\nItem is already borrowed.")

                return

        print("\nItem does not exist.")

    # --------------------------------------------------------
    # RETURN ITEM
    # --------------------------------------------------------
    def return_item(self, title):
        """
        Returns an item to the library.

        Conditions:
        - Item must exist.
        - Item must currently be borrowed.
        """

        for item in self.items:

            if item.title.lower() == title.lower():

                if not item.available:
                    item.available = True
                    print(f"\nYou returned '{item.title}'.")
                else:
                    print("\nThis item was not borrowed.")

                return

        print("\nItem does not exist.")

    # --------------------------------------------------------
    # SEARCH ITEM
    # --------------------------------------------------------
    def search_item(self, keyword):
        """
        Search by title or author.

        Returns all matching results.
        """

        results = []

        for item in self.items:

            if (keyword.lower() in item.title.lower() or
                    keyword.lower() in item.author.lower()):
                results.append(item)

        if not results:
            print("\nNo matching items found.")
            return

        print("\n===== SEARCH RESULTS =====")

        for item in results:
            item.display_info()

    # --------------------------------------------------------
    # DISPLAY ALL ITEMS
    # --------------------------------------------------------
    def display_all_items(self):
        """
        Displays every item in the library.
        Demonstrates polymorphism because each object
        calls its own version of display_info().
        """

        if not self.items:
            print("\nLibrary is empty.")
            return

        print("\n===== ALL LIBRARY ITEMS =====")

        for item in self.items:
            item.display_info()


# ============================================================
# MENU FUNCTION
# ============================================================
def display_menu():
    """
    Prints the main menu.
    """

    print("\n")
    print("========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Add Magazine")
    print("3. Remove Item")
    print("4. Borrow Item")
    print("5. Return Item")
    print("6. View Available Items")
    print("7. Search Item")
    print("8. View All Items")
    print("9. Exit")
    print("===============================================")


# ============================================================
# MAIN PROGRAM
# ============================================================
def main():

    library = Library()

    # Sample data
    library.add_item(Book(
        "Python Programming",
        "John Smith",
        2023,
        "Technology"
    ))

    library.add_item(Book(
        "The Great Gatsby",
        "F. Scott Fitzgerald",
        1925,
        "Classic Fiction"
    ))

    library.add_item(Magazine(
        "Science Weekly",
        "Editorial Team",
        2024,
        101
    ))

    # Infinite loop until user exits
    while True:

        display_menu()

        try:
            choice = input("Enter your choice: ")

            # ------------------------------------------------
            # ADD BOOK
            # ------------------------------------------------
            if choice == "1":

                title = input("Title: ")
                author = input("Author: ")
                year = int(input("Year: "))
                genre = input("Genre: ")

                new_book = Book(
                    title,
                    author,
                    year,
                    genre
                )

                library.add_item(new_book)

            # ------------------------------------------------
            # ADD MAGAZINE
            # ------------------------------------------------
            elif choice == "2":

                title = input("Title: ")
                author = input("Author: ")
                year = int(input("Year: "))
                issue_number = int(input("Issue Number: "))

                new_magazine = Magazine(
                    title,
                    author,
                    year,
                    issue_number
                )

                library.add_item(new_magazine)

            # ------------------------------------------------
            # REMOVE ITEM
            # ------------------------------------------------
            elif choice == "3":

                title = input("Enter title to remove: ")
                library.remove_item(title)

            # ------------------------------------------------
            # BORROW ITEM
            # ------------------------------------------------
            elif choice == "4":

                title = input("Enter title to borrow: ")
                library.borrow_item(title)

            # ------------------------------------------------
            # RETURN ITEM
            # ------------------------------------------------
            elif choice == "5":

                title = input("Enter title to return: ")
                library.return_item(title)

            # ------------------------------------------------
            # VIEW AVAILABLE ITEMS
            # ------------------------------------------------
            elif choice == "6":

                library.view_available_items()

            # ------------------------------------------------
            # SEARCH ITEM
            # ------------------------------------------------
            elif choice == "7":

                keyword = input(
                    "Enter title or author to search: "
                )

                library.search_item(keyword)

            # ------------------------------------------------
            # VIEW ALL ITEMS
            # ------------------------------------------------
            elif choice == "8":

                library.display_all_items()

            # ------------------------------------------------
            # EXIT
            # ------------------------------------------------
            elif choice == "9":

                print("\nThank you for using the system.")
                break

            else:
                print("\nInvalid menu option.")

        # Handles invalid integer conversions
        except ValueError:
            print("\nInvalid input. Please enter valid data.")

        # General exception handling
        except Exception as e:
            print(f"\nUnexpected error: {e}")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main()