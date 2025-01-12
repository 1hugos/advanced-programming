import os
import cv2
import tensorflow as tf
from datetime import datetime
import utils

DEFAULT_OUTPUT_DIR = "../data/annotated_images"
MODEL_PATH = "C:/Users/spart/ssd_mobilenet_v2/saved_model"
model = tf.saved_model.load(MODEL_PATH)
detect_fn = model.signatures["serving_default"]


def detect_people_from_path(image_path):
    image = utils.load_image_from_path(image_path)

    return detect_people(image)


def detect_people_from_url(image_url):
    image = utils.load_image_from_url(image_url)

    return detect_people(image)


def detect_people(image_np, output_dir=DEFAULT_OUTPUT_DIR):
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"{timestamp}.png")

    input_tensor = tf.convert_to_tensor(image_np)[tf.newaxis, ...]

    detections = detect_fn(input_tensor)
    num_detections = int(detections["num_detections"])

    boxes = detections["detection_boxes"][0][:num_detections].numpy()
    classes = detections["detection_classes"][0][:num_detections].numpy().astype(int)
    scores = detections["detection_scores"][0][:num_detections].numpy()

    person_count = 0
    height, width, _ = image_np.shape

    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    for i in range(num_detections):
        if classes[i] == 1:
            print(f"Class: {classes[i]}, score: {scores[i]}")

        # Sprawdza czy dla klasy person pewność, że jest to osoba jest większa od 0.5
        if classes[i] == 1 and scores[i] > 0.5:
            person_count += 1

            y_min, x_min, y_max, x_max = boxes[i]
            x_min = int(x_min * width)
            x_max = int(x_max * width)
            y_min = int(y_min * height)
            y_max = int(y_max * height)

            cv2.rectangle(image_bgr, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    # Zapis obrazu z zaznaczonymi osobami
    cv2.imwrite(output_path, image_bgr)

    return {"count": person_count}
