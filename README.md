# StudySphere 📚

A simple command-line task management application built with Python.

StudySphere helps students organize their study tasks through an interactive
menu-driven interface. The project is being developed incrementally as a
learning project throughout my Python Full Stack journey.

---

## Features

### v1.0 — Basic CLI Task Manager

- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Menu-driven interface
- List and dictionary-based task management

### v1.1 — OOP + Exception Handling

- Object-Oriented Programming (OOP)
- `Task` class for task objects
- `TaskManager` class for task management
- Task status management
- Input validation
- Exception handling using `try-except`
- Safe task completion and deletion
- `__str__()` magic method

### v2.0 — JSON Storage

- Permanent task storage using JSON
- Load tasks automatically when the application starts
- Save tasks automatically after adding a task
- Save tasks automatically after completing a task
- Save tasks automatically after deleting a task
- `load_tasks()` utility function
- `save_tasks()` utility function
- Automatic creation of `tasks.json` if it does not exist
- Handling of invalid or corrupted JSON data
- File handling using Python's `json` module

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Exception Handling
- File Handling
- JSON
- Git & GitHub

---

## Project Structure

```text
StudySphere/
│
├── main.py
├── task.py
├── task_manager.py
├── utils.py
├── tasks.json
├── README.md
└── .gitignore
```

## File Description

| File | Purpose |
| --- | --- |
| `main.py` | Runs the main application and handles the menu |
| `task.py` | Contains the `Task` class |
| `task_manager.py` | Handles task operations |
| `utils.py` | Contains menu and JSON file handling functions |
| `tasks.json` | Stores tasks permanently |
| `README.md` | Project documentation |
| `.gitignore` | Specifies files ignored by Git |

---

## How to Run

### Clone the repository

```bash
git clone <repository-url>
```

### Move into the project directory

```bash
cd StudySphere
```

### Run the application

```bash
py main.py
```

---

## Application Menu

```text
=========== StudySphere ===========

1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit

===================================
```

---

## Example

### Add a task

```text
Enter your choice (1-5): 1

Enter title for task: Learn Python

Task added successfully
```

### View tasks

```text
Enter your choice (1-5): 2

=========== YOUR TASKS ===========

1. Learn Python -> Pending

===================================
```

### Complete a task

```text
Enter your choice (1-5): 3

Enter task number to mark as complete: 1

Task marked as complete
```

### Delete a task

```text
Enter your choice (1-5): 4

Enter task number to delete: 1

Task is deleted successfully
```

---

## Data Storage

Starting from **v2.0**, StudySphere stores tasks permanently using a JSON file.

The `tasks.json` file contains task information such as:

```json
[
    {
        "title": "Learn Python",
        "status": "Pending"
    }
]
```

The application uses:

- `load_tasks()` to load tasks from `tasks.json`
- `save_tasks()` to save tasks to `tasks.json`

If `tasks.json` does not exist, the application automatically creates it.

If the JSON file contains invalid data, the application safely initializes
an empty task list.

---

## Exception Handling

StudySphere uses exception handling to make the application more reliable.

Currently handled exceptions include:

- `FileNotFoundError`
- `json.JSONDecodeError`
- `ValueError`
- `PermissionError`
- `TypeError`
- `OSError`
- `KeyboardInterrupt`
- `EOFError`

### `FileNotFoundError`

Handles situations where `tasks.json` does not exist.

The application automatically creates a new JSON file.

### `json.JSONDecodeError`

Handles situations where `tasks.json` contains invalid or corrupted JSON data.

The application resets the task list and recreates valid JSON data.

### `ValueError`

Handles invalid task numbers entered by the user.

For example:

```text
Enter task number: abc

Enter a valid task number
```

### `PermissionError`

Handles situations where the application does not have permission to save
the task data.

### `TypeError`

Handles data that cannot be converted into valid JSON.

### `OSError`

Handles other file-system related errors.

### `KeyboardInterrupt`

Handles user interruption using `Ctrl + C`.

### `EOFError`

Handles situations where input is unexpectedly terminated.

---

## OOP Design

StudySphere uses Object-Oriented Programming to organize the application.

### `Task` Class

The `Task` class represents an individual task.

It contains:

- Task title
- Task status
- `__str__()` method
- `to_dict()` method

Example:

```python
task = Task("Learn Python")
```

### `TaskManager` Class

The `TaskManager` class manages the collection of tasks.

It provides functionality to:

- Add tasks
- View tasks
- Complete tasks
- Delete tasks

Example:

```python
manager = TaskManager()
```

---

## JSON File Handling

StudySphere uses Python's built-in `json` module for persistent storage.

### Loading data

```python
json.load(file)
```

The `load_tasks()` function reads task data from `tasks.json`.

### Saving data

```python
json.dump(tasks, file, indent=4)
```

The `save_tasks()` function writes task data to `tasks.json`.

The project uses JSON because it is simple, human-readable, and suitable for
learning file-based data persistence.

---

## Limitations

- The application currently runs only through the command-line interface.
- No database is used yet.
- No web interface is available.
- No user authentication or authorization is implemented.
- JSON storage is suitable for this learning project but is not ideal for
  large-scale applications.
- No task search or filtering is currently available.
- No task priorities are currently available.
- No due dates or deadlines are currently available.
- Tasks are not associated with individual users.

---

## Future Improvements

- Add SQLite database support
- Build a Flask web application
- Develop RESTful APIs
- Add user authentication and authorization
- Add task search and filtering
- Add task priorities
- Add due dates and deadlines
- Add task categories
- Add AI-powered study assistance
- Add student productivity analytics
- Add user profiles
- Build a complete student learning platform

---

## About the Project

StudySphere is a learning-focused project designed to grow alongside my
Python Full Stack journey.

The project started as a simple command-line task manager that allowed users
to add, view, complete, and delete study tasks.

In **v1.1**, the project was upgraded using Object-Oriented Programming and
exception handling. The application introduced classes to represent and
manage tasks while input validation and exception handling improved
reliability.

In **v2.0**, the application was upgraded with **JSON-based persistent
storage**. Tasks are now saved to `tasks.json` and automatically loaded when
the application starts.

StudySphere follows an incremental development approach. Each version
introduces new programming concepts and technologies while building on the
previous version.

The long-term goal is to transform StudySphere from a simple CLI task manager
into a complete student learning platform with database support, web
development, APIs, authentication, and AI-powered features.

---

## Learning Objectives

Through the development of StudySphere, the project focuses on learning and
practicing the following concepts:

- Python programming fundamentals
- Object-Oriented Programming
- Classes and objects
- Magic methods
- Exception handling
- Input validation
- File handling
- JSON data storage
- Persistent data management
- Modular programming
- Separation of responsibilities
- Database design
- RESTful API development
- Web application development
- Authentication and authorization
- AI integration
- Git and GitHub
- Incremental software development

---

## Development Roadmap

| Version | Description | Status |
| --- | --- | --- |
| v1.0 | CLI Task Manager (List + Dictionary) | ✅ Completed |
| v1.1 | OOP + Exception Handling | ✅ Completed |
| v2.0 | JSON Storage | ✅ Completed |
| v2.1 | SQLite Database | ⏳ Planned |
| v3.0 | Flask Web Application | ⏳ Planned |
| v3.1 | Authentication & Authorization | ⏳ Planned |
| v3.2 | REST API | ⏳ Planned |
| v4.0 | AI-Powered Student Learning Platform | ⏳ Planned |

---

## Current Version

### v2.0 - JSON Storage

#### What's included in v2.0?

- `Task` class
- `TaskManager` class
- Task objects
- `__str__()` magic method
- `to_dict()` method
- Add task functionality
- View task functionality
- Complete task functionality
- Delete task functionality
- Empty task validation
- Task number validation
- `ValueError` exception handling
- `FileNotFoundError` handling
- `json.JSONDecodeError` handling
- `PermissionError` handling
- `TypeError` handling
- `OSError` handling
- `KeyboardInterrupt` handling
- `EOFError` handling
- JSON file storage
- Persistent task data
- `load_tasks()` function
- `save_tasks()` function
- Automatic creation of `tasks.json`
- Automatic recovery from invalid JSON data

---

## Version History

### v1.0

The initial version of StudySphere was developed as a basic command-line
task manager using Python lists and dictionaries.

Users could:

- Add tasks
- View tasks
- Complete tasks
- Delete tasks

### v1.1

The project was upgraded using Object-Oriented Programming.

The following concepts were introduced:

- Classes
- Objects
- `Task`
- `TaskManager`
- `__str__()`
- Exception handling
- Input validation

### v2.0

The project was upgraded to use **JSON-based persistent storage**.

Tasks are now stored in:

```text
tasks.json
```

The application automatically loads existing tasks when it starts and saves
changes when tasks are added, completed, or deleted.

---

## Git & Version Control

StudySphere is developed incrementally using Git and GitHub.

Each major version represents a stage in the learning process.

Example version progression:

```text
v1.0
  ↓
Basic CLI Task Manager
  ↓
v1.1
  ↓
OOP + Exception Handling
  ↓
v2.0
  ↓
JSON Persistent Storage
  ↓
v2.1
  ↓
SQLite Database
  ↓
v3.0
  ↓
Flask Web Application
```

This approach allows the project to evolve while maintaining a clear history
of the development process.

---

## Author

CHAMARTHI MANIKANTA

B.Tech (CSM)  
Raghu Engineering College
