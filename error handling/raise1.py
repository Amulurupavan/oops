class InsufficientFundsError(Exception):
    def __init__(self,msg):
        self.m1=msg
        
amount=int(input("Enter amount:"))
if amount > 5000:
    raise InsufficientFundsError("less amount")
else:
    print("Success")