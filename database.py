import sqlite3

def get_connection():
    return sqlite3.connect("tasks.db")

def create_database():
    try:
        with get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            """)

            cursor.execute("""
                CREATE UNIQUE INDEX IF NOT EXISTS idx_tasks_title_unique
                ON tasks (LOWER(TRIM(title)))
            """)
        
    except sqlite3.Error as error:
        print(f"Database error: {error}")

def add_task(title, status):
    try:
        with get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO tasks (title, status) VALUES (?, ?)",
                (title, status)
            )

            task_id = cursor.lastrowid

            return task_id

    except sqlite3.IntegrityError:
        print("Task already exists")
        return None
    
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return None

def get_tasks():
    try:
        with get_connection() as connection:
        
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM tasks")

            tasks = cursor.fetchall()

            return tasks
    
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []

def complete_task(task_id):
    try:
        with get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute(
                "UPDATE tasks SET status = ? WHERE id = ?",
                ("Complete", task_id)
            )

            rows_affected = cursor.rowcount

            return rows_affected
    
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return 0

def delete_task(task_id):
    try:
        with get_connection() as connection:

            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM tasks WHERE id = ?",
                (task_id,)
            )

            rows_affected = cursor.rowcount
        
            return rows_affected
    
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return 0
