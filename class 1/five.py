class account:
    acc_bal=50000
    
    
    def open_acc(self):
        print('account opened successfully')
        
    def deposit_money(self):
        print('money deposited successfully')
            
    def withdrawl_amount(self):
        print('insufficient money')
                
    def get_bal(self):
        print('acc_bal')
                    
                    
a1=account()
a1.open_acc()
a1.deposit_money()
a1.withdrawl_amount()
a1.get_bal()
