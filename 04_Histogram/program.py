import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image6.jpg",0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])

print("Highest frequency intensity:",
      np.argmax(hist))

plt.plot(hist)
plt.title("Histogram")
plt.savefig("output.png")
plt.close()