# run.py

import sys
import atexit
from decimal import Decimal
from digital_wallet.logger import setup_logging
from digital_wallet.persistence import load_data, save_data, DATA_FILE
from digital_wallet.cli import main_menu, preload_demo
from digital_wallet.operations import deposit_amount, withdraw_amount, transfer_amount
from digital_wallet.reports import report_category_spend_data, report_monthly_summary_data, report_top_payees_data, export_report
from digital_wallet.qr import generate_qr_code_data, pay_via_qr_data
import argparse
import logging

def parse_args():
    p = argparse.ArgumentParser(description="Digital Wallet CLI")
    p.add_argument("--demo-mode", action="store_true")
    return p.parse_args()

def main():
    setup_logging()
    args = parse_args()


    load_data()

    if args.demo_mode:
        preload_demo()

    atexit.register(save_data)
    main_menu()

if __name__=="__main__":
    main()