class account:
    min_bal=500
    
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
        
    def open_account(self):
        print('done')
        
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount
        
    def get_bal(self):
        return self.acc_bal-account.min_bal
    
    @classmethod
    def update_min_bal(cls):
        cls.min_bal=1000
        
        
    
a1=account(101,'pavan',5000)
a2=account(102,'nani',6000)
a3=account(103,'gana',7000)

a1.deposit(700)
print(a1.get_bal())
print(a1.__dict__)
print(a1.get_bal())
account.update_min_bal()
print(account.__dict__)