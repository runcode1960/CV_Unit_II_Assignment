import cv2

img = cv2.imread("image23.jpg")

mean_img = cv2.blur(img,(5,5))
gaussian_img = cv2.GaussianBlur(img,(5,5),0)
median_img = cv2.medianBlur(img,5)

cv2.imwrite("output_mean.png", mean_img)
cv2.imwrite("output_gaussian.png", gaussian_img)
cv2.imwrite("output_median.png", median_img)

