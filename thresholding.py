import cv2
import numpy as np


def empty_callback(value):
    pass


img = cv2.imread('img.jpeg')
img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('window1')
cv2.createTrackbar('Threshold', 'window1', 0, 255, empty_callback)
cv2.setTrackbarPos('Threshold', 'window1', 120)
cv2.createTrackbar('Threshold Type', 'window1', 0, 4, empty_callback)

while True:
    type = cv2.getTrackbarPos('Threshold Type', 'window1')
    if type == 0:
        ttype = cv2.THRESH_BINARY
    elif type == 1:
        ttype = cv2.THRESH_BINARY_INV
    elif type == 2:
        ttype = cv2.THRESH_TRUNC
    elif type == 3:
        ttype = cv2.THRESH_TOZERO
    elif type == 4:
        ttype = cv2.THRESH_TOZERO_INV

    threshold = cv2.getTrackbarPos('Threshold', 'window1')
    ret, thresh = cv2.threshold(img_gs, threshold, 255, ttype)
    cv2.imshow('window1', thresh)
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()
        break

