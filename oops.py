# # class Student:
# #     def __init__(self, name, marks):
# #         self.name=name
# #         self.marks=marks
# #     def avgMark(self):
# #         sum=0
# #         for i in self.marks:
# #             sum+=i
# #         print(sum/len(self.marks))

# # s=Student("Lalit",[10,20,30])
# # print(s.name)
# # s.avgMark()4


# class Account:

#     def __init__(self, accNo, balance):
#         self.__accNo = accNo
#         self.__balance = balance

#     @property
#     def accNo(self):
#         return self.__accNo

#     @property
#     def balance(self):
#         return self.__balance

#     def credit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Credit amount:", amount)
#             print("Total balance:", self.__balance)
#         else:
#             print("Invalid amount")

#     def debit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount <= self.__balance:
#             self.__balance -= amount
#             print("Debit amount:", amount)
#             print("Total balance:", self.__balance)
#         else:
#             print("Insufficient balance")


# a = Account(1001, 5000)

# print("Account No:", a.accNo)
# print("Balance:", a.balance)

# a.credit(500)
# a.debit(250)

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def show(self):
#         print(self.real,"i ",self.img,"j")

#     def __add__(num1,num2):
#         newReal=num1.real+num2.real
#         newImg=num1.img+num2.img
#         return Complex(newReal, newImg)
    
# num1=Complex(2,5)
# num2=Complex(2,5)

# num3=num1+num2
# num3.show()

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return (22/7)*self.radius**2

#     def perimeter(self):
#         return 2*(22/7)*self.radius

# c=Circle(5)
# print(c.area(), c.perimeter())

# class Emp:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def showDetails(self):
#         print("Role",self.role," Dept: ",self.dept," Salary",self.salary)

# class Engineer(Emp):
#     def __init__(self, name, age):
#         super().__init__("Developer","IT",50000)
#         self.name=name
#         self.age=age

# eng=Engineer("Rahul",25)
# eng.showDetails()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, odr2):
        return self.price>odr2.price

order1=Order("Chips",225)
order2=Order("Biscuit",28)
print(order1>order2)