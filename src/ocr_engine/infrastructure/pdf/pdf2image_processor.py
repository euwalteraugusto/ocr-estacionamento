from pdf2image import convert_from_path
import cv2
import numpy as np
from ...config import DPI, POPPLER_PATH
from ...application.interfaces.pdf_interface import PDFProcessorInterface


class PDF2ImageProcessor(PDFProcessorInterface):

    def convert_to_images(self, pdf_path):
        kwargs = {"dpi": DPI}
        if POPPLER_PATH:
            kwargs["poppler_path"] = POPPLER_PATH

        pages = convert_from_path(pdf_path, **kwargs)

        images = []
        for page in pages:
            img = np.array(page)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            images.append(img)

        return images

    def split_into_tickets(self, image):
        h, w, _ = image.shape
        return [
            image[0:h//2, 0:w//2],
            image[0:h//2, w//2:w],
            image[h//2:h, 0:w//2],
            image[h//2:h, w//2:w]
        ]