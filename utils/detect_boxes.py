import cv2
import numpy as np
from PIL import Image

def detect_colored_boxes(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    results = []

    # Define colors in HSV
    color_ranges = {
        "yellow": ([20, 100, 100], [30, 255, 255]),
        "blue": ([90, 50, 50], [130, 255, 255])
    }

    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in cnts:
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 20 and h > 20:  # skip small noise
                crop = img[y:y+h, x:x+w]
                results.append({
                    "color": color_name,
                    "coords": [x, y, w, h],
                    "image": crop
                })

    return results
