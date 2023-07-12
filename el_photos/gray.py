import cv2, numpy as np

img = cv2.imread("/home/azarakuss/development/el_photos/out-2436-30.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(gray)
kernel = np.ones((5, 5), np.uint8)
image = cv2.erode(equ, kernel)

cv2.imwrite("gray2436-33.jpeg", gray)
