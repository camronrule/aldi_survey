from PIL import Image
from pytesseract import*
from heic2png import HEIC2PNG
import os
import cv2
import re

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


print("Please enter the name of the .heic image, without the extension:")
img_name = input()
heic_img = HEIC2PNG(img_name+".heic")
heic_img.save()
os.remove(img_name+".heic")

#preprocess image to make recognition stronger
#apply grayscale, gaussian blur, otsu's threshold
image = cv2.imread(img_name+".png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#remove noise, invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

print("Pulling text from image, this may take a second.")

img_text = pytesseract.image_to_string(invert, lang='eng')
for i in img_text.splitlines():
    if "/" in i and ("www" not in i):
        text = (re.sub("[^0-9^/^:^ ^P^M]", "", i)).strip()
        print(text)
        break

os.remove(img_name+".png")