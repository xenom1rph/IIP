import time

import cv2
import time as t

img = cv2.imread('cube.jpeg')
t1 = t.perf_counter()
img1 = cv2.resize(img, (0, 0), fx=2.5, fy=2.5, interpolation=cv2.INTER_LINEAR)
print('Linear: ' + str(t.process_time()))

t2 = t.perf_counter()
img2 = cv2.resize(img, (0, 0), fx=2.5, fy=2.5, interpolation=cv2.INTER_NEAREST)
print('Nearest: ' + str(t.process_time()))

t3 = t.perf_counter()
img3 = cv2.resize(img, (0, 0), fx=2.5, fy=2.5, interpolation=cv2.INTER_AREA)
print('Area: ' + str(t.process_time()))

t4 = t.perf_counter()
img4 = cv2.resize(img, (0, 0), fx=2.5, fy=2.5, interpolation=cv2.INTER_LANCZOS4)
print('Lanczos4: ' + str(t.process_time()))

imgs = [img1, img2, img3, img4]

while True:
    for i in range(len(imgs)):
        cv2.imshow('window' + str(i), imgs[i])
    key = cv2.waitKey(1)
    if key == 27:
        break
