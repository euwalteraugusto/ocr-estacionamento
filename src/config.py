from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# sample path used previously in pdf_processor; kept for reference but not used
pdf_path = BASE_DIR / "arquivo.pdf"

INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"
LOG_DIR = BASE_DIR / "data" / "logs"

# Parameters for the OCR pipeline
DPI = 300
LANGUAGES = ['pt']

# If you're using pdf2image you must have Poppler installed and provide its
# binary directory. Set this to the correct location on your system, or leave
# as None if poppler is on your PATH.
POPPLER_PATH = r"C:\Users\walter.fonseca\DownloadsForProjects\poppler-25.12.0\Library\bin"  # adjust as needed

