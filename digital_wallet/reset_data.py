# reset_data.py
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def reset_data():
    DATA_FILE.write_text(
        json.dumps({"accounts": {}}, indent=2),
        encoding="utf-8"
    )
    print("Data has been reset successfully.")

if __name__ == "__main__":
    reset_data()