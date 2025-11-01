from utils.helpers import valid_pin_format, require_account, authenticate_pin, ensure_account_fields

def create_account(d):
    name = input("Choose a username: ").strip().lower()
    if not name:
        print("Username cannot be empty.")
        return
    if name in d["accounts"]:
        print("Username already exists.")
        return
    pin = input("Set 4-digit PIN: ").strip()
    if not valid_pin_format(pin):
        print("PIN must be exactly 4 digits.")
        return
    confirm = input("Confirm PIN: ").strip()
    if confirm != pin:
        print("PINs don’t match.")
        return
    d["accounts"][name] = {"pin": pin, "balance": 0.0, "transactions": []}
    print(f"Account '{name}' created successfully!")

def login(d):
    name = input("Username: ").strip().lower()
    if name not in d["accounts"]:
        print("User not found.")
        return None
    ensure_account_fields(d, name)
    acc = d["accounts"][name]
    for _ in range(3):
        pin = input("Enter PIN: ").strip()
        if pin == acc["pin"]:
            print("Login successful.")
            return name
        print("Wrong PIN.")
    print("Too many attempts.")
    return None

def change_pin(d, username):
    try:
        username = require_account(d, username)
    except Exception as e:
        print(e); return
    if not authenticate_pin(d, username):
        print("PIN verification failed.")
        return
    new_pin = input("Enter new 4-digit PIN: ").strip()
    if not valid_pin_format(new_pin):
        print("PIN must be 4 digits.")
        return
    d["accounts"][username]["pin"] = new_pin
    print("PIN changed successfully.")
