#CHAPTER FOUR_ IF STATEMENTS

QUESTION 1 work on the negative number
def length():
    len = eval(input('Enter length in centimeters: '))
    inch = round((len / 2.54),2)
    if len < 0:
        print('The entry is invalid.')
    
    else:
        print(len,'centimeters in', inch, 'inches.')

length()

QUESTION 2

def tem():
    temp = eval(input('Enter a temperature: '))
    temp_que = input("What is the unit of the temperature, Celsius or Fahrenheit?: ")
    
    C_temp = (5/9)*(temp-32)
    F_temp = ((9/5)*temp) + 32
    
    if temp_que == "Celsius":
        print(temp, "Celsius is", F_temp, "Fahrenheit.")
    elif temp_que == "Fahrenheit":
        print(temp, "Fahrenheit is", C_temp, "Celsius.")
    else: 
        print("invalid measure of unit")
tem()

QUESTION 3
temp = eval(input("Enter a temperature in Celsius: "))
if temp < (-273.15):
    print("The temperature is invalid because it is below absolute zero.")
elif temp == (-273.15):
        print("The temperature is absolute 0.")
elif -273.15<temp<0:
        print("The temperature is below the freezing point.")
elif temp == 0:
        print("The temperature is at the freezing point.")
elif 0<temp<100:
        print("The temperature is in the normal range.")
elif temp == 100:
        print("The temperature is at the boiling point.")
else:
    print("The temperature is above the boiling point.")

QUESTION 4
credit = eval(input("How many credit hours hava you taken?: "))
if credit <= 23:
    print("The student is a freshman.")
elif 24 < credit < 53:
    print("The student is a sophmore.")
elif 54 <credit<83:
    print("The student is a junior.")
elif credit > 84:
    print("The student is a senior.")

QUESTION 5
from random import randint
num = randint(1,10)
guess = eval(input("Guess a number: "))
if num == guess:
    print("You guessed the number right.")
else: 
    print("The number was ", num, ". Try again.", sep='')

QUESTION 6
item= eval(input("How many items are you buying?: "))
if item < 10:
    print ("The total cost of your items is $", item*12,".", sep='')
elif 10 < item < 99: 
      print ("The total cost of your items is $", item*10,".", sep='')
else:
  print ("The total cost of your items is $", item*7,".", sep='')

QUESTION 7
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num2 == num1 + 0.001:
    print("Close")
elif num1 == num2 + 0.001:
    print("Close")
else:
    print("Not close")

QUESTION 8
year = eval(input("Enter a year: "))
if year% 4 == 0:
    print(year,"is a leap year.")
elif year%100 == 0 and year%400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#QUESTION 9
num = eval(input("Enter a number: "))
print("The divisors of", num, "are:")
for i in range(1,num+1):
    if(num%i == 0):
        print(i)

#QUESTION 10
import math
import random

def x():
    
    
    for i in range(1,11):
        num1 = random.randint(1,11)
        num2= random.randint(1,11)
        ans= num1*num2
        guess = eval(input("Question " + str(i) + ": " + str(num1) + " x " + str(num2)+ " = "))

        if guess == ans:
            print("Right!")
        else:
            print("Wrong. The answer is",ans)
    if i == 10:
        print("You have come to the end of the game. Thank you for playing")
x()


#QUESTION 11
hr = eval(input("Enter hour: "))
suffix = eval(input("am (1) or pm(2)? "))
# def am_pm():
#     if suffix != 1 or suffix != 2:    
#         return suffix          
# am_pm()   
hr_ahead = eval(input("How many hours ahead? "))
new_hr_am = hr + hr_ahead
new_hr_pm = (hr + hr_ahead)%12
if suffix == 1 and new_hr_am <=12:
    print("New hour: ", new_hr_am, "am") 
else:
    print("New hour: ", new_hr_pm, "pm") 
