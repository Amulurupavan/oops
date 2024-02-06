class test:
    a=500
    
    def __init__(self):
        self.b=350
    
    def m1(self):
        self.c=200
    
    
t1=test()
t1.d=400
t1.m1()
print(t1.__dict__)
print(test.__dict__)

