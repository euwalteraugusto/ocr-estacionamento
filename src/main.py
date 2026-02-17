import pandas as pd
from pathlib import Path
from config import INPUT_DIR, OUTPUT_DIR
from pdf_processor import pdf_to_images, split_into_tickets
from ocr_engine import extract_text
from extractor import extract_fields


def process_all_pdfs():
    all_data = []

    pdf_files = list(INPUT_DIR.glob("*.pdf"))

    for pdf in pdf_files:
        print(f"Processando: {pdf.name}")
        images = pdf_to_images(pdf)

        for img in images:
            tickets = split_into_tickets(img)

            for ticket in tickets:
                text = extract_text(ticket)
                data = extract_fields(text)
                all_data.append(data)

    return all_data


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    data = process_all_pdfs()

    df = pd.DataFrame(data)
    output_file = OUTPUT_DIR / "tickets_consolidado.xlsx"
    df.to_excel(output_file, index=False)

    print("Processamento finalizado.")
