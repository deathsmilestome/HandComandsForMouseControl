import cv2
import time
from HandTrackModule import HandDet
import numpy as np
import math
import pyautogui as pg


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDet()

    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lms_list = detector.find_dots(img)
        if len(lms_list) != 0:
            x4, y4 = lms_list[4][1], lms_list[4][2]
            x8, y8 = lms_list[8][1], lms_list[8][2]
            #pg.moveTo(x8 * 3, y8 * 3 )
            if lms_list[4][2] > 450:
                break
            elif x8 > 0:

                #pg.moveTo(pg.position().x + x_dif, pg.position().y + y_dif)
                pg.moveTo(x8*3, y8*3)
            elif math.hypot(x8-x4, y8-y4) < 11:
                print("done")
        #cv2.rectangle(img, (300, 200), (380, 400), (255, 0, 255), 1)
        cv2.line(img, (0, 450), (640, 450), (255, 0, 255), 1)
        cv2.putText(img, "off zone", (240, 475), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
