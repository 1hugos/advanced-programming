import sqlite3

DATABASE_PATH = 'tasks.db'

def init():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            result TEXT,
            error TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_task_status(task_id, status, result=None, error=None):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO tasks (task_id, status, result, error)
        VALUES (?, ?, ?, ?)
    ''', (task_id, status, result, error))
    conn.commit()
    conn.close()


def get_task_status(task_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT status, result, error FROM tasks WHERE task_id = ?
    ''', (task_id,))
    task = cursor.fetchone()
    conn.close()

    if task:
        return {
            "status": task[0],
            "result": task[1],
            "error": task[2]
        }
    else:
        return {"status": "not found"}
