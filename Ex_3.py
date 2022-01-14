
#QUESTION 1

# for i in range(1,51):
#     from random import randint
#     x = randint(3,6)
#     print(x)

#QUESTION 2
# from random import randint
# x = randint(1,50)
# print(x)
# y = randint(2,5)
# print(y)
# print(x**y)

#QUESTION 3
# from random import randint
# z = randint(1,10)
# print(z)
# for i in range(z):
#     print('Fiifi')

#QUESTION 4 
# import random
# print(round(random.uniform(1, 10), 2))

# #QUESTION 5
# for i in range(50):
#     from random import randint
#     x = randint(1,2)
#     print(i)

#QUESTION 6
# x = eval(input('Enter a number: '))
# y = eval(input('Enter another number: '))
# a = abs(x-y)
# b = x+y
# print(a/b)

#QUESTION 7
# x = eval(input("Enter an angle between -180 degrees and 180 degrees:"))
# if x>= -180 and x<= 180:
#     y = x%360 + 0
#     print(y)
# else:
#     print("Try again") 

#QUESTION 8

# x = eval(input('Enter number of seconds:'))
# min = x // 60
# sec = x % 60

# if x < 60:
#     print(x, 'number of seconds has no minute and just', sec, 'seconds.')
# elif x == 60:
#     print(x, 'number of seconds is', min, 'minute and has no seconds.')
# else:
#     print(x,'number of seconds is', min, 'minutes and', sec, 'seconds.')


#QUESTION 9
# hrs = eval(input('Enter hour: '))
# ahead = eval(input('Enter hours ahead in the future: '))
# new_hr = (hrs+ahead) % 12

# if new_hr == 0:
#     print('New hour is', 12, "o'clock")
# else:
#     print('New hour is', new_hr, "o'clock")

#QUESTION 10 a
# pwr = eval(input('Enter a power: '))
# num = 2**pwr
# print(num)
# digit = num % 10
# print(digit)

#QUESTION 10 b
# pwr = eval(input('Enter a power: '))
# num = 2**pwr
# print(num)
# digit = num % 100
# print(digit)

#QUESTION 10 c
# pwr = eval(input('Enter a power: '))
# num_digit = eval(input('Enter number of digits: '))
# mod = 10**num_digit
# num = 2**pwr
# print(num)
# digit = num % mod
# print(digit)

#QUESTION 11
# kg = eval(input('Enter weight in kilograms: '))
# kg_pound = kg * 2.20462
# print(round(kg_pound, 1))

# #QUESTION 12
# def fact(n):
#     f = 1
#     for i in range (1,n+1):
#         f = f*i
#         # print(f)
#     return f    
             
# n = eval(input('Enter a number: '))
# result= fact(n)    
# print(n,'factorial is', result)

# QUESTION 13
# from math import *
# n = eval(input('Enter a number: '))
# x = round(cos(n),2)
# y = round(sin(n),2)
# z = round(tan(n),2)
# print('The cosine of', n, 'is', x)
# print('The sine of', n, 'is', y)
# print('The tangent of', n, 'is', z)

# QUESTION 14
# from math import *
# num = eval(input('Enter an angle in degrees: '))
# if num == 0:
#     print('The sine of',num, 'degree is', round(sin(num),2))
# else:
#     print('The sine of',num, 'degrees is', round(sin(num),2))

#QUESTION 15
# from math import *
# for i in range(0,346,15):
#     print(i, round(sin(i),4),round(cos(i),4))

#QUESTION 16 
# Not too sure about this because I am not getting the 
# right outcome
# from math import *
# Y = eval(input('Enter a year in full digits: '))
# C = 19
# f = floor(C/4)
# g = floor((8*C+13)/25)

# m = (15 + C - f - g) % 30
# n = (4 + C - f) % 7
# a = Y % 4
# b = Y % 7
# c = Y % 19
# d = ((19*C) + m) % 30
# e = ((2*a) + (4*b) + (6*d) + n) % 7
# k = int(22 + d + e)
# i = int(d + e - 9)

# if (e == 6 and m == 2) or (e == 6 and m == 5) or (e == 6 and m == 10) or (e == 6 and m == 13) or (e == 6 and m == 16) or (e == 6 and m == 21) or (e == 6 and m == 24) or (e == 6 and m == 39):
#     print('Easter falls one week earlier on April 18 of', Y)

# elif d == 29 and e == 6:
#     print('Easter falls one week earlier on April 19 of', Y)
# else:
#     print('Easter falls on either March', k, 'or April',i, 'of', Y)


# QUESTION 17
x = eval(input('Enter a year: '))
