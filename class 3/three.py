class bank:
    '''bank acc is created by Amuluru Pavan'''
    def __init__(self):
        print('constructor method')
    def open_acc(self):
        print('acc opened successfully')
        
    @classmethod
    def m1(cls):
        print('class method - m1')
    
    @staticmethod
    def m2():
        print('static method - m2')
        
        
a1=bank()
a2=bank()

print(a1.__doc__)
a1.open_acc()
a1.m1()
a1.m2()
a2.m1()
a2.m2()