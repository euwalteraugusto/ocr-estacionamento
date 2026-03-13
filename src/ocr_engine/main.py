from pathlib import Path
from .config import INPUT_DIR, OUTPUT_DIR
from .infrastructure.ocr.easyocr_engine import EasyOCREngine
from .infrastructure.pdf.pdf2image_processor import PDF2ImageProcessor
from .infrastructure.persistence.excel_exporter import ExcelExporter
from .application.use_cases.process_tickets import ProcessTicketsUseCase


def main():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = list(INPUT_DIR.glob("*.pdf"))
    print(f"PDFs encontrados: {len(pdf_files)}")
    print(pdf_files)

    pdf_processor = PDF2ImageProcessor()
    ocr_engine = EasyOCREngine()

    use_case = ProcessTicketsUseCase(pdf_processor, ocr_engine)

    tickets = use_case.execute(pdf_files)

    exporter = ExcelExporter()
    exporter.export(tickets, OUTPUT_DIR / "tickets_consolidado.xlsx")


if __name__ == "__main__":
    main()