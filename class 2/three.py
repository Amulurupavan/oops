class account:
    acc_bal=50000
    
    
    def deposit_money(self,amount):
        print('amount deposited successfully', amount)
        self.amount=5000
        
a1=account()
a2=account()
a1.deposit_money(500)
print(a1.acc_bal)
print(a1.__dict__)
a2.deposit_money(45000)
print(a2.acc_bal)
print(a2.__dict__)
