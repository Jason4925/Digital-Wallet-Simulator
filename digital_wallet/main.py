from data.mock_data import data
from features.accounts import create_account, login, change_pin
from features.transactions import deposit, withdraw, transfer
from features.qr_payments import qr_generate, qr_pay
from features.reports import show_transactions, show_balance, report_category_spend, report_monthly_summary, report_top_payees
def user_menu():
    print("""
==== Digital Wallet ====
1. Add Money (Deposit)
2. Withdraw
3. Show Balance
4. Transfer
5. Generate QR
6. Pay via QR
7. Transaction History
8. Change pin
9. Report: Spend by Category
10. Report: Monthly In/Out
11. Report: Top Payees
0. Logout
""")
    

def main_menu():
    print("""
==== Welcome ====
1. Create Account
2. Login
0. Exit
""")

# ----------------- Main loop -----------------

def main():
    d = data
    while True:
        main_menu()
        choice = input("Choose: ")
        if choice == "1":
            create_account(d)
        elif choice == "2":
            user = login(d)
            if not user:
                continue
            while True:
                user_menu()
                ch = input("Select: ")
                if ch == "1": 
                    deposit(d, user)
                elif ch == "2": 
                    withdraw(d, user)
                elif ch == "3": 
                    show_balance(d, user)
                elif ch == "4": 
                    transfer(d, user)
                elif ch == "5": 
                    qr_generate(d, user)
                elif ch == "6": 
                    qr_pay(d, user)
                elif ch == "7": 
                    show_transactions(d, user)
                elif ch == "8": 
                    change_pin(d, user)
                elif ch == "9": 
                    report_category_spend(d, user)
                elif ch == "10": 
                    report_monthly_summary(d, user)
                elif ch == "11": 
                    report_top_payees(d, user)
                elif ch == "0":
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice.")
        elif choice == "0":
            print("Thank You for using Digital Wallet, Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
