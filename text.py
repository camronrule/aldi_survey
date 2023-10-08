from PIL import Image
from pytesseract import*
from heic2png import HEIC2PNG
import os
import cv2
import re

def main():
        
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("\nPut the image of the receipt into this directory ("+dir_path+")")
    print("Please enter the name of the .heic image, without the extension:")
    img_name = input()
    heic_img = HEIC2PNG(img_name+".heic")
    heic_img.save()
    #os.remove(img_name+".heic")

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

    print("\nPulling text from image, this may take a second.\n")

    img_text = pytesseract.image_to_string(invert, lang='eng')
    for i in img_text.splitlines():
        if "/" in i and ("www" not in i):

            #process survey code

            i = i.replace(" ", "/") #replace whitespace with '/' to make split easier later
            text = (re.sub("[^0-9^/]", "", i)).strip() #remove anything that is not a digit or /
            while (not text[0].isnumeric()): #trim the front of the string until it starts with a number
                text = text[1:]
            print(text[0:20])
            #first 20 char are survey code, separated with '/'
            break

    os.remove(img_name+".png")
    
    return text[0:20] #send survey code back to script.py

if __name__ == '__main__':
    main()