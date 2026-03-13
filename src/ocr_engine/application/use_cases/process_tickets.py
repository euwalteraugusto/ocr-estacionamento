from typing import List
from ...domain.services.ticket_extractor import TicketExtractor
from ...domain.entities.ticket import Ticket


class ProcessTicketsUseCase:

    def __init__(self, pdf_processor, ocr_engine):
        self.pdf_processor = pdf_processor
        self.ocr_engine = ocr_engine
        self.extractor = TicketExtractor()

    def execute(self, pdf_files: List[str]) -> List[Ticket]:

        tickets = []

        for pdf in pdf_files:
            images = self.pdf_processor.convert_to_images(pdf)

            for image in images:
                splitted = self.pdf_processor.split_into_tickets(image)

                for ticket_img in splitted:
                    text = self.ocr_engine.extract_text(ticket_img)
                    print("=== TEXTO OCR ===")
                    print(text)
                    print("=================")
                    ticket = self.extractor.extract(text)
                    tickets.append(ticket)

        return tickets