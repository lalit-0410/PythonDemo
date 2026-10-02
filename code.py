# emp=[(101,"alice",5000),
#      (102,"allen",5000),
#      (103,"ceta",5000)]
# print(emp)

# searchid=int(input("Enter emp id: "))
# found=False
# for e in emp:
#     getid=e[0]
#     if getid==searchid:
#         print("Employee found!")
#         print("Employee ID:", e[0])
#         print("Employee Name:", e[1])
#         print("Salary:", e[2])
#         found=True 
#         break

# if(not found):
#     print("Not found")


# def calc_gst(price):
#     newPrice=price+price*0.18
#     return newPrice
# print(calc_gst(55))


# num=int(input())
# def evenodd(num):
#     if num%2==0:
#         print("even")
#     # else:
#     #     print("odd")

# evenodd(num)

# str=input()
# def countV(str):
#     count=0
#     for i in str.lower():
        
#         if i in "aeiou":
#             count+=1
#     return count

# print(countV(str))

# import math

# num = int(input("Enter a number: "))

# def isPrime(num):
#     if num < 2:
#         print("Not Prime")
#         return

#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             return

#     print("Prime")

# isPrime(num)


# numbers = list(map(int, input("Enter numbers: ").split()))
# def avgM(numbers):
#     sum=0
#     for i in numbers:
#         sum+=i
#     avg=sum/len(numbers)
#     print(avg)

# avgM(numbers)

# marks = {
# "Math": 95,
# "Physics": 97,
# "Chemistry": 98
# }

# for sub in marks:
#     print(sub,marks[sub])

# newList=[]
# # for i in range(1,11):
# #     if i%2==0:
# #         newList.append(i**3)

# # print(newList)

# newList=[i**3 for i in range(2,11,2)]
# print(newList)

# def sq(x):
#     return x*x
# print(sq(5))

# square=lambda x:x*x
# print(square(2))

# Input data
# celsius_temps = [0, 10, 20, 35, 100]
# listT=list(map(lambda x:(x*9/5)+32,celsius_temps))
# print(listT)
# usernames = ["alex", "johndoe", "sam", "pixel_perfect", "emily", "coder123"]
# list=list(filter(lambda n:len(n)>=6,usernames))
# print(list)

# # Input data
# students = [
#     {"name": "Alice", "grade": 88},
#     {"name": "Bob", "grade": 95},
#     {"name": "Charlie", "grade": 78},
#     {"name": "Diana", "grade": 91}
# ]

# # Write your sorted code here:
# top_students = sorted(students,key=lambda x:x["grade"],reverse=True)

# print(top_students)
# Expected Output: 
# [{'name': 'Bob', 'grade': 95}, {'name': 'Diana', 'grade': 91}, {'name': 'Alice', 'grade': 88}, {'name': 'Charlie', 'grade': 78}]
