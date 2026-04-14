from digital_wallet.data_store import data
from digital_wallet.persistence import save_data

def list_categories():
    print("Available Categories:")
    for idx, cat in enumerate(data["categories"], start=1):
        print(f"  {idx}. {cat}")

def choose_category():
    list_categories()
    choice = input("Select category number: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(data["categories"])):
        print(f"Invalid choice; defaulting to '{data['categories'][-1]}'.")
        return data["categories"][-1]
    return data["categories"][int(choice) - 1]

def add_category():
    new_cat = input("New category name: ").strip()
    if not new_cat:
        print("Category name cannot be empty.")
        return
    if new_cat in data["categories"]:
        print(f"'{new_cat}' already exists.")
        return
    data["categories"].append(new_cat)
    save_data()
    print(f"Added category: {new_cat}")

def remove_category():
    from digital_wallet.data_store import data
    from digital_wallet.persistence import save_data

    FALLBACK_CATEGORY = "Others"

    print("Available Categories:")
    for i, cat in enumerate(data["categories"], start=1):
        print(f"{i}. {cat}")

    choice = input("Enter category number to remove: ").strip()

    if not choice.isdigit():
        print("Invalid input.")
        return

    idx = int(choice) - 1

    if idx < 0 or idx >= len(data["categories"]):
        print("Invalid category number.")
        return

    category = data["categories"][idx]

    if category.strip().lower() == FALLBACK_CATEGORY.lower():
        print("'Others' is a fallback category and cannot be removed.")
        return

    removed = data["categories"].pop(idx)
    save_data()
    print(f"Category '{removed}' removed successfully.")