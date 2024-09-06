class granfather:
    def __init__(self,gname):
        self.granfathername=gname
    def dis1(self):
        return f"granfather name is: {self.granfathername}"
    
class father(granfather):
    def __init__(self,gname,fname):
        granfather.__init__(self,gname)
        self.fathername=fname
    def dis2(self):
        return f"father name is: {self.fathername}"
    
class son(father):
    def __init__(self,gname,fname,son):
        father.__init__(self,gname,fname)
        self.son=son
    def dis3(self):
        print(f"son name is: {self.son}")

family=son("mathav","bala","ramu")
print(family.dis1())
print(family.dis2())
family.dis3()


