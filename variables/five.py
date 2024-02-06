class Account:
    min_bal=500
    
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    
    def open_acc(self):
        print("acc opened success fully")
        
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount
        
    def get_bal(self):
        return self.acc_bal    
        
a1=Account(101,'pavan',5000)
a2=Account(102,'kiran',5500)
a3=Account(103,'venkat',6000)

a1.deposit(500)
a2.deposit(300)
a3.deposit(100)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

print(a1.get_bal())
print(a2.get_bal())
print(a3.get_bal())



