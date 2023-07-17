
import pytesseract
from pdf2image import convert_from_path
import cv2
import os
import regex as re
from natsort import natsorted

class ocr_extraction_1():
    def __init__(self):
        pass

    def pdf2img(self,pdf):
        #pop_path = "/usr/local/Cellar/poppler/21.03.0_1/bin"

        pdf_path=pdf
        images = convert_from_path(pdf_path)
        for i in range(len(images)):
            images[i].save('./ocr_output/page'+str(i)+'.jpg','JPEG')

    def ocr_extraction_f(self):
        print('done')
        all_files=(list(filter(lambda x: re.search('.jpg',x), os.listdir('./ocr_output'))))
        #print(all_files)
        aa=sorted(all_files, key=lambda x: (int(re.sub('\D', '', x)), x))
        print(aa)
        for file in aa:
            print('process start','./ocr_output/'+file)
            image=cv2.imread('./ocr_output/'+file)
            pytesseract.pytesseract.tesseract_cmd=r'/opt/homebrew/bin/tesseract'
            text=pytesseract.image_to_string(image,config='--psm 6')
            #file1=open("./ocr_output/result_output.txt","a")
            #file1.write('--------------------new page started ------'+file)
            #file1.write(text)



if __name__ == '__main__':
    print('======================inside main ========================')
    #ocr=ocr_extraction_1()
    # ocr.pdf2img('/Users/sonam/Desktop/1.pdf')
    # ocr.ocr_extraction_f()






