# StudySphere 📚

A simple command-line task management application built with Python.

StudySphere helps users organize their study tasks by allowing them to add, view, complete, and delete tasks through an interactive menu-driven interface.

---

## Features

- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Menu-driven interface
- Simple and beginner-friendly design

---

## Technologies Used

- Python 3

---

## Project Structure

```
StudySphere/
│
├── main.py
├── tasks.py
├── utils.py
└── README.md
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

```
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

```
Choose your choice (1-5): 1

Enter Task Title: Learn Python

Task added successfully
```

### View tasks

```
Choose your choice (1-5): 2

Task 1

Title: Learn Python

Completed: No
```

### Complete a task

```
Choose your choice (1-5): 3

Enter task number: 1

Task 'Learn Python' is marked as completed
```

### Delete a task

```
Choose your choice (1-5): 4

Enter task number: 1
```

---

## Limitations

- Tasks are stored only in memory.
- Tasks are deleted when the application closes.
- Data is not saved permanently.

---

## Development Roadmap

| Version | Description | Status |
| --- | --- | --- |
| v1.0 | CLI Task Manager (List + Dictionary) | ✅ Completed |
| v1.1 | Object-Oriented Programming (OOP) | ⏳ In Progress |
| v2.0 | JSON Storage | ⏳ Planned |
| v2.1 | SQLite Database | ⏳ Planned |
| v3.0 | Flask Web Application | ⏳ Planned |
| v3.1 | Authentication | ⏳ Planned |
| v3.2 | REST API | ⏳ Planned |
| v4.0 | AI-Powered Student Learning Platform | ⏳ Planned |

---

## Future Improvements

- Convert the project to OOP
- Store tasks in JSON files
- Use an SQLite database
- Build a Flask web application
- Add search functionality
- Add task priorities
- Add due dates

---

## Author

CHAMARTHI MANIKANTA

B.Tech (CSM)

Raghu Engineering College