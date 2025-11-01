from datetime import datetime

# Categories
CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Education", "Health", "Other"]

# Mock database
data = {
    "accounts": {
        "alice": {
            "pin": "1111",
            "balance": 830.0,
            "transactions": [
                {
                    "id": "tx-a1",
                    "timestamp": "2025-09-20 09:30:05",
                    "type": "deposit",
                    "amount": 1000.0,
                    "note": "Initial top-up",
                    "category": None,
                    "counterparty": "self"
                },
                {
                    "id": "tx-a2",
                    "timestamp": "2025-09-20 10:05:12",
                    "type": "transfer_out",
                    "amount": 250.0,
                    "note": "Lunch split",
                    "category": "Food",
                    "counterparty": "bob"
                },
                {
                    "id": "tx-a3",
                    "timestamp": "2025-09-21 18:22:40",
                    "type": "qr_out",
                    "amount": 120.0,
                    "note": "Movie tickets",
                    "category": "Entertainment",
                    "counterparty": "charlie"
                },
                {
                    "id": "tx-a4",
                    "timestamp": "2025-09-22 08:10:01",
                    "type": "withdraw",
                    "amount": 100.0,
                    "note": "Cash",
                    "category": "Other",
                    "counterparty": "cash"
                },
                {
                    "id": "tx-a5",
                    "timestamp": "2025-09-23 12:45:33",
                    "type": "transfer_in",
                    "amount": 300.0,
                    "note": "Project reimbursement",
                    "category": None,
                    "counterparty": "disha"
                }
            ]
        },
        "bob": {
            "pin": "2222",
            "balance": 625.0,
            "transactions": [
                
            ]
        },
        "disha": {
            "pin": "4444",
            "balance": 100.0,
            "transactions": [
                {
                    "id": "tx-d1",
                    "timestamp": "2025-09-19 08:00:00",
                    "type": "deposit",
                    "amount": 200.0,
                    "note": "Initial load",
                    "category": None,
                    "counterparty": "self"
                },
                {
                    "id": "tx-d2",
                    "timestamp": "2025-09-22 20:05:49",
                    "type": "transfer_in",
                    "amount": 200.0,
                    "note": "Gift",
                    "category": None,
                    "counterparty": "bob"
                },
                {
                    "id": "tx-d3",
                    "timestamp": "2025-09-23 12:45:33",
                    "type": "transfer_out",
                    "amount": 300.0,
                    "note": "Project reimbursement",
                    "category": "Bills",
                    "counterparty": "alice"
                }
            ]
        }
    }
}