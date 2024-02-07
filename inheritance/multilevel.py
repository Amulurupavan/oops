class GP:
    def m1(self):
        print("GP - m1 method") 

class parent(GP):
    def m2(self):
        print("parent - m2 method")

class child(parent):
    def m3(self):
        print("child - m3 method")


obj=child()
obj.m1()
obj.m2()
obj.m3()