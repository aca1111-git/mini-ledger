import pandas as pd

def calc_summary(transactions):
    income = 0
    expense = 0

    for t in transactions:
        if t.ttype == "수입":
            income += t.amount
        elif t.ttype == "지출":
            expense += t.amount

    balance = income - expense
    return income, expense, balance

def transactions_to_dataframe(transactions):
    data = [t.to_dict() for t in transactions]
    return pd.Dataframe(data, 
        columns=["data", "type", "category", "description", "amount"]
    )