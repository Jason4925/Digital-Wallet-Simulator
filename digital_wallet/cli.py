# digital_wallet/cli.py

from decimal import Decimal
from digital_wallet.data_store import data
from digital_wallet.auth import create_account, authenticate, change_pin
from digital_wallet.operations import deposit, withdraw, transfer
from digital_wallet.categories import list_categories, add_category, remove_category, choose_category
from digital_wallet.qr import generate_qr_code_data, pay_via_qr_data
from digital_wallet.reports import report_category_spend, report_monthly_summary, report_top_payees, show_transactions

def main_menu():
    while True:
        print("1. Create Account\n2. Login & Use Wallet\n3. Exit")
        choice = input("Select: ").strip()
        if choice=="1":
            create_account()
        elif choice=="2":
            user = authenticate()
            if user:
                wallet_menu(user)
        elif choice=="3":
            print("Goodbye, Thank You for using!\nDigital Wallet Simulator")
            break
        else:
            print("Invalid option.")

def wallet_menu(user: str):
    while True:
        print(f"""
--- {user}'s Wallet ---
1. Show Balance
2. Deposit
3. Withdraw
4. Transfer
5. Generate QR
6. Pay via QR
7. Show Transactions
8. Report: Category Spend
9. Report: Monthly Summary
10. Report: Top Payees
11. Change PIN
12. List Categories
13. Add Category
14. Remove Category
15. Logout
""")
        choice = input("Select: ").strip()
        if choice=="1":
            bal = data["accounts"][user]["balance"]
            print(f"Balance: ₹{bal:.2f}")
        elif choice=="2":
            deposit(user)
        elif choice=="3":
            withdraw(user)
        elif choice=="4":
            transfer(user)
        elif choice == "5":  # Generate QR
            amt = Decimal(input("Amount: ").strip())
            note = input("Note (optional): ")
            cat = choose_category()
            qr = generate_qr_code_data(user, amt, note, cat)  # user = receiver
            print("QR String:", qr)
        elif choice == "6":  # Pay via QR
            qr_str = input("Paste QR string: ")
            success = pay_via_qr_data(user, qr_str)  # user = payer
            print("Payment successful." if success else "Payment failed.")
        elif choice=="7":
            show_transactions(user)
        elif choice=="8":
            report_category_spend(user)
        elif choice=="9":
            report_monthly_summary(user)
        elif choice=="10":
            report_top_payees(user)
        elif choice=="11":
            change_pin(user)
        elif choice=="12":
            list_categories()
        elif choice=="13":
            add_category()
        elif choice=="14":
            remove_category()
        elif choice=="15":
            print("Logging out.")
            break
        else:
            print("Invalid option.")

def preload_demo():
    from digital_wallet.utils import generate_tx_id, current_timestamp
    from decimal import Decimal
    data["accounts"]["alice"] = {
        "pin": "1234",
        "balance": Decimal("5000.00"),
        "transactions": [{
            "id": generate_tx_id(),
            "timestamp": current_timestamp(),
            "type":"deposit",
            "amount":5000.0,
            "note":"Initial deposit",
            "category":None,
            "counterparty":"self"
        }],
        "locked": False,
        "failed_attempts": 0
    }
    data["accounts"]["bob"] = {
        "pin": "5678",
        "balance": Decimal("3000.00"),
        "transactions": [],
        "locked": False,
        "failed_attempts":0
    }
    print("Demo accounts loaded: alice, bob")