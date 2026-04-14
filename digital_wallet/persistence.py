# digital_wallet/persistence.py

import json
from pathlib import Path
from decimal import Decimal
from digital_wallet.data_store import data
from digital_wallet.constants import CATEGORIES

DATA_FILE = Path(__file__).parent.parent / "data.json"

def load_data():
    """Load wallet data from JSON if it exists."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        # Convert balances to Decimal
        for acct in loaded.get("accounts", {}).values():
            acct["balance"] = Decimal(str(acct.get("balance", 0.0)))
        data.clear()
        data.update(loaded)

    # Ensure categories key exists
    if "categories" not in data:
        data["categories"] = list(CATEGORIES)

def save_data():
    """Save in-memory data to JSON, converting Decimal to float."""
    def convert(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=convert)