import pytesseract
from pdf2image import convert_from_path
import cv2
import os
import regex as re
from natsort import natsorted

image=cv2.imread('./ocr_output/page31.jpg')
pytesseract.pytesseract.tesseract_cmd=r'/opt/homebrew/bin/tesseract'
text=pytesseract.image_to_string(image,config='--psm 6')

print(text)
