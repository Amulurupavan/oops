class Test:
    '''test document is created by pavan'''
    a=100
    def m1(self):
        pass

    def m2(self):
        pass


a1=Test()
print(a1.__doc__)
print(a1)
print(id(a1))
print(type(a1))
print(a1.a)