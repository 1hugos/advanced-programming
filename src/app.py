import os
import db_manager
from flask import Flask, request, jsonify
from tasks import send_task

app = Flask(__name__)

UPLOAD_FOLDER = "../data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/people-count-local", methods=["GET"])
def people_count_local():
    image_path = request.args.get("path")
    if not image_path:
        return jsonify({"error": "Image path is required"}), 400

    task_id = send_task({"type": "local", "image_path": image_path})

    return jsonify({"task_id": task_id}), 200


@app.route("/people-count-url", methods=["GET"])
def people_count_url():
    image_url = request.args.get("url")
    if not image_url:
        return jsonify({"error": "Image URL is required"}), 400

    #mock dla dodania 1000 zdjęc do kolejki
    task_ids = []
    for i in range(1000):
        task_id = send_task({"type": "url", "image_url": image_url})
        task_ids.append(task_id)

    return jsonify({"task_ids": task_ids}), 200
    # return jsonify({"task_id": task_id}), 200


@app.route("/people-count-file", methods=["POST"])
def people_count_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    files = request.files.getlist("file")

    task_ids = []

    for file in files:
        if file.filename == "":
            continue

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        task_id = send_task({"type": "file", "image_path": file_path})
        task_ids.append(task_id)

    return jsonify({"task_ids": task_ids}), 200


@app.route("/task-status", methods=["GET"])
def task_status():
    task_id = request.args.get("task_id")
    if not task_id:
        return jsonify({"error": "Task ID is required"}), 400

    result = db_manager.get_task_status(task_id)

    return jsonify(result), 200


@app.route("/")
def home():
    return "Home page"


if __name__ == "__main__":
    app.run(debug=True)
