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
# DVD CLASS (INHERITS FROM LibraryItem)
# ============================================================
class DVD(LibraryItem):
    """
    Child class representing a DVD in the library.

    Additional attribute:
        duration (int): Duration of the DVD in minutes
    """

    def __init__(self, title, author, year, duration):
        # Call parent constructor
        super().__init__(title, author, year)

        self.duration = duration

    # Method overriding (Polymorphism)
    def display_info(self):
        """
        Overrides LibraryItem.display_info() to include DVD-specific information.
        """

        status = "Available" if self.available else "Borrowed"

        print("\n--- DVD Information ---")
        print(f"Title: {self.title}")
        print(f"Director: {self.author}")
        print(f"Year: {self.year}")
        print(f"Duration: {self.duration} minutes")
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
    # ADD ITEM - Adds a Book or Magazine object to the library.
    # --------------------------------------------------------
    def add_item(self, item):
        self.items.append(item)
        print(f"\n'{item.title}' added successfully.")

    # --------------------------------------------------------
    # REMOVE ITEM - Removes an item from the library by title.
    # --------------------------------------------------------
    def remove_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                self.items.remove(item)
                print(f"\n'{title}' removed successfully.")
                return

        print("\nItem not found.")

    # --------------------------------------------------------
    # VIEW AVAILABLE ITEMS - Displays all items that are currently available for borrowing.
    # --------------------------------------------------------
    def view_available_items(self):
        available_items = [item for item in self.items if item.available]

        if not available_items:
            print("\nNo available items.")
            return

        print("\n===== AVAILABLE ITEMS =====")

        for item in available_items:
            item.display_info()

    # --------------------------------------------------------
    # BORROW ITEM from the library by title. Conditions: Item must exist. Item must be available.
    # --------------------------------------------------------
    def borrow_item(self, title):
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
    # RETURN ITEM to the library. Conditions: Item must exist. Item must currently be borrowed.
    # --------------------------------------------------------
    def return_item(self, title):
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


    # --------------------------------------------------------------
    # DISPLAY SORTED ITEMS
    # --------------------------------------------------------------
    def sort_items(self, sort_by):
        """
        Sorts library items by title, author or year.

        Parameters:
            sort_by (str): Attribute used for sorting.
                           Valid options:
                           "title"
                           "author"
                           "year"
        """

        # Check whether the user entered a valid option.
        if sort_by.lower() == "title":

            # Create a sorted copy of the list.
            sorted_items = sorted(
                self.items,
                key=lambda item: item.title.lower()
            )

        elif sort_by.lower() == "author":

            sorted_items = sorted(
                self.items,
                key=lambda item: item.author.lower()
            )

        elif sort_by.lower() == "year":

            sorted_items = sorted(
                self.items,
                key=lambda item: item.year
            )

        else:
            print("\nInvalid sorting option.")
            print("Please choose: title, author or year.")
            return

        # Display sorted results.
        print(f"\n===== ALL LIBRARY ITEMS SORTED BY {sort_by.upper()} =====")

        for item in sorted_items:
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
    print("3. Add DVD")
    print("4. Remove Item")
    print("5. Borrow Item")
    print("6. Return Item")
    print("7. View Available Items")
    print("8. Search Item")
    print("9. View All Items")
    print("10. View All Items Sorted")
    print("11. Exit")
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

    library.add_item(
        DVD(
            "Inception",
            "Christopher Nolan",
            2010,
            148
        )
    )

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
            # ADD DVD
            # ------------------------------------------------
            elif choice == "3":

                title = input("Title: ")
                director = input("Director: ")
                year = int(input("Year: "))
                duration = int(input("Duration (in minutes): "))

                new_dvd = DVD(
                    title,
                    director,
                    year,
                    duration
                )

                library.add_item(new_dvd)

            # ------------------------------------------------
            # REMOVE ITEM
            # ------------------------------------------------
            elif choice == "4":

                title = input("Enter title to remove: ")
                library.remove_item(title)

            # ------------------------------------------------
            # BORROW ITEM
            # ------------------------------------------------
            elif choice == "5":

                title = input("Enter title to borrow: ")
                library.borrow_item(title)

            # ------------------------------------------------
            # RETURN ITEM
            # ------------------------------------------------
            elif choice == "6":

                title = input("Enter title to return: ")
                library.return_item(title)

            # ------------------------------------------------
            # VIEW AVAILABLE ITEMS
            # ------------------------------------------------
            elif choice == "7":

                library.view_available_items()

            # ------------------------------------------------
            # SEARCH ITEM
            # ------------------------------------------------
            elif choice == "8":

                keyword = input(
                    "Enter title or author to search: "
                )

                library.search_item(keyword)

            # ------------------------------------------------
            # VIEW ALL ITEMS
            # ------------------------------------------------
            elif choice == "9":

                library.display_all_items()

            # ------------------------------------------------
            # VIEW ALL ITEMS SORTED
            # ------------------------------------------------
            elif choice == "10":

                print("\nSort Options")
                print("1. Title")
                print("2. Author")
                print("3. Year")

                option = input("Choose a sorting option: ")

                if option == "1":
                    library.sort_items("title")

                elif option == "2":
                    library.sort_items("author")

                elif option == "3":
                    library.sort_items("year")

                else:
                    print("\nInvalid sorting option.")

            # ------------------------------------------------
            # EXIT
            # ------------------------------------------------
            elif choice == "11":

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