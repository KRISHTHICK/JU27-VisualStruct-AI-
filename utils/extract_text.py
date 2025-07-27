import pytesseract
from PIL import Image

def extract_text_from_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray, config='--psm 6').strip()
