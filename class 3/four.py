class account:
    def open_acc(self):
        print('account opened successfully')
    
    def deposit(self,amount):
        print('amount deposited successfully',amount)
        
    def withdrawl(self):
        print('insufficient balance')
        
    def get_bal(self):
        print('acc balance')
        
a1=account()
a2=account()

a1.deposit(5000)
