
# Importing library
from ocr_extraction import ocr_extraction_1
import os
import datetime
from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import cv2
import numpy
import shutil

# Intializing fastapi services and calling ocr_extraction file
app=FastAPI()
origins=["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )
@app.post("/uploadfile/")
async def upload_file(file : UploadFile=File(...)):
    in_file=('./input_file/')
    print('----------',file.filename)
    ocr = ocr_extraction_1()
    ocr.pdf2img(in_file+file.filename)
    ocr.ocr_extraction_f()
    #shutil.copy(file.filename,in_file)









