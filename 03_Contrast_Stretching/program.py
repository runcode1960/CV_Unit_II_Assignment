import cv2
import numpy as np
from pathlib import Path

image_path = Path(__file__).parent / "image10.jpg"
img = cv2.imread(str(image_path))

if img is None:
    raise FileNotFoundError(f"Could not load image: {image_path}")

min_val = img.min()
max_val = img.max()

if max_val == min_val:
    result = img.copy()
else:
    result = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("Contrast stretched", result)
cv2.waitKey(0)
cv2.destroyAllWindows()