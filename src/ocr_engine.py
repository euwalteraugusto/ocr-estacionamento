import easyocr
import cv2

reader = easyocr.Reader(['pt'], gpu=False)

def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)

    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )
    return thresh


def extract_text(image):
    processed = preprocess(image)
    results = reader.readtext(processed, detail=0)
    return " ".join(results)
