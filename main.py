import cv2
import time
from HandTrackModule import HandDet
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDet()

    while True:
        success, img = cap.read()
        img = detector.find_hands(img)  # add draw = False if u don't want to draw dots and connections


        lms_list = detector.find_dots(img)  # add draw = True if u want to highlight dot
        if len(lms_list) != 0:
            print(lms_list[4])
            if lms_list[4][2] > 450:
                break
            elif lms_list[8][1] > 320:
                cv2.circle(img, (lms_list[8][1], lms_list[8][2]), 10, (255, 0, 255), cv2.FILLED)

        cv2.line(img, (0, 450), (640, 450), (255, 0, 255), 1)
        cv2.putText(img, "off zone", (240, 475), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
