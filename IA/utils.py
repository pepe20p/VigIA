import cv2
import numpy as np
import json
import os
import sys

fps = 0.0
precision = 60.0

def set_precision(new_precision):
    global precision
    if(new_precision <= 0):
        raise ValueError("O valor da precisão deve ser maior que zero.")
    precision = new_precision

def get_precision():
    return precision

def set_fps(new_fps):
    global fps
    if(new_fps <= 0):
        raise ValueError("O valor de FPS deve ser maior que zero.")
    fps = new_fps

def get_fps():
    return fps

class_names = []
util_class_names = []
with open("coconames", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
with open("utilnames", "r") as f:
    util_class_names = [cname.strip() for cname in f.readlines()]

net = cv2.dnn.readNet("yolov7-tiny.weights", "yolov7-tiny.cfg")
model = cv2.dnn.DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)