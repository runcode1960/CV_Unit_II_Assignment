import cv2

img = cv2.imread("01_Grayscale/image1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("Original Shape:", img.shape)
print("Gray Shape:", gray.shape)

h, w = gray.shape
print("Height:", h)
print("Width:", w)

cv2.imwrite("output.png", gray)