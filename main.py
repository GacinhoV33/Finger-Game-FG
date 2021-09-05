#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import cv2 as cv
import cvzone

import numpy as np
from settings import X_S, Y_S, Resolution, Res_center, ColorRect
from sources import Detector, Rect_list
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def Game(Root):
    # GameRoot = Toplevel()
    # GameRoot.geometry(f'{Resolution[0]}x{Resolution[1]}')
    try:
        Camera = cv.VideoCapture(0)
    except Exception as exc:
        try:
            Camera = cv.VideoCapture(1)
        except Exception as exc:
            messagebox.showerror("Error", "No Camera Found")
            Root.destroy()
            return 0

    Camera.set(3, Resolution[0])
    Camera.set(4, Resolution[1])

    while True:
        success, frame = Camera.read()
        if not success:
            break
        frame = cv.flip(frame, 1)

        hands = Detector.findHands(frame, flipType=False, draw=False)

        if hands:
            hand1 = hands[0]
            lmList = hand1['lmList']
            cursor = lmList[8]
            length, _ = Detector.findDistance(lmList[8], lmList[12])

            if length < 50:
                for rect in Rect_list:
                    rect.update(cursor)
        for rect in Rect_list:
            centerx, centery = rect.posCenter
            w, h = rect.size
            cv.rectangle(frame, (int(centerx - w // 2), int(centery - h // 2)), (int(centerx + w // 2), int(centery + h // 2)),
                         ColorRect, cv.FILLED)
            cvzone.cornerRect(frame, (int(centerx - w // 2), int(centery - h // 2), w, h), 20, rt=0)
        #
        # elif len(hands) == 2:
        #     hand1 = hands[0]
        #     hand2 = hands[1]
        #
        # else:
        #     pass

        cv.imshow('FG', frame)
        cv.waitKey(1)


if __name__ == '__main__':
    Root = Tk()
    Root.geometry(f'{Resolution[0]}x{Resolution[1]}+{Res_center[0]}+{Res_center[1]}')
    Root.title('Finger Game')
    Root.wm_attributes('-transparentcolor', '#ab23ff')
    logo_img = ImageTk.PhotoImage(file='images/intro.jpg')
    Root.tk.call('wm', 'iconphoto', Root._w, logo_img)
    canv = Canvas(Root, width=Resolution[0], height=Resolution[1], bg='white')
    canv.pack(fill="both", expand=True)
    startImg = ImageTk.PhotoImage((Image.open('images/intro.jpg')).resize((Resolution[0], Resolution[1])), Image.ANTIALIAS)
    canv.create_image(0, 0, anchor=NW, image=startImg)
    print(X_S, Y_S)
    StartButton = Button(Root, text="Start", padx=int(X_S/15), pady=int(Y_S/22), font=("Helvetica", 23), command=lambda: Game(Root))
    StartButton.place(x=int(X_S/2 - 1.5 * X_S/15), y=int(Y_S/1.2 - 3 * Y_S/72))
    #
    # canv.create_text(Root, )


    Root.mainloop()









