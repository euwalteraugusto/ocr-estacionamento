import pandas as pd
from typing import List
from domain.entities.ticket import Ticket


class ExcelExporter:

    def export(self, tickets: List[Ticket], output_path):

        data = [ticket.__dict__ for ticket in tickets]
        df = pd.DataFrame(data)
        df.to_excel(output_path, index=False)