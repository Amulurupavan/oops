class account:
    def __init__(self,id,name,balance):
        self.acc_id=id
        self.name=name
        self.acc_bal=balance
        print('Constructor executed automatically')
    def open_acc(self):
        print('account opened successfully')
    
    def deposit(self,amount):
        #print('amount deposited successfully',amount)
        self.acc_bal=self.acc_bal+amount
        
    def withdrawl(self):
        print('insufficient balance')
        
    def get_bal(self):
        #print('acc balance')
        return self.acc_bal
        
        
a1=account(6006,'Pavan',50000)
a2=account(6075,'ganesh',60000)

print(a1.__dict__)
print(a2.__dict__)

a1.deposit(500)
a2.deposit(550)
a2.deposit(320)
print(a1.get_bal())
print(a2.get_bal())

