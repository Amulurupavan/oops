class GP:
    def m1(self):
        print("gp - m1 method")

class parent1(GP):
    def m2(self):
        print("parent1 - m2 method")

class parent2(GP):
    def m3(self):
        print("parent2 - m3 method")

class child(parent1,parent2):
    def m4(self):
        print("child - m4 method")



obj=child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
