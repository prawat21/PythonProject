import pytest
from re import A
import sys

# test case start/end with test keyword
# from wsgiref.simple_server import sys_version
# if , if else and if elif expressions:
# age = int(input('Enter your age: '))
# if age>18:
#  print('Eligible for voting')
# elif age==18:
#     print('Try next year')
# else:
#  print('Not eligible for voting')

# Range function
# a = list(range(10))
# print(a)
# aa = list(range(5,20))  #start from 5 inclusive but last 20 is exclusive
# print(aa)
# aaa = list(range(5,20,2)) #start from 5 inclusive but last 20 is exclusive with 2 step
# print(aaa)

# ====================LOOPS====================================================================

# for x in range(10):
# print(2*x)
# print(2*x, end=" ")
# print(2*x, end=",")


# a =['Puneet','Kumar','Rawat']
# for name in a:
#     print(name*2)

# n=5
# while n>=0:
#     print(n)
#     n -= 1

# break & continue statements

# for i in range(10):
#     if i > 6:
#         break
#     print(i)

# for i in range(10):
#     if i == 8:
#         continue
#     print(i)

# ============Strings==============================

# name = "Puneet"
# paragraph = '''This is a multiline String
# paragraph used for
# testing '''

# print(name)
# print(paragraph)

# Python Strings Indexing supports -ve indexing
# fruit = "Apple"
# print(fruit[-1])
# my_char = fruit[2]
# print(my_char)

# s = "abcde"
# t ="fghij"
# q = s + t
# print(q)
# print(s*2)

# A =10, 20, 30 #tuple
# a =[1,2,3,4,5] #List
# print(A)
# print(type(A))
# print(id(A))
# print("Last Index of a tuple A is: ",A[-1])
# print("Last Index of a list a is: ",a[-1])
# a= 0o101
# b=2
# c=a+b
# print(c)

# print(sys_version)
# p = "Puneet"
# q = p
# print(sys.getrefcount(p))

# # dispose a variable
# del p
# print(sys.getrefcount(p))

# a = range(1, 1000)
# #print("The return type of range() is: ")
# print("The return type of range() is: " , type(a))

# Slicing - Access more than one element from a list/tuple
# a =[10,20,30,40,50,60,70,80,90]
# print(a[-1:0:-1])
# print(a[-1:0:-2])
# print(a[-1:0:1])

# convert a list of Integers to a comma separated string
a = [1, 2, 3, 4, 5, 6, 7, 8]
# print("List of Integers: ", a)
# nums = ','.join(str(i) for i in a)
# print("New_String is: " ,numstr)
b = [8, 9, 10]
a.extend(b)
print("Extend Function Example: ", a)
c = ['a', 'b']
# a.append(c)
c.append(a)
print("Append Function Example: ", c)


