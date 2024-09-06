class addtion:
    def add(self,a,b,c=None):
        if c is not None:
            return a+b+c
        else:
            return a+b
        
re=addtion()
va=re.add(2,3)
va1=re.add(2,3,4)
print(va)
print(va1)

# class addtion:
#     def add(self,a,b):
#             return a+b
        
# re=addtion()
# va=re.add("kalai","selvan")
# va1=re.add(2,3)
# print(va)
# print(va1)



        
#dynamic

# class animal:
#     def speak(self):
#         print("lion")
# class dog(animal):
#     def speak(self):
#         print("park")
# class cat(animal):
#     def speak(self):
#         print("meow")
# dog1=dog()
# dog1.speak()
# cat1=cat()
# cat1.speak()

# class dog():
#     def speak(self):
#         print("park")
# class cat():
#     def speak(self):
#         print("meow")
# dog1=dog()
# cat1=cat()
# def both_animal(animal_name):
#     animal_name.speak() 
# both_animal(cat1)
# both_animal(dog1)



#task:
# 2.Create a ComplexNumber class that overloads the + operator to add two complex numbers.
# Also, overload the * operator to multiply two complex numbers
# class complex_number:
#     def __init__(self,r,i):
#         self.realpart=r
#         self.imaginarypart=i
    # def  __add__(self,new):
    #     # self.fir=firnum
    #     # self.sec=secnum
    #     return f"{self.realpart+new.realpart}+{self.imaginarypart+new.imaginarypart}j"
#     def __mul__(self,new):
#         return f"{self.realpart*new.realpart}+{self.imaginarypart*new.imaginarypart}j"
    
# a=complex_number(5,8)
# b=complex_number(2,2)
# print(a*b)

        


# 3.Create two classes, Dog and RobotDog, each with a method bark. Write a function make_it_bark that accepts an object and calls its bark method. Test this function with instances of both Dog and RobotDog.
# class dog:
#     def bark(self):
#         print("dark")
# class robotdag:
#     def bark(self):
#         print("none")
# d=dog()
# rd=robotdag()
# def make_it_bark(name):
#     name.bark()
# make_it_bark(rd)
# make_it_bark(d)

# name="kalaiselvan" just reverse string..
# print(name[::-1])
