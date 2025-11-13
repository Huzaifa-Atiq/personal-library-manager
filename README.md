# 📖 Personal Library Manager (CLI)

A simple command-line interface (CLI) application built in Python for managing a personal collection of books. It allows users to add, list, search, remove, and update book records, with data persisted to a JSON file.

---

## 📚 Table of Contents

* [📖 Personal Library Manager (CLI)](#-personal-library-manager-cli)

  * [🎥 Demo Video](#-demo-video)
  * [🚀 Getting Started](#-getting-started)

    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Run the Application](#run-the-application)
    * [How to Run](#how-to-run)
  * [📂 Project Structure Overview](#-project-structure-overview)
  * [✨ Features](#-features)

    * [Data Persistence](#data-persistence)
  * [🛠️ Key Classes and Methods](#️-key-classes-and-methods)
  * [🧪 Usage Examples](#-usage-examples)
  * [✅ Error Handling](#-error-handling)
  * [📦 Data Storage Details](#-data-storage-details)
  * [🧱 Limitations (Current)](#-limitations-current)
  * [🤝 Contributing](#-contributing)
  * [📝 Related Article](#-related-article)
  * [📜 License](#-license)
  * [🙋 About This Project](#-about-this-project)

---

## 🎥 Demo Video

Watch a demo session of **Python Library Manager** in action on YouTube:

[![Watch Tiny Hero Demo](https://img.youtube.com/vi/45JkMS5_JHc/0.jpg)](https://youtu.be/45JkMS5_JHc)

Or click the link directly: [Watch on YouTube](https://youtu.be/45JkMS5_JHc)

---

## 🚀 Getting Started

### Prerequisites

You only need **Python 3.10+** installed.
No external packages. No virtual environment required.

### Installation

Clone the repository:

```bash
git clone https://github.com/Sherouz/personal-library-manager.git
cd personal-library-manager
```

### Run the Application

```bash
python main.py
```

When the program starts, the main menu will appear, and you can begin managing your library.

### Prerequisites

To run this application, you only need **Python 3.x** installed on your system.

### How to Run

1. **Save the files:** Ensure all the provided Python files (`cli.py`, `main.py`, `src/library_core.py`, `ui/cli_display.py`, `storage/file_storage.py`) are placed in their correct directory structure as shown below:

   ```
   .
   ├── cli.py
   ├── main.py
   ├── src/
   │   ├── library_core.py
   │   └── search_module.py (Assumed dependency)
   ├── storage/
   │   └── file_storage.py
   └── ui/
       └── cli_display.py
   ```

   *Note: The `src/search_module.py` file was not provided, but it is imported by `library_core.py`. You'll need to ensure it exists or mock it (e.g., with an empty file containing a simple `SearchEngine` class with `find_by_title` static method) for the application to run without errors.*
2. **Execute the main file:** Open your terminal or command prompt in the project's root directory and run:

   ```bash
   python main.py
   ```
3. **Start Managing:** The application's main menu will appear, and you can start interacting with your library!

---

## 📂 Project Structure Overview

The application is designed with a basic Model-View-Controller (MVC)-like separation of concerns:

* **`main.py`**: The entry point of the application.
* **`cli.py`**: Handles the **Controller** logic, managing user input and orchestrating calls to the `Library` core based on menu choices.
* **`src/library_core.py`**: The **Model** or core business logic. Contains the `Library` class, which manages the book list and implements all CRUD (Create, Read, Update, Delete) operations.
* **`ui/cli_display.py`**: The **View** logic. Contains the `Display` class for formatting and printing all output (menus, lists, results, messages) to the user.
* **`storage/file_storage.py`**: Handles data **Persistence**. The `FileStorage` class manages saving and loading the book data to/from the `json/library_data.json` file.

---

## ✨ Features

The Library Manager offers the following core functionalities:

1. **Add Book**: Input title, author, and year. Prevents adding duplicates.
2. **List Books**: Display all books currently in the library with formatted output.
3. **Search Book**: Find books by title (case-insensitive search).
4. **Remove Book** (Partial Implementation): Remove a book by title. The current logic handles exact matches but flags an issue if multiple results are found, indicating a need for interactive choice.
5. **Update Book** (Partial Implementation): Update the title, author, or year of an existing book by its current title.
6. **Summary**: Display a summary of the library, including the **Total number of books** and the count of **Unique Authors**.
7. **Exit Program**: Save data and gracefully close the application.

### Data Persistence

All data is automatically loaded on startup and saved after every modification (add, remove, update) to the file specified in `file_storage.py` (default: `json/library_data.json`).

---

## 🛠️ Key Classes and Methods

| File                | Class           | Key Methods                                                                                       | Description                                                       |
| :------------------ | :-------------- | :------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------- |
| `library_core.py` | `Library`     | `add_book`, `list_books`, `search_book`, `remove_book`, `update_book`, `show_summary` | Manages the collection of book data.                              |
| `file_storage.py` | `FileStorage` | `save_data`, `load_data`                                                                      | Handles reading and writing book data to a JSON file.             |
| `cli_display.py`  | `Display`     | `menu`, `list_books`, `search_results`, `summary`, `success`, `warning`, `info`     | Static methods for all command-line output.                       |
| `cli.py`          | `LibraryApp`  | `main_menu`, `get_valid_year`                                                                 | Runs the main application loop and handles user input validation. |

---

## 🧪 Usage Examples

Below are some sample interactions showing how the program behaves in the terminal:

```
📖 Personal Library Manager
1️⃣ Add Book
2️⃣ List Books
3️⃣ Search Book
4️⃣ Remove Book
5️⃣ Update Book
6️⃣ Summary
7️⃣ Exit Program
```

**Example: Adding a Book**

```
Enter the book title: Clean Code
Enter the author’s name: Robert C. Martin
Enter publication year: 2008
✅ Added 'Clean Code' by Robert C. Martin (2008).
```

**Example: Searching**

```
Enter title to search: python
📗 Python Crash Course - Eric Matthes (2019)
```

---

## ✅ Error Handling

The application includes basic error handling:

* Invalid menu choices are rejected with a warning.
* Publication year must be between **1000–2025**.
* Duplicate books (same title + author) are not allowed.
* Missing or corrupted JSON data is handled gracefully.
* If multiple search matches exist during removal/update, the program alerts the user instead of removing the wrong book.

---

## 📦 Data Storage Details

Data is stored in:

```
json/library_data.json
```

The file is created automatically if it does not exist. Formatting uses:

* UTF-8 encoding
* `indent=4` for readability
* `ensure_ascii=False` to allow non-English characters (e.g., Persian titles or author names)

Example JSON structure:

```json
[
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008
    }
]
```

---

## 🧱 Limitations (Current)

It's important to document known limitations so contributors or users know what to expect:

* **Removal and update are not interactive** when multiple books match the same title.
* **No sorting** (by year, title, author).
* **No validation** for author or title formatting.
* **No unit tests** included yet.
* **Search limited to title only** — no author/year search.

---

## 🤝 Contributing

Contributions are welcome. Suggested areas include:

* Adding full interactive selection for duplicates.
* Improving search functionality (author, year, partial matches).
* Adding sorting options.
* Writing unit tests (pytest recommended).
* Adding CI/CD pipeline for testing.
* Improving error handling and user experience.

To contribute:

```
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request
```

---

📝 Related Article

I wrote a detailed article about this project on [Dev.to](https://dev.to/shahrouzlogs/building-a-simple-personal-library-with-python-my-experience-from-zero-to-execution-fge).
It explains the development process, structure, and lessons learned while building this CLI app.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋 About This Project

This project is built for learning purposes, focusing on:

* Python scripting
* Modular architecture
* CLI-based applications
* JSON storage
* Clean separation of concerns

---
