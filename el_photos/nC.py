import cv2

# Gri tonlamalı görüntüyü yükle
img = cv2.imread("/home/azarakuss/development/el_photos/out-2436-30.jpeg", cv2.IMREAD_GRAYSCALE)

# Histogram dengeleme işlemi uygula
gaussian_img = cv2.GaussianBlur(img, (5,5), 0)
sharp_img = cv2.addWeighted(img, 1.5, gaussian_img, -0.5, 0)
equalized_img = cv2.equalizeHist(sharp_img)


# Siyah çizgileri belirginleştirmek için adaptif eşikleme uygula
#thresh = cv2.adaptiveThreshold(equalized_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 5)

# Görüntüyü kaydet
cv2.imwrite("sonuc.jpg", equalized_img)
