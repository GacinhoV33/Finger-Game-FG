#!/usr/bin/python
# -*- coding: utf-8 -*-

from settings import detectionCon
from cvzone.HandTrackingModule import HandDetector
from DragRect import DragFigure
Detector = HandDetector(detectionCon=detectionCon, maxHands=2)

# Rect_list = list()
Circle_list = list()
#
# for i in range(5):
#     Rect_list.append(DragFigure())

Rect_list = [DragFigure([50, 130], [100, 200])]
Circle_list.append(DragFigure([250, 250], [80, 80]))
Circle_list.append(DragFigure([500, 250], [80, 80]))

Elipse = DragFigure([450, 500], [75, 75])