# def add(a, b):
#     return a + b
# a=4
# b=5
# print(add(a, b))
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
print('del')        