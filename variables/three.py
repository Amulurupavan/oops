class account:
    min_bal=500
    
    def __init__(self):
        pass
    
    def close_bal(self):
        print('insufficient bal')
    
a1=account()
print(a1)
a1.close_bal()
print(account.__dict__)