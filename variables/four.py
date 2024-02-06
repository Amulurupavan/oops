class Account:
    min_bal=500
    branch_name='banglore'
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    
    def open_acc(self):
        print("acc opened success fully")
        
        
        
        
a1=Account(101,'pavan',5000)
a2=Account(102,'kiran',5500)
a3=Account(103,'venkat',6000)

'''print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)'''

print(Account.__dict__)