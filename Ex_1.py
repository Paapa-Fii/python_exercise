# #QUESTION 1
print("**************")
print("**************")
print("**************")
print("**************")

# #QUESTION 2
print("***************")
print("*             *")
print("*             *")
print("***************")

# #QUESTION 3
print('*')
print('**')
print('***')
print('****')

# #QUESTION 4
x = 512 - 282
y = 47.48 + 5
print(x/y)

# #QUESTION 5
num = eval(input("Enter a number: "))
print('The square of ', num, ' is ', num*num, '.', sep='')

# #QUESTION 6
x = eval(input('Enter a number: '))
print(x, 2*x, 3*x, 4*x, 5*x, sep ='---')

 
#QUESTION 8
num1 = eval(input('Enter first number: '))
num2 = eval(input('Enter second number: '))
num3 = eval(input('Enter third number: '))
total = num1+num2+num3
average = total/3
print('The total of the three numbers is', total)
print('The average of the three numbers is', average)

#QUESTION 9
meal_price = eval(input('Enter price of meal: '))
tip_percent = eval(input('Enter percent tip: '))
tip_amt = (tip_percent/100)*meal_price
print('The tip amount is ', tip_amt)
total_bill = meal_price + tip_amt
print('The total bill is ', total_bill)
