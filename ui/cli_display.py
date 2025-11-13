# ui/cli_display.py

class Display:
    """Handles pretty-printing for the CLI interface."""

    @staticmethod
    def header(title):
        line = "─" * (len(title) + 10)
        print(f"\n {line}")
        print(f"   📖 {title}")
        print(f"{line}")

    @staticmethod
    def menu():
        Display.header("Personal Library Manager")
        print("1️⃣  Add Book")
        print("2️⃣  List Books")
        print("3️⃣  Search Book")
        print("4️⃣  Remove Book")
        print("5️⃣  Update Book")
        print("6️⃣  Summary")
        print("7️⃣  Exit Program")
        print("─" * 50)

    @staticmethod
    def list_books(books):
        if not books:
            print("📭 No books found in your library yet.")
            return

        Display.header("Books in Library")
        for i, book in enumerate(books, start=1):
            print(f"#{i}  📘 {book['title']}")
            print(f"     ✍️  Author: {book['author']}")
            print(f"     🗓️  Year: {book['year']}\n")
        print("─" * 50)

    @staticmethod
    def search_results(matches):
        if not matches:
            print("❌ No matching books found.")
            return

        Display.header("Search Results")
        for book in matches:
            print(f"📗 {book['title']} - {book['author']} ({book['year']})")
        print("─" * 50)

    @staticmethod
    def summary(total, authors):
        Display.header("Library Summary")
        print(f"📊 Total Books: {total}")
        print(f"🧑‍💻 Unique Authors: {authors}")
        print("─" * 50)

    @staticmethod
    def success(message):
        print(f"✅ {message}")

    @staticmethod
    def warning(message):
        print(f"⚠️  {message}")

    @staticmethod
    def info(message):
        print(f"ℹ️  {message}")
