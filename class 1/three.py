class Test:
    ''' Test class created by pavan '''

    a = 100   #variable
    name='pavan'
    def m1(self):    #method
        pass

    def m2(self):
        pass


print(Test.__doc__)

t1 = Test()  # t1 is ref variable or object.
print(t1)
print(id(t1))
print(type(t1))
print(Test.__dict__)
print(t1.a)