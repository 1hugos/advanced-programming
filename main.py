import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print('1:', pytesseract.image_to_string(Image.open(r'data\cant_afford_the_cat.png')))
print('2:', pytesseract.image_to_string(Image.open(r'data\im_tired_boss.png')))
print('3:', pytesseract.image_to_string(Image.open(r'data\speaks_korean.png')))
print('4:', pytesseract.image_to_string(Image.open(r'data\thats_what_she_said.png')))
print('5:', pytesseract.image_to_string(Image.open(r'data\you_shall_not_pass.png')))

print('###')

print(pytesseract.image_to_string(r'data\cant_afford_the_cat.png'))

print(pytesseract.image_to_string(Image.open(r'data\im_tired_boss.png'), lang='eng'))