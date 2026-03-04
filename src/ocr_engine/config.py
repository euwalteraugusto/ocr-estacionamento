from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"
LOG_DIR = BASE_DIR / "data" / "logs"

# Parâmetros para o pipeline de OCR
DPI = 300
LANGUAGES = ['pt']

# O uso do pdf2imagerequer Poppler instalado e fornecer seu
# diretório binário. Configure isso para a localização correta no seu sistema, ou deixe
# como None se o poppler estiver no seu PATH.
POPPLER_PATH = r"C:\Users\walter.fonseca\DownloadsForProjects\poppler-25.12.0\Library\bin"

