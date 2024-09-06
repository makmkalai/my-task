def upper(ref):
    def convert():
        data=ref()
        return data.upper()
    return convert

def split(ref):
    def spt():
        ans=ref()
        return ans.split()
    return spt
@split

@upper
def myfun():
    return "good evening"
print(myfun())

#1.Write a Python program to create a decorator to
#  convert the return value of a function
#  to a specified data type
# def data(ref):
#     def convert():
#         ans=ref()
#         a=float(ans)
#         print("inner fun",type(a))
#         return a
#     return convert
# @data
# def indata():
#     x=6
#     return x
# print(indata())


#2.Write a Python program using a decorator to reverse a string.
# def reverse(ref):
#     def con():
#         ans=ref()
#         a=ans[::-1]
#         return a
#     return con
# @reverse
# def myfun():
#     return "good evening"
# print(myfun())

#3.Python program that uses a decorator to check if a number is prime or not.
# def convert(num1):
#     def prime():
#         num=num1()
#         if num==1:
#             return "not a prime number"
#         elif num>1:
#             for i in range(2,num):
#                 if (num%i) == 0:
#                     return "not a prime number"
#             else:
#                 return "prime number"
#         return num
#     return prime
# @convert
# def giv():
#     x=int(input("enter the number:"))
#     return x
# print(giv())

#4.Create a class decorator that adds a new method log_info to any class it decorates.
# The log_info method should print the class name and a message


#example

# class upper():
#     def __init__(self,ref):
#         self.ref=ref
#     def __call__(self, *args):
#         result=self.ref(*args).upper()
#         return result
# @upper
# def fun(str1,str2):
#     return f"values are:{str1} {str2}"
# print(fun("kalai","divi"))

# class add():
#     def __init__(self,ref):
#         self.ref=ref
#     def __call__(self,no1,no2):
#         result=self.ref(no1,no2)
#         return result
# @add
# def fun(no1,no2):
#     return no1+no2
# print(fun(3,5))
            

            