from abc import ABC, abstractmethod
import numpy as np


class OCREngineInterface(ABC):

    @abstractmethod
    def extract_text(self, image: np.ndarray) -> str:
        pass