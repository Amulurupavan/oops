class parent:
    def m1(self):
        print("parent class - m1 method")

class child(parent):
    def m2(self):
        print("child class - m2 method")


obj=child()
obj.m1()
obj.m2()