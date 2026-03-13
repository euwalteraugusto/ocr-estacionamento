import re
from datetime import datetime
from ...domain.entities.ticket import Ticket


class TicketExtractor:

    def extract(self, text: str) -> Ticket:
        placa_match = re.search(r'[A-Z]{3}[0-9][A-Z0-9][0-9]{2}', text)
        datas = re.findall(r'\d{2}/\d{2}/\d{4}', text)
        valor_match = re.search(r'\d+,\d{2}', text)

        placa = placa_match.group() if placa_match else None
        entrada = datas[0] if len(datas) > 0 else None
        saida = datas[1] if len(datas) > 1 else None

        valor = None
        if valor_match:
            valor = float(valor_match.group().replace(",", "."))

        permanencia = None
        if entrada and saida:
            try:
                d1 = datetime.strptime(entrada, "%d/%m/%Y")
                d2 = datetime.strptime(saida, "%d/%m/%Y")
                permanencia = (d2 - d1).days
            except ValueError:
                pass

        status = "OK"
        if not placa or not entrada or not saida or not valor:
            status = "REVISAR"

        return Ticket(
            placa=placa,
            entrada=entrada,
            saida=saida,
            permanencia=permanencia,
            valor=valor,
            status=status
        )