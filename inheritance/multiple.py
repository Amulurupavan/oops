class parent1:
    def m1(self):
        print("parent1 class - m1 method")

class parent2:
    def m2(self):
        print("parent2 class - m2 method")

class child(parent1,parent2):
    def m3(self):
        print("child class - m3 method")



obj=child()
obj.m1()
obj.m2()
obj.m3()
