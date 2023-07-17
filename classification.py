import pytesseract
from pdf2image import convert_from_path
import cv2
import os
import regex as re
from natsort import natsorted

all_files=(list(filter(lambda x: re.search('.jpg',x), os.listdir('./ocr_output'))))
        #print(all_files)
aa=sorted(all_files, key=lambda x: (int(re.sub('\D', '', x)), x))
print(aa)
for key,file in enumerate(aa):
    print('process start','./ocr_output/'+file)
    image=cv2.imread('./ocr_output/'+file)
    pytesseract.pytesseract.tesseract_cmd=r'/opt/homebrew/bin/tesseract'
    text=pytesseract.image_to_string(image,config='--psm 3')

    diagnosis_match = re.search(r"DIAGNOSIS\s*(.*?)\s*(?:\n\n|$)", text, re.DOTALL)
    if diagnosis_match:
        diagnosis_text = diagnosis_match.group(1)
        # Find the line starting with "1." after DIAGNOSIS
        line_match = re.search(r"1\..*", diagnosis_text)
        if line_match:
            target_line = line_match.group(0).strip()
            print("Line starting with '1.' after DIAGNOSIS:", target_line)
            file1=open("./ocr_output/result_output_diagnosis.txt","a")
            file1.write('--------------------new page started ------'+str(key))
            file1.write(target_line)

# Extract page number
    page_match = re.search(r"Page\s+(\d+)\s+of", text)
    if page_match:
        page_number = page_match.group(1)
        print("Page Number:", page_number)
    #print(text)