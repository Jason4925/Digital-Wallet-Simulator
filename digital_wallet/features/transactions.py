from utils.helpers import make_txn, require_account, authenticate_pin
from data.mock_data import CATEGORIES

def deposit(d, username):
    username = require_account(d, username)
    amt = float(input("Amount to deposit: "))
    if amt <= 0:
        print("Invalid amount.")
        return
    note = input("Note: ") or "Deposit"
    d["accounts"][username]["balance"] += amt
    d["accounts"][username]["transactions"].append(make_txn("deposit", amt, note, None, "self"))
    print("Deposit successful.")

def withdraw(d, username):
    username = require_account(d, username)
    amt = float(input("Withdraw amount: "))
    acc = d["accounts"][username]
    if acc["balance"] < amt:
        print("Insufficient balance.")
        return
    note = input("Note: ") or "Withdraw"
    acc["balance"] -= amt
    acc["transactions"].append(make_txn("withdraw", amt, note, None, "cash"))
    print("Withdrawal successful.")

def transfer(d, sender):
    sender = require_account(d, sender)
    receiver = input("Receiver username: ").strip().lower()
    if receiver not in d["accounts"]:
        print("Receiver not found.")
        return
    amt = float(input("Amount: "))
    if amt <= 0 or d["accounts"][sender]["balance"] < amt:
        print("Invalid amount or insufficient funds.")
        return
    if not authenticate_pin(d, sender):
        print("PIN verification failed.")
        return
    note = input("Note: ") or "Transfer"
    d["accounts"][sender]["balance"] -= amt
    d["accounts"][receiver]["balance"] += amt
    d["accounts"][sender]["transactions"].append(make_txn("transfer_out", amt, note, None, receiver))
    d["accounts"][receiver]["transactions"].append(make_txn("transfer_in", amt, note, None, sender))
    print("Transfer completed.")
