import cv2
from HandTrackModule import HandDet
import math
import pyautogui as pg

# 1920x1080 screen
# 640x480 cam


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDet()
    x_center = 320
    y_center = 240
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lms_list = detector.find_dots(img)
        if len(lms_list) != 0:
            x4, y4 = lms_list[4][1], lms_list[4][2]
            x8, y8 = lms_list[8][1], lms_list[8][2]
            x12,y12 = lms_list[12][1], lms_list[12][2]
            if lms_list[4][2] > 450:
                break
            elif x8 in range (240,400) and y8 in range(160,320) and math.hypot(x8-x4, y8-y4) > 20: # change this range for more work space
                x_dif = x8 - x_center
                y_dif = y8 - y_center
                cv2.line(img, (x_center, y_center), (x8,y8), (255, 0, 255), 1)
                pg.moveTo(pg.position().x - x_dif, pg.position().y + y_dif)
            elif math.hypot(x8-x12, y8-y12) < 20:
                pg.click()
        cv2.rectangle(img, (240, 160), (400, 320), (255, 0, 255), 1)  # drawing work space
        cv2.circle(img, (x_center,y_center), 0, (255, 0, 255), 2)
        cv2.line(img, (0, 450), (640, 450), (255, 0, 255), 1)
        cv2.imshow("Image", cv2.flip(img, 1))
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
