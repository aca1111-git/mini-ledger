import streamlit as st
import pandas as pd

if "transactions" not in st.session_state:
    st.session_state.transactions = []    #초기화 안하면 오류남

st.set_page_config(page_title="나만의 미니 가계부", layout="wide")
st.title("🏙️ 재상이의 가계부")

st.write("첫번째 프로젝트 과제입니다. !")
st.write("5조에 소속된 방재상입니다. !")

# ======================
# F1. 거래 등록
# ======================
class Transaction:
    def __init__(self, date, ttype, category, description, amount):
        self.date = date          # "2025-01-01"
        self.ttype = ttype         # "지출" 또는 "수입"
        self.category = category   # 식비, 교통
        self.description = description   # 사용내용
        self.amount = amount      # int  사용금액
    
    def to_dict(self):
        return {
            "date": self.date,
            "type": self.ttype,
            "category": self.category,
            "description": self.description,
            "amount": self.amount,
        }

# 입력 폼
date = st.date_input("날짜")
ttype = st.selectbox("구분", ["지출", "수입"])
category = st.selectbox("카테고리", ["식비", "교통", "급여", "기타"])
description = st.text_input("내용")
amount = st.number_input("금액", min_value=0, step=1000)



# t1 = Transaction("2025-01-01", "지출", "식비", "점심", 8000)

# date = st.date_input()
# ttype = st.selectbox()
# category = st.selectbox()
# description = st.text_input()
# amount = st.number_input()
# my_trans = Transaction(data1, type1, category1, description1, amount1)


st.button("등록")   # 등록버튼 클릭시 저장. 어디에?
if amount <= 0:
    st.warning("금액은 0보다 커야 합니다.")
else:
    transaction = Transaction(
            date = str(date),
            ttype = ttype,
            category = category,
            description = description,
            amount = int(amount)
    )

st.session_state.transactions.append(transaction)
st.success("거래가 등록되었습니다.")
# (확인용) 현재 등록된 거래 수
st.caption(f"현재 등록된 거래 수: {len(st.session_state.transactions)}")


# ======================
# F2. 거래 목록 조회
# ======================

st.subheader("📑 거래 목록")

transactions = st.session_state.transactions

if not transactions:
    st.info("등록된 거래가 없습니다.")
else:
    data = [t.to_dict() for t in transactions]
    df = pd.DataFrame(data)
    df.columns = ["날짜", "구분", "카테고리", "내용", "금액"]
    st.dataframe(df, use_container_width=True)

# ======================
# F3. 요약 통계
# ======================
st.subheader("📊 요약 통계")

transactions = st.session_state.transactions

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


if not transactions:
    st.info("통계를 표시할 거래가 없습니다.")
else:
    income, expense, balance = calc_summary(transactions)

    col1, col2, col3 = st.columns(3)

    col1.metric("총 수입", f"{income:,} 원")
    col2.metric("총 지출", f"{expense:,} 원")
    col3.metric("잔액", f"{balance:,} 원")

st.write("통계는 calc_summary 함수를 정의해서 활용함 ")

# ======================
# F4. CSV 파일 처리
# ======================

# st.title("대시보드")

df = pd.read_csv("data/account.csv")
# df[df["type"] =="지출"]
# st.dataframe(df)
# st.bar_chart(df)

st.subheader("📑 원본 데이터")
st.dataframe(df, use_container_width=True)
