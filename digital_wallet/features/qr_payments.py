import json
from utils.helpers import make_txn, require_account, authenticate_pin

def qr_generate(d, username):
    username = require_account(d, username)
    amt = float(input("Amount to request: "))
    note = input("Note: ") or ""
    payload = {"type": "QR", "recipient": username, "amount": amt, "note": note}
    print("QR Payload (copy and share):")
    print(json.dumps(payload))

def qr_pay(d, payer):
    payer = require_account(d, payer)
    payload_raw = input("Paste QR payload: ")
    payload = json.loads(payload_raw)
    recipient = payload["recipient"]
    amt = float(payload["amount"])
    note = payload.get("note", "QR Payment")
    if not authenticate_pin(d, payer):
        print("PIN failed.")
        return
    if d["accounts"][payer]["balance"] < amt:
        print("Insufficient balance.")
        return
    d["accounts"][payer]["balance"] -= amt
    d["accounts"][recipient]["balance"] += amt
    d["accounts"][payer]["transactions"].append(make_txn("qr_out", amt, note, None, recipient))
    d["accounts"][recipient]["transactions"].append(make_txn("qr_in", amt, note, None, payer))
    print("QR payment successful.")
