from abc import ABC, abstractmethod
from typing import List
import numpy as np


class PDFProcessorInterface(ABC):

    @abstractmethod
    def convert_to_images(self, pdf_path: str) -> List[np.ndarray]:
        pass

    @abstractmethod
    def split_into_tickets(self, image: np.ndarray) -> List[np.ndarray]:
        pass