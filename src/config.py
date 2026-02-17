from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

pdf_path = BASE_DIR / "arquivo.pdf"

INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"
LOG_DIR = BASE_DIR / "data" / "logs"

DPI = 300
LANGUAGES = ['pt']
