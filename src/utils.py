from PIL import Image
import requests
import numpy as np
from io import BytesIO

def load_image_from_path(image_path):
    image = Image.open(image_path)

    if image.mode != "RGB":
        image = image.convert("RGB")
        
    return np.array(image)


def load_image_from_url(image_url):
    response = requests.get(image_url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch image. Status code: {response.status_code}")
    
    image = Image.open(BytesIO(response.content))
    if image.mode != "RGB":
        image = image.convert("RGB")

    return np.array(image)
