## Project Overview
This project simulates a modern digital payment system similar to UPI (Unified Payments Interface) platforms.

It provides account management, secure transactions, QR-based payments, transaction tracking, and expense analytics, all implemented using pure Python and mock in-memory data (no external databases).

The goal is to help understand digital payment concepts and Python programming through a working, console-based simulation.



## Project Folder Structure
digital_wallet/
│
├── main.py                         # Main application entry point
│
├── data/
│   └── mock_data.py                 # Initial mock users and transaction data
│
├── utils/
│   └── helpers.py                   # Common helper functions (PIN check, timestamp, etc.)
│
└── features/
    ├── accounts.py                  # Account creation, login, PIN change
    ├── transactions.py              # Deposit, withdraw, transfer
    ├── qr_payments.py               # QR code payment generation and processing
    └── reports.py                   # Transaction history and expense reports


## Features
1. Account Management: Create accounts, login, change 4-digit PIN
2. Transactions: Deposit, withdraw, transfer money to other users
3. QR Payments: Generate and pay using QR payloads
4. Transaction History: View all transactions with details
5. Expense Categorization: Tag and track spending by category
6. Reports:
        Spending by category
        Monthly inflow/outflow
        Top payees ranking
7. Security: PIN authentication with 3-attempt lockout



## Requirements
- Python 3.8+
- No external dependencies (standard library only)

## Run
In VS Code terminal :- `python main.py`

## Note:-
- All data is mock and in-memory only (lost when the program exits).
- Uses Python standard libraries only (json, datetime, time, collections).
- Fully modular design for accounts, transactions, QR payments, and reports.

## Developed By

Jeetesh Nehete
