import cv2
from pathlib import Path

# Read the input image
image_path = Path(__file__).parent / "image23.jpg"
img = cv2.imread(str(image_path))

if img is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

# Apply a 5 x 5 mean filter
mean_filtered = cv2.blur(img, (5, 5))

# Save the filtered image
output_path = Path(__file__).parent / "output.png"
cv2.imwrite(str(output_path), mean_filtered)

print("Mean filter applied successfully.")
