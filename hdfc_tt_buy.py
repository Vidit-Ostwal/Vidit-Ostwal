"""
USD T.T. Buying (Inward Remittance) rate from HDFC Bank's treasury forex card
rate sheet (a one-page PDF).

The PDF's text layer drops the spaces between words ("UnitedStatesDollar",
"T.T.Buying(Inw Rem)"), so names are compared with all whitespace removed.
The rate column is located by its header name, never by position, so a new
or reordered column can't silently shift us onto the wrong number.
"""

import re
from io import BytesIO

import requests

HDFC_FOREX_RATES_URL = (
    "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/personal-banking/"
    "discover-products/interest-rates/hdfc-bank-treasury-forex-card-rates.pdf"
)
CURRENCY_ROW = "unitedstatesdollar"
CURRENCY_CODE = "USD"
RATE_HEADER = "t.t.buying(inwrem)"


def _squash(cell: str | None) -> str:
    return re.sub(r"\s+", "", cell or "").lower()


def fetch_hdfc_usd_tt_buy() -> str:
    """
    Download the HDFC rate sheet and return USD T.T. Buying (Inw Rem), e.g. "91.50".
    Raises ValueError if the table, column, row or number can't be found exactly.
    """
    import pdfplumber  # imported here so a missing dependency only skips HDFC

    response = requests.get(
        HDFC_FOREX_RATES_URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()

    with pdfplumber.open(BytesIO(response.content)) as pdf:
        page = pdf.pages[0]
        text = page.extract_text() or ""
        tables = page.extract_tables()

    stamp = re.search(r"DATE:\s*([0-9-]+)\s*TIME:\s*([0-9:]+\s*[AP]M)", text)
    if stamp:
        print(f"HDFC rate sheet dated {stamp.group(1)} {stamp.group(2)}")

    for table in tables:
        header = next((row for row in table if row and _squash(row[0]) == "currencytype"), None)
        if header is None:
            continue
        columns = [i for i, cell in enumerate(header) if _squash(cell) == RATE_HEADER]
        if len(columns) != 1:
            raise ValueError(f"Expected one 'T.T. Buying (Inw Rem)' column, found {len(columns)}")
        col = columns[0]

        rows = [
            row for row in table
            if row and _squash(row[0]) == CURRENCY_ROW and (row[1] or "").strip() == CURRENCY_CODE
        ]
        if len(rows) != 1:
            raise ValueError(f"Expected one United States Dollar row, found {len(rows)}")

        value = (rows[0][col] or "").strip()
        if not re.fullmatch(r"[0-9]+\.[0-9]+", value):
            raise ValueError(f"USD T.T. Buying (Inw Rem) is not a number: {value!r}")
        return value

    raise ValueError("Rate table not found in HDFC forex rate PDF")


if __name__ == "__main__":
    print(fetch_hdfc_usd_tt_buy())
