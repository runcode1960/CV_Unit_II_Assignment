import cv2
import numpy as np

img = cv2.imread("image2.jpg")

before = img[50,50]

bright = np.clip(img + 50, 0, 255).astype(np.uint8)

after = bright[50,50]

print("Before:", before)
print("After:", after)

cv2.imwrite("output.png", bright)