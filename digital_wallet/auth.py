# digital_wallet/auth.py

import logging
from decimal import Decimal
from digital_wallet.data_store import data
from digital_wallet.utils import generate_tx_id

PIN_RETRY_LIMIT = 3

def create_account():
    username = input("Enter new username: ").strip()
    if username in data["accounts"]:
        print("Username already exists.")
        return

    pin = input("Set 4-digit PIN: ").strip()
    if not (pin.isdigit() and len(pin) == 4):
        print("PIN must be exactly 4 digits.")
        return

    data["accounts"][username] = {
        "pin": pin,
        "balance": Decimal("0.00"),
        "transactions": [],
        "locked": False,
        "failed_attempts": 0
    }
    logging.info("Account created for %s", username)
    print(f"Account '{username}' created successfully.")

def authenticate():
    username = input("Username: ").strip()
    acct = data["accounts"].get(username)
    if not acct:
        print("User not found.")
        return None
    if acct["locked"]:
        print("Account is locked.")
        return None

    for _ in range(PIN_RETRY_LIMIT):
        pin = input("Enter PIN: ").strip()
        if pin == acct["pin"]:
            acct["failed_attempts"] = 0
            logging.info("User %s logged in", username)
            return username
        acct["failed_attempts"] += 1
        logging.warning("Failed login %s attempt %d", username, acct["failed_attempts"])
        if acct["failed_attempts"] >= PIN_RETRY_LIMIT:
            acct["locked"] = True
            print("Account locked after 3 failed attempts.")
            logging.error("Account %s locked", username)
    else:
        print("Incorrect PIN.")
    return None

def change_pin(user: str):
    new_pin = input("New 4-digit PIN: ").strip()
    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("PIN must be exactly 4 digits.")
        return
    data["accounts"][user]["pin"] = new_pin
    logging.info("PIN changed for %s", user)
    print("PIN updated successfully.")