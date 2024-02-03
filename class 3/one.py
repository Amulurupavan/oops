class account:
    
    def __init__(self):
        print('constructor is special method -it is executed automatically')
        
a1=account()
a2=account()
a3=account()

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)