import cv2
import os
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

input_dir = "data/raw_img"
output_dir = "data/processed_img"
text_output_dir = "data/ocr_results"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(text_output_dir):
    os.makedirs(text_output_dir)

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)


for file_name in os.listdir(input_dir):
    file_path = os.path.join(input_dir, file_name)
    if os.path.isfile(file_path):
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

        if img is not None:
            base_name = os.path.basename(file_path)
            name, ext = os.path.splitext(base_name)

            # Median Blur
            converted_img = cv2.medianBlur(img, 3)
            output_path = os.path.join(output_dir, f"{name}_medianBlur{ext}")
            cv2.imwrite(output_path, converted_img)
            text = extract_text_from_image(converted_img)
            with open(os.path.join(text_output_dir, f"{name}_medianBlur.txt"), "w") as text_file:
                text_file.write(text)

            # Gaussian Blur with Otsu Thresholding
            converted_img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            output_path = os.path.join(output_dir, f"{name}_gaussian_otsu{ext}")
            cv2.imwrite(output_path, converted_img)
            text = extract_text_from_image(converted_img)
            with open(os.path.join(text_output_dir, f"{name}_gaussian_otsu.txt"), "w") as text_file:
                text_file.write(text)

            # Bilateral Filter with Otsu Thresholding
            converted_img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            output_path = os.path.join(output_dir, f"{name}_bilateral_otsu{ext}")
            cv2.imwrite(output_path, converted_img)
            text = extract_text_from_image(converted_img)
            with open(os.path.join(text_output_dir, f"{name}_bilateral_otsu.txt"), "w") as text_file:
                text_file.write(text)

            # Median Blur with Otsu Thresholding
            converted_img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            output_path = os.path.join(output_dir, f"{name}_median_otsu{ext}")
            cv2.imwrite(output_path, converted_img)
            text = extract_text_from_image(converted_img)
            with open(os.path.join(text_output_dir, f"{name}_median_otsu.txt"), "w") as text_file:
                text_file.write(text)

            # Adaptive Thresholding with Gaussian Blur
            converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            output_path = os.path.join(output_dir, f"{name}_adaptive_gaussian{ext}")
            cv2.imwrite(output_path, converted_img)
            text = extract_text_from_image(converted_img)
            with open(os.path.join(text_output_dir, f"{name}_adaptive_gaussian.txt"), "w") as text_file:
                text_file.write(text)

            # Adaptive Thresholding with Bilateral Filter
            converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            output_path = os.path.join(output_dir, f"{name}_adaptive_bilateral{ext}")
            cv2.imwrite(output_path, converted_img)
            text = extract_text_from_image(converted_img)
            with open(os.path.join(text_output_dir, f"{name}_adaptive_bilateral.txt"), "w") as text_file:
                text_file.write(text)

            # Adaptive Thresholding with Median Blur
            converted_img = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            output_path = os.path.join(output_dir, f"{name}_adaptive_median{ext}")
            cv2.imwrite(output_path, converted_img)
            text = extract_text_from_image(converted_img)
            with open(os.path.join(text_output_dir, f"{name}_adaptive_median.txt"), "w") as text_file:
                text_file.write(text)
