# digital_wallet/qr.py

import logging
import json
from decimal import Decimal
from digital_wallet.data_store import data
from digital_wallet.utils import generate_tx_id
from digital_wallet.operations import transfer_amount

def generate_qr_code_data(receiver: str, amt: Decimal, note="", category=None) -> str:
    """
    QR is created by receiver to receive money.
    Returns JSON string encoding payment request.
    """
    acct = data["accounts"].get(receiver)
    if not acct or amt <= 0:
        logging.error("QR generation failed: %s ₹%s", receiver, amt)
        return ""
    
    tx_id = generate_tx_id()
    payload = {
        "tx_id": tx_id,
        "receiver": receiver,   # QR is for receiving money
        "amount": float(amt),
        "note": note,
        "category": category or "Others"
    }
    qr_string = json.dumps(payload)
    logging.info("QR generated: %s", payload)
    return qr_string

def pay_via_qr_data(payer: str, qr_string: str) -> bool:
    """
    Payer scans/pastes QR to pay the receiver encoded in the QR.
    """
    try:
        payload = json.loads(qr_string)
        receiver = payload["receiver"]
        amt = Decimal(str(payload["amount"]))
        note = payload.get("note", "")
        category = payload.get("category")
    except (json.JSONDecodeError, KeyError):
        logging.error("Invalid QR string")
        return False

    success = transfer_amount(payer, receiver, amt, note, category)
    if success:
        logging.info("QR payment: %s -> %s ₹%.2f", payer, receiver, amt)
    else:
        logging.error("QR payment failed: %s -> %s ₹%.2f", payer, receiver, amt)
    return success

# Aliases
qr_generate = generate_qr_code_data
qr_pay = pay_via_qr_data