# QUESTION 1
"""
count = 0
for i in range(1,101):
    m = i**2
    if m%10 == 1:
        count = count +1
        # print(m, end=' ')
print(count)
"""

# QUESTION 2
"""
count1 = 0
count2 = 0
for i in range(1,101):
    m = i**2
    if m%10 == 4:
        count1 = count +1
    elif m%10 ==9:
        count2 = count2 +1
        # print(m, end=' ')
print("Number of squares that end is 4 is", count1)
print("Number of squares that end is 9 is", count2)
"""

# QUESTION 3

"""
import math
from math import log 

num = eval(input('Enter a value of n: '))
for i in range(1,num+1):
    a = i + (1/i)
    b = math.log(num) 
    x = a-b
print(x)
"""

# QUESTION 4
"""
sum = 0
for i in range(1,7):
    if i%2 == 0:
        sum = sum - i 
    else:
        sum = sum + i
    
print(sum)
"""

# QUESTION 5
"""
sum = 0
n = eval(input("Enter a number: "))
for i in range(1,n+1):
    if n%i == 0:
        print(i, end='\n')
        sum = sum + i
print("The sum of the divisors of", n, "is", sum, end=' ')
"""

# QUESTION 6

"""
for i in range(1,10000):
    sum = 0
    for x in range(1,i):
        if (i%x == 0):
            sum = sum + x
    if (sum == i):
        print(i,"is a perfect number")
"""
# QUESTION 7

# QUESTION 8
"""x,y,z=3,5,7
x, y, z = y, z, x
print(x,y,z)"""

# QUESTION 9
# sum1 = 0
# sum2 = 0
# sum3 = 0
"""
for i in range(1,10):
    sum1 = 0
    for x in range(1,i):
        if (i%x == 0):
            sum1 = sum1 + x
    if (sum == i):
        print(i,"is a perfect number")
"""

# QUESTION 10 Not completed
"""
largest = int(input("Enter test score: "))
for i in range(9):
    score = int(input("Enter test score: "))
    if score > largest:
        largest = score
    print('Highest score is', largest)
"""
"""
lowest = eval(input("Enter test score: "))
for i in range(9):
    score = eval(input("Enter test score: "))
    if score < lowest:
        lowest = score
print('Lowest score is', lowest)
"""

"""
import math
sum = 0
for i in range (10):
    score = eval(input("Enter test score: "))
    sum = sum + score
print("The average score is",sum/10)
"""


"""
s= 0
for i in range (10):
    score = eval(input("Enter test score: "))
    if score > 100:
        s=s+ 1
    
# if s > 1:
#     print('Values over 100 has been entered')
# else:
print('A value over 100 has been entered')
"""
# QUESTION 11 Print the factorial of a number
"""
num = eval(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Sorry, the factorial does not exist")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of", num, "is", factorial)
"""

# QUESTION 12
""" Write a program that asks the user to guess a random 
number between 1 and 10. If they guess right, they get 10 
points added to their score, and they lose 1 point for an 
incorrect guess. Give the user five numbers to guess and 
print their score after all the guessing is done."""

"""
from random import randint
count = 0


for i in range(5):
    num = randint(1,10) 
    print(num)
    guess = eval(input("Guess a random number between 1 and 10: "))
           
    if guess == num:
        count = count + 10
    else:
        count = count - 1 
print("Your score is", count)
"""

# QUESTION 13
"""
rite a multiplication game program for kids. The program should 
give the player ten randomly generated multiplication questions 
to do. After each, the program should tell them whether they got 
it right or wrong and what the correct answer is.
"""
"""
from random import randint
count1 = 0
count2 = 0
for i in range(1,11):
    num1 = randint(1,10)
    num2 = randint(1,10)
    ans = num1*num2
    guess = eval(input("Question " + str(i) +": " + str(num1) + "x" + str(num2)+ " = "))
    if (guess == ans):
        print("Right!")
        count1 = count1 +1
    else:
        print("Wrong. The answer is", ans)
        count2 = count2 +1
if i == 10:
    print("You have come to the end of the game.")
if count1 == 0:
    print("You had 0 right answers and", count2, "wrong answers.")
elif count1 == 10:
    print("You had 10 right answers and no wrong answer.")
else:
    print("You had", count1, "right answers and", count2, "wrong answers")

"""

# QUESTION 14 MONTY HALL PROBLEM
"""
import math 
from random import randint
Door1= "Goat"
Door2= "Goat"
Door3= "Goat"
Door4= "Prize"

guess1= eval(input("There are 4 doors numbered 1-4. Choose a door: "))
for i range(1):
    if 
open1=randint(1,4)
print(open1)
guess2 = eval(input("Monty opens door "+ str(open1) + ". Press (5) if you want to keep the same door or \n"
"press (6) if you want to change doors: " ))
if guess2==6:
    guess3= eval(input("Pick a door aside doors, "+ str(open1) + " and " + str(guess1)))
"""