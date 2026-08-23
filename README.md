# StudySphere 📚

A simple command-line task management application built with Python.

StudySphere helps students organize their study tasks through an interactive
menu-driven interface. The project is being developed incrementally as a
learning project throughout my Python Full Stack journey.

---

## Features

### v1.0

- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Menu-driven interface

### v1.1

- Object-Oriented Programming (OOP)
- `Task` class for task objects
- `TaskManager` class for task management
- Task status management
- Input validation
- Exception handling using `try-except`
- Safe task completion and deletion
- `__str__()` magic method

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Exception Handling
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
├── README.md
└── .gitignore
```

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
============ StudySphere ============

1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit

=====================================
```

---

## Example

### Add a task

```text
Choose your choice (1-5): 1

Enter Task Title: Learn Python

Task added successfully
```

### View tasks

```text
Choose your choice (1-5): 2

=========== YOUR TASKS ===========

1. Learn Python -> Pending
```

### Complete a task

```text
Choose your choice (1-5): 3

Enter task number to mark as complete: 1

Task marked as complete
```

### Delete a task

```text
Choose your choice (1-5): 4

Enter task number to delete: 1

Task is deleted successfully
```

---

## **Limitations**

- Tasks are currently stored only in memory.
- Tasks are deleted when the application closes.
- Data is not saved permanently.
- The application currently runs only through the command-line interface.
- No database is used.
- No web interface is available.
- No user authentication or authorization is implemented.

---

## **Future Improvements**

- Store tasks permanently using JSON files.
- Add SQLite database support.
- Build a Flask web application.
- Develop RESTful APIs.
- Add user authentication and authorization.
- Add task search and filtering.
- Add task priorities.
- Add due dates and deadlines.
- Add task categories.
- Add AI-powered study assistance.
- Add student productivity analytics.

---

## **About the Project**

StudySphere is a learning-focused project designed to grow alongside my
Python Full Stack journey.

The project started as a simple command-line task manager that allows users
to add, view, complete, and delete study tasks.

In **v1.1**, the project was upgraded using Object-Oriented Programming
(OOP) and exception handling. The application now uses classes to represent
and manage tasks, while input validation and exception handling make the
application more reliable.

StudySphere follows an incremental development approach. Each version
introduces new programming concepts and technologies while building on the
previous version.

The long-term goal is to transform StudySphere from a simple CLI task
manager into a complete student learning platform with database support,
web development, APIs, authentication, and AI-powered features.

The project also provides practical experience with software development
concepts such as:

- Object-oriented design
- Exception handling
- Input validation
- File handling
- Database design
- API development
- Version control
- Git and GitHub
- Full-stack development
- AI integration

---

## **Objectives**

- Learn and strengthen Python programming fundamentals.
- Practice Object-Oriented Programming.
- Understand exception handling and input validation.
- Learn file handling and JSON data storage.
- Learn database design using SQLite.
- Build RESTful APIs.
- Develop full-stack applications using Flask.
- Implement authentication and authorization.
- Integrate AI-based features.
- Follow Git and GitHub best practices.
- Develop software incrementally using version control.

---

## **Development Roadmap**

| Version | Description | Status |
| --- | --- | --- |
| v1.0 | CLI Task Manager (List + Dictionary) | ✅ Completed |
| v1.1 | OOP + Exception Handling | ✅ Completed |
| v2.0 | JSON Storage | ⏳ Planned |
| v2.1 | SQLite Database | ⏳ Planned |
| v3.0 | Flask Web Application | ⏳ Planned |
| v3.1 | Authentication & Authorization | ⏳ Planned |
| v3.2 | REST API | ⏳ Planned |
| v4.0 | AI-Powered Student Learning Platform | ⏳ Planned |

---

## **Current Version**

### v1.1 — OOP + Exception Handling

#### What's included in v1.1?

- `Task` class
- `TaskManager` class
- Task objects
- `__str__()` magic method
- Add task functionality
- View task functionality
- Complete task functionality
- Delete task functionality
- Empty task validation
- Task number validation
- `ValueError` exception handling
- Safe handling of invalid user input

---

## **Author**

CHAMARTHI MANIKANTA

B.Tech (CSM)

Raghu Engineering College
