import cv2
import os

path = '/home/xenom0rph/PycharmProjects/wdpo2/' #input target path (needs forward slashes on both sides, e.g. /path/)
images = []
names = []
for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        images.append(cv2.imread(path + filename, cv2.IMREAD_COLOR))
        names.append(filename)
        print("File found: " + path + filename)
        continue
    else:
        continue

total = len(images)
print("Previewing " + str(total) + " images in total.")
current = 0
while True:
    cv2.imshow(names[current], images[current])
    print('DEBUG: Displaying image ' + str(current + 1) + ' out of ' + str(total) + '. Name: ' + names[current])
    key = cv2.waitKey(0)
    if key == 81:
        cv2.destroyWindow(names[current])
        if current == 0:
            current = total - 1
        else:
            current = current - 1
    elif key == 83:
        cv2.destroyWindow(names[current])
        if current == total - 1:
            current = 0
        else:
            current = current + 1
    elif key == 27:
        cv2.destroyAllWindows()
        break
