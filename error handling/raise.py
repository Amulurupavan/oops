#how to create custom/user defined errors
class InsufficientFundsError(Exception):
    def __init__(self,arg):
        self.msg=arg
        
amount = int(input("Enter amount:"))
if amount >5000:
    raise InsufficientFundsError("Less Balance")
else:
    print("Success")