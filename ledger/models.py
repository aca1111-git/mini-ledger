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