import easyocr
import cv2
from config import LANGUAGES
from application.interfaces.ocr_interface import OCREngineInterface


class EasyOCREngine(OCREngineInterface):

    def __init__(self):
        self.reader = easyocr.Reader(LANGUAGES, gpu=False)

    def preprocess(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    def extract_text(self, image):
        processed = self.preprocess(image)
        result = self.reader.readtext(processed, detail=0)
        return " ".join(result)