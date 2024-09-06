#private methods:
# class Myclass:
#     def __init__(self):
#         self.__var="kalai"
#     def __privatemethod(self):
#         print("this is private methods.")
# obj=Myclass()
# # obj.privatemethod()
# # obj.var
# obj._Myclass__privatemethod()
# print(obj._Myclass__var)


#protected
# class Myclass:
#     def __init__(self):
#         self._var="kalai"
#     def _protectedmethod(self):
#         print("this is protected method")
# obj=Myclass()
# print(obj._var)
# obj._protectedmethod()


# class Car:
#     def __init__(self,name,color):
#         self.name=name
#         self._color=color
#         self.__km=0
#     def start(self):
#         print(f"{self.name} {self._color}")
#     def __updatemil(self,mileage):
#         self.__km += mileage
#     def drive(self,mileage):
#         self.__updatemil(mileage)
#         print(f"milage is: {mileage}")
# car=Car("TATA","RED")
# car.start()
# car.drive(50)
# print(car._color)


# class Bank_account:
#     def __init__(self,name,acno):
#         self.name=name
#         self._acno=acno
#         self.__amount=0
#     def achold(self):
#         print(f"Holder name is: '{self.name}', Account number is: '{self._acno}'")
#     def _deposite(self,add_amount):
#         self.__amount += add_amount
#         print(f"Deposite Amount is: Rs- '{self.__amount}' only")
#     def _withdraw(self,amount):
#         self.__crtamount =self.__amount-amount
#         print(f"Withdraw Amount is: Rs- '-{amount}' only")
#     def __balance(self):
#         print(f"Balance amount is: Rs- '{self.__crtamount}' only")
# bankaccount=Bank_account("kalai",8652349712)
# bankaccount.achold()
# print(f"Holder name: '{bankaccount.name}'")
# print(f"Account number is: '{bankaccount._acno}'")
# bankaccount._deposite(1300)
# bankaccount._withdraw(1100)
# bankaccount._Bank_account__balance()



# class Bank_account:
#     def __init__(self,name,acno):
#         self.name=name
#         self._acno=acno
#         self.__amount=0
#     def achold(self):
#         print(f"Holder name is: '{self.name}', Account number is: '{self._acno}'")
#     def _deposite(self,add_amount):
#         self.__adamount = self.__amount + add_amount
#         print(f"Deposite Amount is: Rs- '{self.__adamount}' only")
#     def _withdraw(self,amount):
#         self.__crtamount =self.__adamount-amount
#         print(f"Withdraw Amount is: Rs- '-{self.__crtamount}' only")
#     def __balance(self):
#         if self.__crtamount==self.__adamount:
#             print(f"Balance amount is: Rs- '{self.__crtamount}' only")
#         else:
#             print(self.__adamount)
# bankaccount=Bank_account("kalai",8652349712)
# bankaccount.achold()
# print(f"Holder name: '{bankaccount.name}'")
# print(f"Account number is: '{bankaccount._acno}'")
# bankaccount._deposite(1300)
# bankaccount._withdraw(1100)
# bankaccount._Bank_account__balance()



# class Bank_account:
#     def __init__(self,name,acno):
#         self.name=name
#         self._acno=acno
#         self.__amount=0
#     def achold(self):
#         print(f"Holder name is: '{self.name}', Account number is: '{self._acno}'")
#     def _deposite(self,add_amount):
#         self.__amount += add_amount
#         print(f"Deposite Amount is: Rs- '{self.__amount}' only")
#     def _withdraw(self,amount):
#         self.__amount =self.__amount-amount
#         print(f"Withdraw Amount is: Rs- '-{amount}' only")
#     def __balance(self):
#         print(f"Balance amount is: Rs- '{self.__amount}' only")
# bankaccount=Bank_account("kalai",8652349712)
# bankaccount.achold()
# print(f"Holder name: '{bankaccount.name}'")
# print(f"Account number is: '{bankaccount._acno}'")
# bankaccount._deposite(1300)
# bankaccount._deposite(700)
# #bankaccount._withdraw(1100)
# bankaccount._Bank_account__balance()


help('moduls')