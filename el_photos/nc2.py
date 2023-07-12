import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
import numpy as np

# görüntüyü yükle
image = cv2.imread('/home/azarakuss/development/el_photos/out-2436-30.jpeg')

# görüntüyü siyah beyaz formata dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# kernel boyutu belirle
img = cv2.equalizeHist(gray_image)

mf = median_filter(img, 1)
lap = cv2.Laplacian(mf,cv2.CV_64F)
sharp = img - 0.7*lap


# sonuçları göster
cv2.imwrite("sonuc2.jpg", sharp)
