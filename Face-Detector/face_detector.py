#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:50:36 2019

@author: omkarkh1
"""

import numpy as np
import pandas as pd
import cv2
import argparse

# import matplotlib.pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
help="path to our image")
ap.add_argument("-b","--red_scheme",default = 0,help = "input first value of rgb-tuple")
ap.add_argument("-g","--green_scheme",default = 255,help = "input second value of rgb-tuple")
ap.add_argument("-r","--blue_scheme",default = 0,help = "input third value of rgb-tuple")
ap.add_argument("-w","--rectangle_width",default = 20,help = "Width of the Rectangle")
ap.add_argument("-s","--scaling_factor",default = 1.1,help = "Scaling factor for image for more information please refer to openCV Documentation")
ap.add_argument("-n","--min_neighbors",default = 10,help = "Minimum Neighbors for Cascade config.. for more information please refer to openCV Documentation")
args = vars(ap.parse_args())

print("[INFO] Path argument taken")
print("[INFO] Detecting Face")

image = cv2.imread(args['image'])

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('Architecture/haarcascade_frontalface_default.xml')
faces_recieved_from_cascade = face_cascade.detectMultiScale(gray_image, args['scaling_factor'], args['min_neighbors'])

for (x,y,w,h) in faces_recieved_from_cascade:
    cv2.rectangle(image,(x,y),(x+w,y+h),(args['red_scheme'],args['green_scheme'],args['blue_scheme']),args['rectangle_width']) 
    
image = cv2.resize(image,(500,500))
cv2.imshow('detected_image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
