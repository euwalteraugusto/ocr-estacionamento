import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"

# Parâmetros para o pipeline de OCR
DPI = 300
LANGUAGES = ['pt']

# O uso do pdf2imagerequer Poppler instalado e fornecer seu
# diretório binário. Defina a variável de ambiente POPPLER_PATH com o diretório bin, ou deixe
# sem definir se o poppler estiver no seu PATH.
POPPLER_PATH = os.getenv("POPPLER_PATH") or None

