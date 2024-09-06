#1.Design a Student class with instance methods to set and display student details
#  such as name, roll number, and grade
# class std():
#     def __init__(self,name,rl_num,grade):
#         self.name=name
#         self.roll_num=rl_num
#         self.grade=grade
#     def dis(self):
#         print(f"Your Name is: {self.name}, Roll Number is: {self.roll_num}, Grade is: {self.grade}")
# details=std("kali",21,"A")
# details.dis()
# details=std("Tamil",22,"A+")
# details.dis()
# details=std("kalai",23,"B")
# details.dis()

#2.Design a Python class named Car with instance methods to display car details
#  such as the model and mileage, and simulate driving the car
# class car():
#     def __init__(self,model,mileage,simulate):
#         self.model=model
#         self.mil=mileage
#         self.sim=simulate
#     def display(self):
#         print(f"Model: {self.model}, Mileage: {self.mil}, Simulate: {self.sim}")
# car1=car("BMW-Z4","non","yes")
# car1.display()
# car2=car("AUDI-Q3","1-lit 17km","no")
# car2.display()
# car3=car("RR-Ghost","1-lit 13km","no")
# car3.display()




#2.Write a Python program to create a class representing a Circle.
#  Include methods to calculate its area and perimeter

#@classmethods:

# class circle:
#     pi=3.14
#     @classmethod
#     def cir(clr,r):
#         area=clr.pi*r**2
#         return area
# cirl=circle
# print("Area of Circle is: ",cirl.cir(5))

# class perimeter:
#     pi=3.14
#     @classmethod
#     def perim(clr,r):
#         area_perimeter=2*clr.pi*r      
#         return area_perimeter
# print("Perimeter of a Circle: ",perimeter.perim(5))






#3.Create an Employee class with a class method
#  to count the total number of employees created.

#classmethod
# class emp:
#     name_list=["kali","ramu","tamil","kalai","mohan"]
#     count=len(name_list)
#     @classmethod
#     def total(clr):
#         x=clr.count
#         return x
# det=emp
# print("count the total no of emp: ",det.total())
#Static methods:
#4.Develop a StringUtils class with a static method that reverses a given string.
# class strin:
#     name="kalai"
#     @staticmethod
#     def rever():
#         name_re=strin.name[::-1]       
#         return name_re
# st=strin
# print(st.rever())
# print("Reverse String: ",strin.rever())

        
    