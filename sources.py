#!/usr/bin/python
# -*- coding: utf-8 -*-

from settings import detectionCon
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from cvzone.HandTrackingModule import HandDetector
from DragRect import DragRect
Detector = HandDetector(detectionCon=detectionCon, maxHands=2)

Rect_list = list()
for i in range(5):
    Rect_list.append(DragRect())

