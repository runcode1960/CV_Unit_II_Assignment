import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image5.jpg",0)

eq = cv2.equalizeHist(img)

cv2.imwrite("output.png", eq)

plt.subplot(1,2,1)
plt.hist(img.ravel(),256,[0,256])

plt.subplot(1,2,2)
plt.hist(eq.ravel(),256,[0,256])

plt.savefig("histogram_comparison.png")
plt.close()