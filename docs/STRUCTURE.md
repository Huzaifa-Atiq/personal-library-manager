# 🏗️ Project Structure: Personal Library Manager

This document explains the folder and file structure of the **Personal Library Manager** project.
It helps you understand how the app is organized, how each module interacts, and where to find the main logic.

---

## 📂 Root Directory

| File/Folder        | Description                                                            |
| ------------------ | ---------------------------------------------------------------------- |
| `.gitignore`       | Specifies files and folders to be ignored by Git.                      |
| `main.py`          | Entry point of the app; launches the CLI interface.                    |
| `README.md`        | Main documentation and usage guide for the project.                    |
| `LICENSE`          | License file (MIT or custom).                                          |
| `requirements.txt` | Dependencies (if external packages are needed).                        |
| `docs/`            | Folder for documentation files such as `STRUCTURE.md`.                 |
| `json/`            | Stores persistent data (`library_data.json`) for books in JSON format. |
| `src/`             | Contains the core logic and app modules.                               |
| `storage/`         | Handles data persistence (save/load from JSON).                        |
| `ui/`              | Contains user interface components for CLI display.                    |

---

## 📂 src Directory

| File               | Responsibility                                                                          |
| ------------------ | --------------------------------------------------------------------------------------- |
| `library_core.py`  | Main logic of the app — manages books (add, remove, search, update, summary).           |
| `search_module.py` | Provides searching utilities for finding books by title (case-insensitive match, etc.). |
| `cli.py`           | Command-line interface controller; manages user input, menus, and interactions.         |
| `__init__.py`      | Marks `src` as a Python package.                                                        |

### ⚙️ `Library` class (`library_core.py`)

This is the **heart of the app**.
It connects to `FileStorage` for saving/loading data and uses `SearchEngine` for searching titles.
Handles all library operations such as:

* Adding new books 📚
* Listing all books 📋
* Searching by title 🔍
* Removing and updating records 🗑️ ✏️
* Showing total and author count 📊

---

## 📂 storage Directory

| File              | Responsibility                                             |
| ----------------- | ---------------------------------------------------------- |
| `file_storage.py` | Handles file operations (save and load book data to JSON). |
| `__init__.py`     | Marks the folder as a Python package.                      |

### 🧠 How it works:

* On app start, it **loads data** from `json/library_data.json`.
* When you add, remove, or update a book, it **writes back to file** (persistent storage).
* Uses `json` and `os` modules for safe reading/writing and file existence checks.

---

## 📂 ui Directory

| File             | Responsibility                                                                    |
| ---------------- | --------------------------------------------------------------------------------- |
| `cli_display.py` | Handles **printing** to the console — menus, headers, book lists, summaries, etc. |
| `__init__.py`    | Marks this directory as a package.                                                |

### 💅 `Display` class (`cli_display.py`)

Centralized display manager for all CLI outputs.
Formats messages consistently using emojis, headers, and separators.
Provides static methods:

* `menu()` – shows main menu
* `list_books()` – displays all books
* `search_results()` – shows search matches
* `summary()` – prints total and unique authors
* `success()`, `warning()`, `info()` – unified message style

---

## 📂 json Directory

| File                | Description                                               |
| ------------------- | --------------------------------------------------------- |
| `library_data.json` | The data file storing all books (auto-created if absent). |

---

## 🧩 Execution Flow Overview

1. **`main.py`** starts the app → creates a `LibraryApp()` instance.
2. `LibraryApp` (from `src/cli.py`) initializes a `Library()` object.
3. `Library` loads saved data via `FileStorage`.
4. User interacts with the menu — each option calls a method in `Library`.
5. All results are shown through the `Display` class for a clean CLI UI.

---

## 🧱 Design Principles

* **Modular Design:** Each concern (data, logic, UI) lives in its own folder.
* **Single Responsibility:** Every file/class has one clear job.
* **Persistence:** Data is automatically saved/loaded via JSON.
* **User-Friendly CLI:** Colored emojis and headers for clarity.

---

## 📝 Notes

* You can easily extend this project — for example, add a **genre** field, or implement a **search by author**.
* Folders follow a **clean MVC-like separation**:

  * `src/` → Logic (Controller + Model)
  * `ui/` → View
  * `storage/` → Persistence Layer
* Great base for scaling into a GUI or web app later using Flask or Django. 🚀

---

*Last updated: Nov 2025*
