import pandas as pd

#총수입, 총지출, 잔액 계산

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

# 등록된 데이터 거래목록에 보여주기 
def transactions_to_dataframe(transactions):
    data = [t.to_dict() for t in transactions]
    return pd.DataFrame(data, 
        columns=["data", "type", "category", "description", "amount"]
    )
    
# 카테고리별 지출 통계
def expense_by_category(transactions):
    """
    지출(type == '지출')만 필터링해서
    카테고리별 합계를 DataFrame으로 반환
    """
    data = [
        {
            "category": t.category,
            "amount": t.amount
        }
        for t in transactions
        if t.ttype == "지출"
    ]

    if not data:
        return pd.DataFrame(columns=["category", "amount"])

    df = pd.DataFrame(data)
    summary = df.groupby("category", as_index=True)["amount"].sum()
    return summary

    # pd.DataFrame  대소문자 오류 조심
    # st.dataframe