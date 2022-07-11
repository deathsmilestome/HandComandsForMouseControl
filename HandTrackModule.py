import cv2
import mediapipe as mp


# 640x480 cam
class HandDet:
    def __init__(self, mode=False, max_hands=2, complexity=1, detection_conf=0.5, track_conf=0.5):

        self.results = None
        self.lms_list = None
        self.mode = mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.detection_conf = detection_conf
        self.track_conf = track_conf

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.complexity, self.detection_conf,
                                         self.track_conf, )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_dots(self, img, hand_N=0, draw=False):
        self.lms_list = []
        if self.results.multi_hand_landmarks:
            hand_lms = self.results.multi_hand_landmarks[hand_N]
            for id, lm in enumerate(hand_lms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lms_list.append([id, cx, cy])  # add "if id ==" construction for your needed dots
                if draw:  # you can add "and id == " to highlight some dots| don't forget to put draw=True in main
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        return self.lms_list  # you can return positions for any dot check line 38

