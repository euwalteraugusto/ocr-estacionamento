# OCR Estacionamento

Pipeline em Python que lê PDFs de tickets de estacionamento, converte cada página em imagem, executa OCR (EasyOCR), extrai os campos relevantes por expressões regulares e consolida tudo em uma planilha Excel.

## Visão geral

1. Cada PDF em `input/` é convertido em imagens (pdf2image + Poppler, 300 DPI).
2. Cada página é dividida em 4 quadrantes (2x2), assumindo 4 tickets por página.
3. O EasyOCR (idioma `pt`, CPU) lê o texto de cada quadrante.
4. O `TicketExtractor` extrai placa, datas de entrada/saída, valor e calcula a permanência em dias.
5. O resultado é exportado para `output/tickets_consolidado.xlsx`.

## Arquitetura

Clean Architecture em camadas; as dependências apontam para dentro (infraestrutura -> aplicação -> domínio).

```
src/
└── ocr_engine/
    ├── main.py                      # composição das dependências e ponto de entrada
    ├── config.py                    # DPI, idiomas, diretórios e caminho do Poppler
    ├── domain/
    │   ├── entities/ticket.py       # dataclass Ticket
    │   └── services/ticket_extractor.py  # regras de extração (regex) e status
    ├── application/
    │   ├── interfaces/              # contratos: OCREngineInterface, PDFProcessorInterface
    │   └── use_cases/process_tickets.py  # ProcessTicketsUseCase (orquestra o fluxo)
    └── infrastructure/
        ├── ocr/easyocr_engine.py            # implementação com EasyOCR
        ├── pdf/pdf2image_processor.py       # PDF -> imagens e divisão em quadrantes
        └── persistence/excel_exporter.py    # exportação com pandas/openpyxl
```

## Requisitos

- Python 3.9+
- [Poppler](https://poppler.freedesktop.org/) (exigido pelo pdf2image)
  - Linux: `sudo apt install poppler-utils`
  - macOS: `brew install poppler`
  - Windows: baixar os binários e definir a variável de ambiente `POPPLER_PATH` com a pasta `bin` (ou colocar `bin` no PATH e não definir a variável)
- Dependências Python (`requirements.txt`): pdf2image, opencv-python, easyocr, pandas, openpyxl, numpy, Pillow

Na primeira execução o EasyOCR baixa os modelos do idioma, então é necessário acesso à internet.

## Instalação

```bash
git clone <url-do-repositorio>
cd ocr-estacionamento
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Defina a variável de ambiente `POPPLER_PATH` (ex.: `set POPPLER_PATH=C:\poppler\Library\bin`). Se o Poppler estiver no PATH, não é necessário.

## Como rodar

Na raiz do projeto:

```bash
mkdir -p input
cp /caminho/dos/seus/*.pdf input/
python -m src.ocr_engine.main
```

## Entrada e saída

- Entrada: arquivos `*.pdf` em `input/` (raiz do projeto).
- Saída: `output/tickets_consolidado.xlsx`, com uma linha por ticket e as colunas:

| Coluna | Descrição |
|---|---|
| `placa` | Placa (padrão antigo ou Mercosul) |
| `entrada` | Primeira data `dd/mm/aaaa` encontrada |
| `saida` | Segunda data encontrada |
| `permanencia` | Diferença em dias entre saída e entrada |
| `valor` | Primeiro valor no formato `0,00` |
| `status` | `OK` ou `REVISAR` (quando algum campo não foi extraído) |

## Limitações

- O layout é fixo: assume exatamente 4 tickets por página, em grade 2x2.
- A extração é por regex sobre o texto bruto; erros de OCR (por exemplo `0`/`O`) geram campos vazios e status `REVISAR`.
- Considera apenas datas (sem horário); a permanência é em dias inteiros.
- O valor extraído é o primeiro número no formato `0,00` do texto, que pode não ser o total do ticket.
- OCR roda somente em CPU (`gpu=False`), o que é lento em lotes grandes.
- O texto OCR bruto é impresso no console a cada ticket (útil para depuração, ruidoso em produção).
- Não há testes automatizados.
- Os PDFs e planilhas podem conter dados pessoais (placas); não os versione.

## Licença

MIT. Veja o arquivo [LICENSE](LICENSE).
