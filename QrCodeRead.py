
from ast import While
import profile
from tkinter import W
import cv2
from cv2 import VideoCapture
import numpy as np
from pyzbar.pyzbar import decode

#profile = cv2.imread('Github.jpg')

scan = cv2.VideoCapture(0)
scan.set(3,640)
scan.set (4,480)

while True:
    okinayan, profile = scan.read()
    for qr in decode(profile):
        github = qr.data.decode('utf-8')
        print(github)

    cv2.imshow('Huli',profile)
    cv2.waitKey(1)