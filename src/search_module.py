# search_module.py
# 🔍 This module handles searching functionality for the library system.

class SearchEngine:
    """A simple search utility for books based on title."""

    @staticmethod
    def find_by_title(books, title):
        """Return list of matching books based on title substring (case-insensitive)."""
        matches = [book for book in books if title.lower() in book['title'].lower()]
        return matches
