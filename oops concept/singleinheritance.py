# class company:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def dis(self):
#         return f"{self.name} {self.id}"
# class emp(company):
#     def __init__(self, name, id,salary,post):
#         super().__init__(name, id)
#         self.salary=salary
#         self.post=post
#     def dis1(self):
#         return f"{super().dis()} {self.salary} {self.post}"
# emp1=emp("kali",12,12000,"trainee")
# print(emp1.dis1())




# task:
# 1.Explain the concept of single inheritance using the provided Python example.
# Describe how the classes Animal and Dog are structured,
# and how the speak() method is utilized in both classes.
# Discuss the behavior of calling my_animal.speak() and my_dog.speak()

# class animal:
#     def __init__(self,aname):
#         self.aniname=aname
#     def anidis(self):
#         return f"animal is: '{self.aniname}'"
# class animalspeak(animal):
#     def __init__(self, aname,sp):
#         super().__init__(aname)
#         self.sp=sp
#     def anispeak(self):
#         return f"{super().anidis()}, speak: '{self.sp}'"
# my_animal=animalspeak("Lion","grunt")
# print(my_animal.anispeak())

# class dog:
#     def __init__(self,dname):
#         self.dgname=dname
#     def dgdis(self):
#         return f"dog name is: '{self.dgname}'"
# class dogspeak(dog):
#     def __init__(self, dname,sp):
#         super().__init__(dname)
#         self.sp=sp
#     def dgspeak(self):
#         return f"{super().dgdis()}, speak: '{self.sp}'"
# my_dog=dogspeak("loki","bark")
# print(my_dog.dgspeak())

#2.Extend the provided Python program to include another child class called Cat,
#  inheriting from the Animal class.
#  Implement the speak() method in the Cat class so that it returns the string
#  "{name} says Meow!".
#  Create an instance of the Cat class and call its speak() method.
#  Describe the output

# class animal:
#     def __init__(self,aname):
#         self.aniname=aname
#     def anidis(self):
#         return f"animal is: '{self.aniname}'"
# class cat(animal):
#     def __init__(self, aname,sp):
#         super().__init__(aname)
#         self.sp=sp
#     def speak(self):
#         return f"{super().anidis()}, '{self.sp}' say: Meow!"
# cat_speak=cat("Lion","Cat")
# print(cat_speak.speak())

# 1.Multiple inheritance:
# Create three classes: Person, Employee, and Manager.
# Person should have attributes name and age.
# Employee should inherit from Person and add an attribute emp_id.
# Manager should inherit from both Employee and Person and add an attribute department.

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def person_det(self):
#         return f"person name is: '{self.name}', \nperson age: '{self.age}'"
# class employee(person):
#     def __init__(self, name, age,id):
#         super().__init__(name, age)
#         self.emp_id=id
#     def emp_det(self):
#         return f"{super().person_det()}, \nemployee id: '{self.emp_id}'"
# class manager(employee):
#     def __init__(self, name, age, id,dept):
#         super().__init__(name, age, id)
#         self.dept=dept
#     def manager_det(self):
#         return f"{super().emp_det()}, \ndepartment is: '{self.dept}'."
# company=manager("kalai",24,201,"computer")
# print(company.manager_det())

# 2.Multilevel inheritance:
# Implement three classes: Shape, Rectangle, and Square.
# Shape should have methods set_color() and display().
# Rectangle should inherit from Shape and add methods set_dimensions() and calculate_area(). 
# Square should inherit from Rectangle and override set_dimensions()
# to ensure that both length and width are the same

class shape:
    def __init__(self,clr):
        self.clr=clr        
    def display(self):
        return f"color is: '{self.clr}'"
class rectangle(shape):
    def __init__(self, clr,length,width):
        super().__init__(clr)
        self.length=length
        self.width=width
    def calculate_area(self):
        return f"{super().display()}, \nrectangle area is: '{self.length*self.width}'"
class square(rectangle):
    def __init__(self,clr,length,width):
        super().__init__(clr,length,width)
        self.length1=length
        self.width1=width
        self.cal=(self.length1*self.width1)**2
    def ans(self):
        return f"{super().calculate_area()}, \nsquare area is: '{self.cal}'."
calculate=square("red",2,2)
print(calculate.ans())

