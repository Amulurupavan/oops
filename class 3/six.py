class Bank:
    bank_name="state bank of india"
    
    def __init__(self,name,code):
        self.branch_name=name
        self.branch_code=code
       
b1=Bank("karakambadi",517507)

print(b1.__dict__)