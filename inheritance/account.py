class Account:
    savings_min_bal=500
    current_min_bal=1000
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
        
    def open_acc(self):
        print('acc opened success fully')


class savings(Account):
    def deposit(self,amount):
        self.acc_bal=self.acc_bal-Account.savings_min_bal
        print(self.acc_bal,'savings deposited')

        
    def get_bal(self):
        print('total savings account deposited amount',self.acc_bal)

class current(Account):
    def deposit(self,amount):
        self.acc_bal=self.acc_bal-Account.current_min_bal
        print(self.acc_bal,'deposited amount')
        print('total amount deposited',self.acc_bal)
        
    def get_bal(self):
        print("current account balance",self.acc_bal)
        

obj=Account(100,'gana',4500)
obj1=savings(101,'pavan',5000)
obj2=current(102,'nani',6500)

obj.open_acc()

obj1.deposit(5000)
obj1.deposit(239)
obj1.get_bal()

obj2.deposit(1500)
obj2.deposit(600)
obj2.get_bal()

