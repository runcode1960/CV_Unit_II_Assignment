import cv2

img = cv2.imread("image23.jpg")

result = cv2.medianBlur(img, 5)

cv2.imwrite("output.png", result)