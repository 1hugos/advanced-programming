import sqlite3
import time

DB_PATH = "tasks.db"


def read_all_tasks(db_path):
    result = []

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, status FROM tasks")
        tasks = cursor.fetchall()

    for task in tasks:
        result.append([task[0], task[1]])

    return result


def update_status(db_path, task_id, status):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        conn.commit()


def process_task(task):
    print(f"Processing task {task[0]}...")
    time.sleep(30)
    print(f"Task {task[0]} done.")


def consume_task(db_path):
    while True:
        all_tasks = read_all_tasks(db_path)
        pending_tasks = []
        tasks_on_hold = []

        for task in all_tasks:
            if task[1] == "pending":
                pending_tasks.append(task)
            elif task[1] == "in_progress":
                tasks_on_hold.append(task)

        if len(pending_tasks) > 0:
            for task in pending_tasks:
                update_status(db_path, task[0], 'in_progress')
                process_task(task)
                update_status(db_path, task[0], 'done')
        elif len(tasks_on_hold) > 0:
            for task in pending_tasks:
                process_task(task)
                update_status(db_path, task[0], 'done')
        else:
            print("No tasks to process.")

        time.sleep(5)


if __name__ == "__main__":
    consume_task(DB_PATH)
