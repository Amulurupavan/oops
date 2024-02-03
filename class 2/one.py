class account:
    a=100
    
    def open_acc(self):
        pass
    
    
a1=account()
a2=account()
a3=account()

#print objects
print(a1)
print(a2)
print(a3)

#print object address
print(id(a1))
print(id(a2))
print(id(a3))

#print object members
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

#print class members
print(account.__dict__)