"""
USD "TT Buying rate" from ICICI Bank's forex card rates page.

The page is server-rendered: a table whose header has two rows
("Currency" spanning both, then "Bank Buying Rate" / "Bank Selling Rate"
groups over the individual rate columns). The currency filter on the page only
hides rows client-side, so the full table is in the HTML. The rate column is
located by its header name and the row by its currency name, never by position.
"""

import re
from html.parser import HTMLParser

import requests

ICICI_FOREX_RATES_URL = "https://www.icici.bank.in/business-banking/global-markets/forex/forex-card-rates"
CURRENCY_ROW = "United States Dollar (USD)"
RATE_HEADER = "TT Buying rate"


class _RateTableParser(HTMLParser):
    """Collects every table as {"head": [[cells]], "body": [[cells]]}."""

    def __init__(self):
        super().__init__()
        self.tables = []
        self._section = None
        self._row = None
        self._cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.tables.append({"head": [], "body": []})
        elif not self.tables:
            return
        elif tag in ("thead", "tbody"):
            self._section = "head" if tag == "thead" else "body"
        elif tag == "tr":
            self._row = []
        elif tag in ("th", "td") and self._row is not None:
            self._cell = []

    def handle_endtag(self, tag):
        if tag in ("th", "td") and self._cell is not None:
            self._row.append(re.sub(r"\s+", " ", "".join(self._cell)).strip())
            self._cell = None
        elif tag == "tr" and self._row is not None:
            if self._section:
                self.tables[-1][self._section].append(self._row)
            self._row = None
        elif tag in ("thead", "tbody"):
            self._section = None

    def handle_data(self, data):
        if self._cell is not None:
            self._cell.append(data)


def fetch_icici_usd_tt_buy() -> str:
    """
    Return ICICI's USD "TT Buying rate", e.g. "91.53".
    Raises ValueError if the table, column, row or number can't be found exactly.
    """
    response = requests.get(
        ICICI_FOREX_RATES_URL,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()
    html = response.text

    stamp = re.search(r"Last updated on:\s*(?:&nbsp;)?\s*([0-9-]+)\s*(?:&nbsp;)?\|(?:&nbsp;)?\s*([0-9:]+\s*[AP]M)", html, re.I)
    if stamp:
        print(f"ICICI rate page last updated {stamp.group(1)} {stamp.group(2)}")

    parser = _RateTableParser()
    parser.feed(html)

    for table in parser.tables:
        head = table["head"]
        if len(head) != 2 or RATE_HEADER not in head[1]:
            continue
        # Row 1 is "Currency" (spanning both header rows) plus group labels;
        # row 2 holds the per-column names, aligned with data cells 1..n.
        leaf_headers = head[1]
        columns = [i for i, name in enumerate(leaf_headers) if name == RATE_HEADER]
        if len(columns) != 1:
            raise ValueError(f"Expected one '{RATE_HEADER}' column, found {len(columns)}")

        rows = [row for row in table["body"] if row and row[0] == CURRENCY_ROW]
        if len(rows) != 1:
            raise ValueError(f"Expected one '{CURRENCY_ROW}' row, found {len(rows)}")
        row = rows[0]
        if len(row) != 1 + len(leaf_headers):
            raise ValueError(f"USD row has {len(row)} cells, expected {1 + len(leaf_headers)}")

        value = row[1 + columns[0]]
        if not re.fullmatch(r"[0-9]+(\.[0-9]+)?", value):
            raise ValueError(f"USD TT Buying rate is not a number: {value!r}")
        return value

    raise ValueError("Forex rate table not found on ICICI page")


if __name__ == "__main__":
    print(fetch_icici_usd_tt_buy())
