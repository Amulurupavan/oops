class account:
    def open_acc(self):
        print('account opened successfully')

    def deposit(self):
        print('money deposited successfully')

    def withdrawl_amount(self):
        print('insufficient money')

    def get_bal(self):
        print('acc_balance')





a1=account()
print(account.__dict__)
print(a1.__dict__)