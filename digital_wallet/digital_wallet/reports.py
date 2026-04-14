# digital_wallet/reports.py

import logging
import json
import csv
from datetime import datetime
from decimal import Decimal
from digital_wallet.data_store import data

def show_transactions(user: str):
    acct = data["accounts"].get(user, {})
    txs = acct.get("transactions", [])
    if not txs:
        print("No transactions found.")
        return
    print(f"\n--- Transactions for {user} ---")
    for tx in txs:
        print(f"{tx['timestamp']} | {tx['type']:12} | ₹{tx['amount']:8.2f} | "
              f"Cat: {tx.get('category') or '—':10} | CP: {tx.get('counterparty'):10} | Note: {tx.get('note') or '—'}")

def report_category_spend(user: str):
    rows, headers = report_category_spend_data(user)
    print("\nCategory Spend:")
    for row in rows:
        print(f"{row[0]}: ₹{row[1]}")

def report_monthly_summary(user: str):
    rows, headers = report_monthly_summary_data(user)
    print("\nMonthly Summary:")
    for row in rows:
        print(f"{row[0]}: ₹{row[1]}")

def report_top_payees(user: str):
    rows, headers = report_top_payees_data(user)
    print("\nTop Payees:")
    for row in rows:
        print(f"{row[0]}: ₹{row[1]}")

def report_category_spend_data(user: str):
    acct = data["accounts"].get(user, {})
    spend = {}
    for tx in acct.get("transactions", []):
        if tx["type"]=="transfer_out":
            cat = tx.get("category") or "Others"
            spend[cat] = spend.get(cat, Decimal("0.00")) + Decimal(str(tx["amount"]))
    rows = [[cat, f"{amt:.2f}"] for cat, amt in spend.items()]
    headers = ["Category","TotalSpent"]
    return rows, headers

def report_monthly_summary_data(user: str):
    acct = data["accounts"].get(user, {})
    summary = {}
    for tx in acct.get("transactions", []):
        month = datetime.strptime(tx["timestamp"],"%Y-%m-%d %H:%M:%S").strftime("%Y-%m")
        delta = Decimal(str(tx["amount"])) if tx["type"] in ("deposit","transfer_in") else -Decimal(str(tx["amount"]))
        summary[month] = summary.get(month, Decimal("0.00")) + delta
    rows = [[m, f"{net:.2f}"] for m, net in sorted(summary.items())]
    headers = ["Month","NetAmount"]
    return rows, headers

def report_top_payees_data(user: str):
    acct = data["accounts"].get(user, {})
    payees = {}
    for tx in acct.get("transactions", []):
        if tx["type"]=="transfer_out":
            cp = tx["counterparty"]
            payees[cp] = payees.get(cp, Decimal("0.00")) + Decimal(str(tx["amount"]))
    rows = [[cp, f"{amt:.2f}"] for cp, amt in sorted(payees.items(), key=lambda x:x[1], reverse=True)]
    headers = ["Payee","TotalSent"]
    return rows, headers

def export_report(data_rows: list, headers: list, filepath: str):
    if filepath.lower().endswith(".csv"):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data_rows)
    else:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([dict(zip(headers,row)) for row in data_rows], f, indent=2)
    logging.info("Report exported to %s", filepath)