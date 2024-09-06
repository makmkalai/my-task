# class stack:
#     def __init__(self):
#         self.stlist=[]
#     def add(self,values):
#         self.stlist.append(values)
#     def remove(self):
#         self.stlist.pop() #pop() last items are remove, list in first out 
#     def display(self):
#         return f"name list are: {self.stlist}"
# result=stack()
# result.add("kali")
# print(result.display())
# result.add("ramu")
# print(result.display())
# result.add("tamil")
# print(result.display())
# result.remove()
# print(result.display())

class queue:
    def __init__(self):
        self.stlist=[]
    def add(self,values):
        self.stlist.append(values)
    def remove(self):
        self.stlist.pop(0)  #pop(0) 0-index remove, first in first out
    def display(self):
        return f"name list are: {self.stlist}"
result=queue()
result.add("kali")
print(result.display())
result.add("ramu")
print(result.display())
result.add("tamil")
print(result.display())
result.remove()
print(result.display())
