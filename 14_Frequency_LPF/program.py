import cv2
import numpy as np

img = cv2.imread("image90.jpg",0)

dft = cv2.dft(np.float32(img),
              flags=cv2.DFT_COMPLEX_OUTPUT)

shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

mask = np.zeros((rows,cols,2),np.uint8)

mask[crow-30:crow+30,
     ccol-30:ccol+30] = 1

fshift = shift * mask

ishift = np.fft.ifftshift(fshift)

img_back = cv2.idft(ishift)

img_back = cv2.magnitude(
    img_back[:,:,0],
    img_back[:,:,1]
)

img_back = cv2.normalize(
    img_back, None, 0, 255, cv2.NORM_MINMAX
)

cv2.imwrite("output.png", img_back)