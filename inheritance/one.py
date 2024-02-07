class Account:
    savings_min_bal=1500
    current_min_bal=1000
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
        
    def open_acc(self):
        print("Account Opened Success Fully")


class savings(Account):
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount-Account.savings_min_bal
        print("savings account money deposited successfully",self.acc_bal)
        
    def get_bal(self):
        print("total savings account balance",self.acc_bal)


class current(Account):
    def deposit(self,amount):
        self.acc_bal=self.acc_bal+amount
        print("current account money deposited successfully",self.acc_bal)
        
    def get_bal(self):
        print("total current accunt balance",self.acc_bal)
        


ob1=savings(101,'pavan',50000)
ob2=current(102,'nani',4500)

ob1.deposit(5200)
ob1.deposit(260)
ob1.get_bal()

ob2.deposit(1500)
ob2.deposit(7564)
ob2.get_bal()