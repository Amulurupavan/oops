class parent1:
    def m1(self):
        print("parent1 - m1 method")
        
    def m2(self):
        print("parent1 - m2 method")
        
class parent2:
    def m3(self):
        print("parent2 - m3 method")
        
    def m2(self):
        print("parent2 - m2 method")
        
class child(parent1,parent2):
    def m4(self):
        print("child - m4 method")
        
ob=child()
ob.m1()
ob.m2()
ob.m2()
ob.m3()
ob.m4()
ob.m2()