from pdf2image import convert_from_path
import cv2
import numpy as np
from config import DPI

# Note: avoid running conversion at import time. The example call above was
# left in the file accidentally and caused an I/O error when the module was
# imported by `main.py`.  The functions below handle conversion on demand.


from config import DPI, POPPLER_PATH

def pdf_to_images(pdf_path):
    # convert a PDF file to a list of OpenCV images.  The caller is
    # responsible for passing a valid path; a missing file will generate an
    # exception from pdf2image which we allow to bubble up so the caller can
    # handle or log it.
    kwargs = {"dpi": DPI}
    if POPPLER_PATH:
        kwargs["poppler_path"] = POPPLER_PATH

    pages = convert_from_path(pdf_path, **kwargs)
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
