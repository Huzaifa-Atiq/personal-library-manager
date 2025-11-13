# storage/file_storage.py
# Module to handle saving and loading library data to/from JSON file

import json
import os

class FileStorage:
    def __init__(self, filepath="json/library_data.json"):
        self.filepath = filepath

    def save_data(self, books):
        """Save book list to JSON file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(books, f, indent=4, ensure_ascii=False)
            print("💾 Library data saved successfully.")
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def load_data(self):
        """Load book list from JSON file if it exists."""
        if not os.path.exists(self.filepath):
            print("\n📁 No existing data found, starting fresh.")
            return []
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                books = json.load(f)
            print(f"\n📂 Loaded {len(books)} books from file.")
            return books
        except Exception as e:
            print(f"\n❌ Error loading data: {e}")
            return []
