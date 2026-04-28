![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)

# 💳 Digital Wallet CLI (UPI-Style)

Digital Wallet Simulator is a fully functional Python command-line application that replicates core features of modern digital payment systems such as UPI wallets. It enables users to securely create accounts with PIN protection, manage balances through deposits and withdrawals, transfer money between users, and perform QR-based payments. The system includes persistent data storage, customizable expense categories, detailed transaction tracking, and financial reports like category-wise spending, monthly summaries, and top payees. Designed with a clean, modular architecture and real-world transaction logic, this project demonstrates strong fundamentals in Python programming, data handling, and system design, making it suitable for learning, experimentation, and portfolio presentation.  

---

## 📌 Features

🔐 Account & Security
- Create wallet accounts with PIN
- Login authentication
- PIN change support
- Account lock after failed attempts (if enabled)

💰 Wallet Operations
- Check balance
- Deposit money
- Withdraw money
- Transfer money between users

📱 QR Code Payments
- Generate QR payment strings
- Pay by scanning (pasting) QR data
- Correct payer → receiver flow (QR creator receives money)

🏷️ Categories
- Default spending categories
- Add custom categories
- Remove categories safely
- Category-based transaction tracking

📊 Reports
- Category-wise spending report
- Monthly transaction summary
- Top payees report
- Export reports to CSV / JSON

💾 Persistence
- Data stored in data.json
- Automatic save on exit
- Optional reset of stored data

🧾 Logging
- All operations are logged
- Log file: wallet.log
- Includes:
    - Transactions
    - Errors
    - QR operations
    - System events

🛡️ Error Handling
- Prevents overdraft
- Validates QR payloads
- Safe category deletion
- Handles invalid input gracefully
- Ensures consistent balances

🧪 Demo Mode
Preloaded demo users:
- alice (PIN: 1234)
- bob (PIN: 5678)

---

## 🗂️ Project Structure

```
digital_wallet/
│
├── run.py                  # Entry point
├── data.json               # Persistent wallet data
├── wallet.log              # All operations are logged
├── reset_data.py           # Reset Stored Data
│
└── digital_wallet/
    ├── __init__.py
    ├── auth.py             # Authentication & PIN logic
    ├── categories.py       # Category management
    ├── cli.py              # Interactive CLI menus
    ├── constants.py        # Default constants
    ├── data_store.py       # In-memory data store
    ├── logger.py           # Logging setup
    ├── operations.py       # Wallet operations
    ├── persistence.py      # Load / save JSON data
    ├── qr.py               # QR payment logic
    ├── reports.py          # Financial reports
    └── utils.py            # Helpers (IDs, timestamps)
```

---

## ⚙️ Requirements
- Python 3.9+
- No external libraries required (standard library only)

---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Jason4925/Digital-Wallet-Simulator.git
cd digital_wallet
```

### 2. Start Interactive Wallet
```bash
python run.py
```

### 3. Run With Demo Accounts
```bash
python run.py --demo-mode
```

### 4. Reset Stored Data
```bash
python reset_data.py
```

---

## 📄 Technical Documentation 
You can read the full technical documentation here: 
[📄 View Technical Document](Digital_Wallet_Technical_Document.pdf)

---

## 🚀 Future Enhancements (Optional Ideas)
- GUI (Tkinter / Web)
- Encrypted data storage
- Real QR image generation
- Multi-currency support
- REST API version
- Mobile app frontend

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 👨‍💻 Author

**Jeetesh Nehete**

Built as a clean, modular, learning-oriented project with real-world payment system logic.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
