import cv2


def nothing(value):
    pass


cv2.namedWindow('win1')
img1 = cv2.imread('blend.jpg')
img2 = cv2.imread('logo.png')
cv2.createTrackbar('Ratio', 'win1', 0, 100, nothing)
cv2.setTrackbarPos('Ratio', 'win1', 50)

while True:
    alpha = cv2.getTrackbarPos('Ratio', 'win1')/100
    beta = 1 - alpha
    dst = cv2.addWeighted(img1, alpha, img2, beta, 0)
    cv2.imshow('win1', dst)
    key = cv2.waitKey(1)
    if key == 27:
        break

