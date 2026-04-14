# digital_wallet/operations.py

import logging
from decimal import Decimal
from digital_wallet.data_store import data
from digital_wallet.utils import generate_tx_id, current_timestamp
from digital_wallet.categories import choose_category

# ---------------------------------
# Core operations (non-interactive)
# ---------------------------------

def deposit_amount(user: str, amt, note: str = "") -> bool:
    """
    Deposit a given amount into user's wallet.
    Amount can be float, int, or Decimal.
    """
    acct = data["accounts"].get(user)
    amt = Decimal(str(amt))
    if not acct or amt <= 0:
        logging.error("Deposit failed: %s ₹%s", user, amt)
        return False

    acct["balance"] += amt
    tx = {
        "id": generate_tx_id(),
        "timestamp": current_timestamp(),
        "type": "deposit",
        "amount": float(amt),
        "note": note,
        "category": None,
        "counterparty": "self"
    }
    acct["transactions"].append(tx)
    logging.info("Deposit: %s ₹%.2f", user, amt)
    return True


def withdraw_amount(user: str, amt, note: str = "") -> bool:
    """
    Withdraw a given amount from user's wallet.
    """
    acct = data["accounts"].get(user)
    amt = Decimal(str(amt))
    if not acct or amt <= 0 or amt > acct["balance"]:
        logging.error("Withdrawal failed: %s ₹%s", user, amt)
        return False

    acct["balance"] -= amt
    tx = {
        "id": generate_tx_id(),
        "timestamp": current_timestamp(),
        "type": "withdraw",
        "amount": float(amt),
        "note": note,
        "category": None,
        "counterparty": "self"
    }
    acct["transactions"].append(tx)
    logging.info("Withdraw: %s ₹%.2f", user, amt)
    return True


def transfer_amount(sender: str, recipient: str, amt, note: str = "", category: str = None) -> bool:
    """
    Transfer amount from sender to recipient.
    Category is optional; if None, user will be prompted.
    """
    s_acct = data["accounts"].get(sender)
    r_acct = data["accounts"].get(recipient)
    amt = Decimal(str(amt))

    if not s_acct or not r_acct:
        logging.error("Transfer failed: invalid accounts %s -> %s", sender, recipient)
        return False

    if sender == recipient:
        logging.error("Transfer failed: sender and recipient are the same: %s", sender)
        return False

    if amt <= 0 or amt > s_acct["balance"]:
        logging.error("Transfer failed: insufficient funds %s ₹%.2f", sender, amt)
        return False

    # Deduct from sender, add to recipient
    s_acct["balance"] -= amt
    r_acct["balance"] += amt

    chosen_cat = category or choose_category()

    # Transaction for sender
    tx_out = {
        "id": generate_tx_id(),
        "timestamp": current_timestamp(),
        "type": "transfer_out",
        "amount": float(amt),
        "note": note,
        "category": chosen_cat,
        "counterparty": recipient
    }

    # Transaction for recipient
    tx_in = tx_out.copy()
    tx_in.update({
        "id": generate_tx_id(),
        "type": "transfer_in",
        "counterparty": sender
    })

    s_acct["transactions"].append(tx_out)
    r_acct["transactions"].append(tx_in)

    logging.info("Transfer: %s -> %s ₹%.2f category=%s", sender, recipient, amt, chosen_cat)
    return True

# -------------------------

def deposit(user: str):
    amt_str = input("Amount to deposit: ").strip()
    try:
        amt = Decimal(amt_str)
    except:
        print("Invalid amount.")
        return
    note = input("Note (optional): ")
    if deposit_amount(user, amt, note):
        print(f"Deposited ₹{amt:.2f}")
    else:
        print("Deposit failed.")

def withdraw(user: str):
    amt_str = input("Amount to withdraw: ").strip()
    try:
        amt = Decimal(amt_str)
    except:
        print("Invalid amount.")
        return
    note = input("Note (optional): ")
    if withdraw_amount(user, amt, note):
        print(f"Withdrew ₹{amt:.2f}")
    else:
        print("Withdrawal failed.")

def transfer(user: str):
    recipient = input("Recipient username: ").strip()
    amt_str = input("Amount to transfer: ").strip()
    try:
        amt = Decimal(amt_str)
    except:
        print("Invalid amount.")
        return
    note = input("Note (optional): ")
    cat = choose_category()
    if transfer_amount(user, recipient, amt, note, cat):
        print("Transfer completed.")
    else:
        print("Transfer failed.")