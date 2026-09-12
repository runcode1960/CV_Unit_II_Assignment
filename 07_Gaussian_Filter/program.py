import cv2
from pathlib import Path

image_path = Path(__file__).parent / "img.jpg"
img = cv2.imread(str(image_path))

if img is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

result = cv2.GaussianBlur(img,(7,7),0)

cv2.imwrite(str(Path(__file__).parent / "output.png"), result)
