import cv2
import time
import mediapipe as mp
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img,draw=False)
    PosList = detector.findPosition(img,draw=False)

    if len(PosList) != 0:
        print(PosList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 5, (255, 0, 255), 3)

    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
