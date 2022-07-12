import cv2
from HandTrackModule import HandDet
import math
import pyautogui as pg

# 1920x1080 screen
# 640x480 cam
# 512x288 work space


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
            x5,y5 = lms_list[5][1], lms_list[5][2]
            x8, y8 = lms_list[8][1], lms_list[8][2]
            x12,y12 = lms_list[12][1], lms_list[12][2]
            x16,y16 = lms_list[16][1], lms_list[16][2]
            if lms_list[4][2] < lms_list[8][2]:
                break
            elif x5 in range (64,576) and y5 in range(96,388) and math.hypot(x5-x4, y5-y4) > 20:  # change this range for more work space
                pg.moveTo(1920 - int((x5 - 64) * 3.75), int((y5 - 96) * 3.75))  # 512x288 * 3,75 = 1920x1080
            elif math.hypot(x12-x8, y12-y8) < 20:
                pg.click()
            elif math.hypot(x12-x16, y12-y16) < 20:
                pg.rightClick()
        cv2.rectangle(img, (64, 96), (576, 388), (255, 0, 255), 1)  # drawing work space
        cv2.circle(img, (x_center,y_center), 0, (255, 0, 255), 2)
        cv2.imshow("Image", cv2.flip(img, 1))
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
