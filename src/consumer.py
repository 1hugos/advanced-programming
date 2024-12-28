import time

FILE_PATH = "tasks.txt"


def read_all_tasks(file_path):
    tasks = []

    with open(file_path, mode='r') as file:
        lines = file.readlines()

    for line in lines:
        tasks.append(line.strip().split('|'))

    return tasks


def write_tasks(file_path, tasks):
    with open(file_path, mode='w') as file:
        for task in tasks:
            file.write("|".join(task) + "\n")


def update_status(file_path, tasks, task_to_update, status):
    updated_tasks = []

    for task in tasks:
        if task[0] == task_to_update[0]:
            task[1] = status

        updated_tasks.append(task)

    with open(file_path, mode='w') as file:
        for task in updated_tasks:
            file.write("|".join(task) + "\n")


def process_task(task):
    task[1] = "in_progress"
    print(f"Processing task {task[0]}...")
    time.sleep(30)
    print(f"Task {task[0]} done.")


def consume_task(file_path):
    while True:
        is_task_processed = False
        updated_tasks = []
        tasks = read_all_tasks(file_path=file_path)

        for task in tasks:
            if task[1] == "pending" and not is_task_processed:
                is_task_processed = True

                update_status(
                    file_path=file_path,
                    tasks=tasks,
                    task_to_update=task,
                    status="in_progress")
                process_task(task=task)

                task[1] = "done"
            elif task[1] == "in_progress":
                process_task(task=task)
                task[1] = "done"

            updated_tasks.append(task)

        write_tasks(file_path=file_path, tasks=updated_tasks)
        time.sleep(5)


if __name__ == "__main__":
    consume_task(FILE_PATH)
