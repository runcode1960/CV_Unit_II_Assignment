import cv2
import numpy as np

img = cv2.imread("boy (2).jpg",0)

f = np.float32(img)

dft = cv2.dft(f,flags=cv2.DFT_COMPLEX_OUTPUT)

shift = np.fft.fftshift(dft)

print("Original:", img.shape)
print("DFT:", dft.shape)
print("Shifted:", shift.shape)

cv2.imwrite("output.png", img)