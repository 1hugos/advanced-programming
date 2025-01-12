import db_manager
import pika
import json
from detection import detect_people_from_path, detect_people_from_url

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "people_detection_tasks"


def process_task(ch, method, properties, body):
    task = json.loads(body)
    task_id = task["task_id"]
    task_type = task["type"]

    try:
        print("Processing task:", task_id)
        db_manager.save_task_status(task_id, "in progress")

        if task_type == "local":
            result = detect_people_from_path(task["image_path"])
        elif task_type == "url":
            result = detect_people_from_url(task["image_url"])
        elif task_type == "file":
            result = detect_people_from_path(task["image_path"])
        else:
            print("Processing error:", task_id)
            raise ValueError("Invalid task type")

        print("Completed task:", task_id)
        db_manager.save_task_status(task_id, "completed", result=str(result))
    except Exception as e:
        db_manager.save_task_status(task_id, "failed", error=str(e))
    finally:
        ch.basic_ack(delivery_tag=method.delivery_tag)


def start_worker():
    connection_parameters = pika.ConnectionParameters(host=RABBITMQ_HOST)
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=process_task)
    print("Worker is running...")
    channel.start_consuming()


if __name__ == "__main__":
    db_manager.init()
    start_worker()
