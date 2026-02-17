import re
from datetime import datetime

def extract_fields(text):

    placa_match = re.search(r'[A-Z]{3}[0-9][A-Z0-9][0-9]{2}', text)
    datas = re.findall(r'\d{2}/\d{2}/\d{4}', text)
    valor_match = re.search(r'\d+,\d{2}', text)

    placa = placa_match.group() if placa_match else None
    entrada = datas[0] if len(datas) > 0 else None
    saida = datas[1] if len(datas) > 1 else None
    valor = valor_match.group() if valor_match else None

    permanencia = None
    if entrada and saida:
        try:
            d1 = datetime.strptime(entrada, "%d/%m/%Y")
            d2 = datetime.strptime(saida, "%d/%m/%Y")
            permanencia = (d2 - d1).days
        except:
            permanencia = None

    status = "OK"
    if not placa or not entrada or not saida or not valor:
        status = "REVISAR"

    return {
        "PLACA": placa,
        "ENTRADA": entrada,
        "SAIDA": saida,
        "PERMANENCIA": permanencia,
        "VALOR": valor,
        "STATUS": status
    }
