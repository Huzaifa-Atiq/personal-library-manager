# library_core.py
# This module defines the Library class which manages book records.

from src.search_module import SearchEngine
from storage.file_storage import FileStorage

class Library:
    def __init__(self):
        self.storage = FileStorage()
        self.books = self.storage.load_data()

    def save(self):
        self.storage.save_data(self.books)

    def add_book(self, title, author, year):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
                return {"success": False, "message": f" Book '{title}' by {author} already exists!"}

        new_book = {"title": title, "author": author, "year": year}
        self.books.append(new_book)
        self.save()
        return {"success": True, "message": f"Added '{title}' by {author} ({year})."}

    def list_books(self):
        if not self.books:
            return {"success": False, "message": "The library is empty."}
        return {"success": True, "books": self.books}

    def search_book(self, title):
        results = SearchEngine.find_by_title(self.books, title)
        if results:
            return {"success": True, "results": results}
        return {"success": False, "message": f"No book found with title '{title}'."}

    def remove_book(self, title):
        results = SearchEngine.find_by_title(self.books, title)
        if not results:
            return {"success": False, "message": f"No book found with the title '{title}' to remove."}

        if len(results) > 1:
            return {"success": False, "message": "Multiple books match. Removal requires interactive choice."}

        book = results[0]
        self.books.remove(book)
        self.save()
        return {"success": True, "message": f"Removed '{book['title']}' successfully."}

    def update_book(self, title, new_title=None, new_author=None, new_year=None):
        results = SearchEngine.find_by_title(self.books, title)
        if not results:
            return {"success": False, "message": f"No book found with the title '{title}' to update."}

        book = results[0]
        if new_title: book['title'] = new_title
        if new_author: book['author'] = new_author
        if new_year: book['year'] = new_year

        self.save()
        return {"success": True, "message": f"Book '{book['title']}' updated successfully."}

    def show_summary(self):
        if not self.books:
            return {"success": False, "message": " Library is empty!"}
        total = len(self.books)
        authors = len(set(b['author'] for b in self.books))
        return {"success": True, "total": total, "authors": authors}
