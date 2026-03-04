from dataclasses import dataclass
from typing import Optional


@dataclass
class Ticket:
    placa: Optional[str]
    entrada: Optional[str]
    saida: Optional[str]
    permanencia: Optional[int]
    valor: Optional[float]
    status: str