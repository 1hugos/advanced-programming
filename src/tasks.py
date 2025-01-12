import pika
import json
from uuid import uuid4

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "people_detection_tasks"


def send_task(task_data):
    connection_parameters = pika.ConnectionParameters(host=RABBITMQ_HOST)
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    task_id = str(uuid4())
    task_data["task_id"] = task_id

    channel.basic_publish(
        exchange="", routing_key=QUEUE_NAME, body=json.dumps(task_data)
    )

    connection.close()
    return task_id
