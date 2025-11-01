import time
from datetime import datetime

def make_txn(txn_type, amount, note, category, counterparty):
    """Create a transaction dict (optional helper to reuse)."""
    return {
        "id": str(int(time.time() * 1000)),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": txn_type,
        "amount": round(float(amount), 2),
        "note": note,
        "category": category,
        "counterparty": counterparty
    }

def normalize(username: str) -> str:
    return username.strip().lower()

def valid_pin_format(pin: str) -> bool:
    return isinstance(pin, str) and pin.isdigit() and len(pin) == 4

def ensure_account_fields(d, username):
    acc = d["accounts"].get(username)
    if acc is None:
        return
    if "transactions" not in acc:
        acc["transactions"] = []
    if "balance" not in acc:
        acc["balance"] = 0.0
    if "failed_attempts" not in acc:
        acc["failed_attempts"] = 0
    if "locked" not in acc:
        acc["locked"] = False

def require_account(d, username):
    username = normalize(username)
    if username not in d["accounts"]:
        raise ValueError(f"User '{username}' does not exist.")
    ensure_account_fields(d, username)
    return username

def authenticate_pin(d, username):
    username = require_account(d, username)
    acc = d["accounts"][username]
    if acc.get("locked"):
        raise PermissionError("Account is locked.")
    pin = input("Enter 4-digit PIN: ").strip()
    if not valid_pin_format(pin):
        print("PIN must be 4 digits.")
        return False
    if pin == acc.get("pin"):
        acc["failed_attempts"] = 0
        return True
    else:
        acc["failed_attempts"] = acc.get("failed_attempts", 0) + 1
        if acc["failed_attempts"] >= 3:
            acc["locked"] = True
            raise PermissionError("Account locked after 3 failed attempts.")
        print("Wrong PIN.")
        return False
