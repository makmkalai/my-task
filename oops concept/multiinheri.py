# class parent1:
#     def dis1(self):
#         print("this is parent1")

# class parent2:
#     def dis2(self):
#         print("this is parent2")

# class child(parent1,parent2):
#     def dis3(self):
#         print("child")
# ch=child()
# ch.dis1()
# ch.dis2()
# ch.dis3()

class father:
    def __init__(self,fname):
        self.fname=fname
    def dis1(self):
        print (f"father name is: {self.fname},")
class mother:
    def __init__(self,mname):
        self.mname=mname
    def dis2(self):
        print(f"mother name is: {self.mname},")
class son(father,mother):
    def __init__(self, fname,mname,sonname):
        father.__init__(self,fname)
        mother.__init__(self,mname)
        self.sname=sonname
    def dis3(self):
        print(f"son name is: {self.sname}")  #{super().dis2()})
    
ans=son("kalai","divi","muthu")
ans.dis1()
ans.dis2()
ans.dis3()

