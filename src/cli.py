# cli.py

from ui.cli_display import Display
from src.library_core import Library

class LibraryApp:
    def __init__(self):
        self.library = Library()

    def main_menu(self):
        while True:
            Display.menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == '1':
                title = input("Enter the book title (or 'cancel'): ")
                if title.lower() == 'cancel':
                    Display.info("↩️  Returning to main menu.")
                    continue

                author = input("Enter the author’s name (or 'cancel'): ")
                if author.lower() == 'cancel':
                    Display.info("↩️  Returning to main menu.")
                    continue

                year = self.get_valid_year()
                if year is None:
                    Display.info("↩️  Returning to main menu.")
                    continue

                result = self.library.add_book(title, author, year)
                if result["success"]:
                    Display.success(result["message"])
                else:
                    Display.warning(result["message"])

            elif choice == '2':
                result = self.library.list_books()
                if result["success"]:
                    Display.list_books(result["books"])
                else:
                    Display.warning(result["message"])

            elif choice == '3':
                title = input("Enter title to search (or 'cancel'): ")
                if title.lower() == 'cancel':
                    Display.info("↩️  Returning to main menu.")
                    continue
                
                result = self.library.search_book(title)
                if result["success"]:
                    Display.search_results(result["results"])
                else:
                    Display.warning(result["message"])

            elif choice == '4':
                title = input("Enter title to remove (or 'cancel'): ")
                if title.lower() == 'cancel':
                    Display.info("↩️  Returning to main menu.")
                    continue
                result = self.library.remove_book(title)
                if result["success"]:
                    Display.success(result["message"])
                else:
                    Display.warning(result["message"])

            elif choice == '5':
                title = input("Enter title to update (or 'cancel'): ")
                if title.lower() == 'cancel':
                    Display.info("↩️  Returning to main menu.")
                    continue
                
                new_title = input("Enter new title (or leave empty): ").strip()
                new_author = input("Enter new author (or leave empty): ").strip()
                new_year = input("Enter new year (or leave empty): ").strip()

                new_year = int(new_year) if new_year.isdigit() else None

                result = self.library.update_book(
                    title,
                    new_title=new_title or None,
                    new_author=new_author or None,
                    new_year=new_year
                )

                if result["success"]:
                    Display.success(result["message"])
                else:
                    Display.warning(result["message"])
                
                result = self.library.search_book(title)
                if result["success"]:
                    Display.search_results(result["results"])
                else:
                    Display.warning(result["message"])

            elif choice == '6':
                summary = self.library.show_summary()
                if summary["success"]:
                    Display.summary(summary["total"], summary["authors"])
                else:
                    Display.warning(summary["message"])

            elif choice == '7':
                Display.info("Goodbye! See you next time!")
                break

            else:
                Display.warning("Invalid choice! Try again.")

    def get_valid_year(self):
        while True:
            year = input("Enter publication year (or 'cancel'): ").strip()
            if year.lower() == 'cancel':
                return None
            if year.isdigit() and 1000 <= int(year) <= 2025:
                return int(year)
            Display.warning("Invalid year! Must be a number between 1000 and 2025, or type 'cancel'.")

