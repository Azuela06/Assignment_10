
from ast import While
import profile
from tkinter import W
import cv2
from cv2 import VideoCapture
import numpy as np
from pyzbar.pyzbar import decode
import datetime

def print_time():
    time = datetime.datetime.now() 
    return time.strftime("%d-%m-%Y %H:%M:%S")

scan = cv2.VideoCapture(0)
scan.set(3,640)
scan.set (4,480)

while True:
    okinayan, profile = scan.read()
    for qr in decode(profile):
        github = qr.data.decode('utf-8')
        side = np.array([qr.polygon],np.int32)
        side = side.reshape((-1,1,2))
        cv2.polylines(profile,[side],True,(215,252,100))
        with open("QrData.txt", "w") as txt:
            txt.write(github)
            txt.write(print_time())


    cv2.imshow('Huli, akin na data mo',profile)
    cv2.waitKey(1)