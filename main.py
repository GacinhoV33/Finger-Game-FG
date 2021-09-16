#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import cv2 as cv
import cvzone

import numpy as np
from settings import X_S, Y_S, Resolution, Res_center, ColorRect, DetectRectColor
from sources import Detector, Rect_list, Circle_list, Elipse, BallImage, BallRect, overlay_transparent
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

            if length < 55:

                #updating the objects and their position
                # for rect in Rect_list:
                #     rect.update(cursor)
                # for circle in Circle_list:
                #     circle.update(cursor)
                BallRect.update(cursor)
                # Elipse.update(cursor)
        else:
            cv.rectangle(frame, (0, 0), (15, 15), DetectRectColor, cv.FILLED)


        #drawing the objects from resources
        ball_x, ball_y = BallRect.posCenter
        ball_w, ball_h = BallRect.size

        # drawing geometry shapes
        # for rect in Rect_list:
        #     centerx, centery = rect.posCenter
        #     w, h = rect.size
        #     cv.rectangle(frame, (int(centerx - w // 2), int(centery - h // 2)),
        #                  (int(centerx + w // 2), int(centery + h // 2)),
        #                  ColorRect, cv.FILLED)
        #     # cvzone.cornerRect(frame, (int(centerx - w // 2), int(centery - h // 2), w, h), 20, rt=0)
        # for circle in Circle_list:
        #     centerx, centery = circle.posCenter
        #     w, _ = circle.size
        #     cv.circle(frame, (centerx, centery), w, thickness=cv.FILLED, color=(0, 255, 0))
        #

        # for jpg

        # frame[ball_y-ball_h//2:ball_y+ball_h//2, ball_x-ball_w//2:ball_x+ball_w//2] = BallImage

        # for png

        frame = cvzone.overlayPNG(frame, BallImage, [ball_x - ball_w//2, ball_y-ball_h//2])
        # frame = overlay_transparent(frame, BallImage, ball_x - ball_w//2, ball_y-ball_h//2)



        # cv.ellipse(frame, Elipse.posCenter, (Elipse.size[0], Elipse.size[1]), 0, 180, 360, (20, 43, 222), thickness=cv.FILLED)

        cv.imshow('FG', frame)
        cv.waitKey(1)


def Options():
    OptionsRoot = Toplevel()
    OptionsRoot.title("Options")
    OptionsRoot.geometry("300x500")


    OptionsRoot.mainloop()


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
    OptionButton = Button(Root, text="Options", padx=int(X_S/21.5), pady=int(Y_S/22), font=("Helvetica", 23), command=Options)
    OptionButton.place(x=int(X_S/2 - 6 * X_S/15), y=int(Y_S/1.2 - 3 * Y_S/72))
    # canv.create_text(Root, )


    Root.mainloop()









