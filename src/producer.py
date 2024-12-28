import sqlite3
import uuid

DB_PATH = "tasks.db"


def initialize_db(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                status TEXT NOT NULL
            )
        """)
        conn.commit()


def add_task(db_path):
    task_id = str(uuid.uuid4())
    status = "pending"

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (id, status) VALUES (?, ?)", (task_id, status))
        conn.commit()

    print(f"Added task: ID: {task_id}, Status: {status}")


if __name__ == "__main__":
    initialize_db(DB_PATH)
    add_task(DB_PATH)
