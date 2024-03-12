import time

import cv2
import mediapipe
import cvzone
from cvzone.HandTrackingModule import HandDetector
import random
time_initia = time.time()
def open_camera():
    vid = cv2.VideoCapture(0)
    while (True):

        ret, frame = vid.read()

        framescaled = cv2.resize(frame,(0 ,0) , None,0.875,0.875)

        cv2.imshow('frame', framescaled)
        detector = HandDetector(maxHands=1)

        hands, frame = detector.findHands(framescaled)
        if hands:
            hand = hands[0]
            bbox1 = hand["bbox"]
            fingers = detector.fingersUp(hand)
            timefinal = time.time()
            if timefinal-time_initia >1:
                if fingers == [0, 0, 0, 0, 0]:
                    user_choice = 1
                elif fingers==[1,1,1,1,1]:
                    user_choice = 2
                elif fingers==[0, 1, 1, 0, 0]:
                    user_choice =3
                
                computer_choice = random.randint(1,3)

                if (user_choice ==1 and computer_choice ==3 or user_choice==2 and computer_choice==1
                        or user_choice==3 and computer_choice==2):
                    print("you won")
                    break
                elif user_choice==computer_choice:
                    print("its a tie")
                    break
                else:
                    print("you loose")
                    break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



open_camera()
