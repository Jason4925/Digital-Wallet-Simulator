# digital_wallet/utils.py

import uuid
from datetime import datetime

used_tx_ids = set()

def generate_tx_id():
    """Generate unique 8-character transaction ID."""
    while True:
        tx_id = uuid.uuid4().hex[:8]
        if tx_id not in used_tx_ids:
            used_tx_ids.add(tx_id)
            return tx_id

def current_timestamp():
    """Return timestamp string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") 