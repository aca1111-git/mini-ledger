import os
import csv
from ledger.models import Transaction

CSV_PATH = "data/account.csv"

def load_transactions():
    """
    CSV가 있으면 읽어서 Transaction 리스트 반환
    없으면 빈 리스트 반환
    """
    transactions = []

    if not os.path.exists(CSV_PATH):
        return transactions

        with open(CSV_PATH, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
        for row in reader:
            transactions.append(
                Transaction(
                    date=row["date"],
                    ttype=row["type"],
                    category=row["category"],
                    description=row["description"],
                    amount=int(row["amount"]),
                )
            )
        return transactions


def save_transactions(transactions):
    
    # Transaction 리스트를 CSV로 덮어쓰기 저장
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "type", "category", "description", "amount"])

        for t in transactions:
            writer.writerow([
                t.date,
                t.ttype,
                t.category,
                t.description,
                t.amount,
            ])
