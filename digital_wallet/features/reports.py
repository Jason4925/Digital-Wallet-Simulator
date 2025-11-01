from utils.helpers import require_account
from collections import defaultdict
from datetime import datetime

# Show balance
def show_balance(d, username):
    username = require_account(d, username)
    print(f"\nCurrent balance: ₹{d['accounts'][username]['balance']:.2f}\n")

# Show all transactions
def show_transactions(d, username):
    username = require_account(d, username)
    txs = d["accounts"][username]["transactions"]
    if not txs:
        print("No transactions found.\n")
        return
    print("\nTransaction History:")
    print("Timestamp           | Type         | Amount  | Counterparty | Category       | Note")
    print("-"*80)
    for t in txs:
        print(f"{t['timestamp']} | {t['type']:<12} | ₹{t['amount']:<7.2f} | {t['counterparty']:<12} | {str(t['category']):<12} | {t['note']}")

# Report: Spend by Category
def report_category_spend(d, username):
    username = require_account(d, username)
    summary = defaultdict(float)
    for t in d["accounts"][username]["transactions"]:
        if t["type"] in ["transfer_out", "qr_out", "withdraw"]:
            summary[t["category"] or "Other"] += t["amount"]
    print("\n Spending by Category:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt:.2f}")
    print()

# Report: Monthly Inflow / Outflow
def report_monthly_summary(d, username):
    username = require_account(d, username)
    monthly = defaultdict(lambda: {"inflow": 0.0, "outflow": 0.0})
    for t in d["accounts"][username]["transactions"]:
        month = datetime.strptime(t["timestamp"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m")
        if t["type"] in ["deposit", "transfer_in", "qr_in"]:
            monthly[month]["inflow"] += t["amount"]
        elif t["type"] in ["withdraw", "transfer_out", "qr_out"]:
            monthly[month]["outflow"] += t["amount"]
    print("\n Monthly Summary (Inflow vs Outflow):")
    print("Month     | Inflow    | Outflow")
    print("-"*35)
    for m, val in monthly.items():
        print(f"{m} | ₹{val['inflow']:<8.2f} | ₹{val['outflow']:<8.2f}")
    print()

# Report: Top Payees
def report_top_payees(d, username):
    username = require_account(d, username)
    counts = defaultdict(lambda: {"count": 0, "total": 0.0})
    for t in d["accounts"][username]["transactions"]:
        if t["type"] in ["transfer_out", "qr_out"]:
            cp = t["counterparty"]
            counts[cp]["count"] += 1
            counts[cp]["total"] += t["amount"]
    top = sorted(counts.items(), key=lambda x: x[1]["total"], reverse=True)
    print("\n Top Payees (Outgoing):")
    print("Payee      | Transactions | Total Amount")
    print("-"*40)
    for cp, val in top:
        print(f"{cp:<10} | {val['count']:<11} | ₹{val['total']:.2f}")
    if not top:
        print("No outgoing transactions yet.")
    print()
