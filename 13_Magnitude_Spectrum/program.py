import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image51.jpg",0)

dft = cv2.dft(np.float32(img),
              flags=cv2.DFT_COMPLEX_OUTPUT)

shift = np.fft.fftshift(dft)

mag = 20*np.log(
    cv2.magnitude(shift[:,:,0],
                  shift[:,:,1])+1
)

plt.imshow(mag,cmap='gray')
plt.axis("off")

plt.savefig("output.png")
plt.close()