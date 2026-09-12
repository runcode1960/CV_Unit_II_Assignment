import cv2
import numpy as np

img = cv2.imread("image71.jpg",0)

dft = cv2.dft(np.float32(img),
              flags=cv2.DFT_COMPLEX_OUTPUT)

shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

mask = np.ones((rows,cols,2),np.uint8)

mask[crow-30:crow+30,
     ccol-30:ccol+30] = 0

fshift = shift * mask

ishift = np.fft.ifftshift(fshift)

img_back = cv2.idft(ishift)

img_back = cv2.magnitude(
    img_back[:,:,0],
    img_back[:,:,1]
)

cv2.imwrite("output.png", img_back)