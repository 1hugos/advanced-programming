import uuid

FILE_PATH = "tasks.txt"


def add_task(file_path: str):
    task_id = uuid.uuid4()
    status = "pending"

    with open(file_path, mode='a') as file:
        file.write(f"{task_id}|{status}\n")

    print(f"Added task: ID: {task_id}, Status: {status}")


if __name__ == "__main__":
    add_task(FILE_PATH)
