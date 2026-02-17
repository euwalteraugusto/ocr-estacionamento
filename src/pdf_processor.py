from pdf2image import convert_from_path
import cv2
import numpy as np
from config import DPI

images = convert_from_path("arquivo.pdf",
    poppler_path=r"C:\Users\walter.fonseca\Desktop\WALTER\DownloadsForProjects\poppler-25.12.0\Library\bin")

def pdf_to_images(pdf_path):
    pages = convert_from_path(pdf_path, dpi=DPI)
    images = []

    for page in pages:
        open_cv_image = np.array(page)
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
        images.append(open_cv_image)

    return images

def split_into_tickets(image):
    h, w, _ = image.shape

    tickets = [
        image[0:h//2, 0:w//2],
        image[0:h//2, w//2:w],
        image[h//2:h, 0:w//2],
        image[h//2:h, w//2:w]
    ]

    return tickets
