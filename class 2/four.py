class test:
    '''Test is created by Amuluru Pavan'''
    def m1(self):
        pass
    
    @classmethod
    def m2(cls):
        pass
    
    @staticmethod
    def m3():
        pass
    
    
t1=test()
print(test.__dict__)
print(test.__doc__)