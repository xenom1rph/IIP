import cv2


def negative(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            for k in range(len(image[i][j])):
                image[i][j][k] = 255 - image[i][j][k]


img = cv2.imread('img.jpeg')
negative(img)
cv2.imshow('win1', img)
cv2.waitKey(0)



