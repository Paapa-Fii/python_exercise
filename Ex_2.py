#QUESTION 1
# for i in range(100):
#     print('Fiifi')

#QUESTION 2
# for i in range(3):
#     print('Fiifi', end='')    
#     print('Fiifi')
    
#QUESTION 3
# for i in range(100):
#     print(i+1, 'Fiifi')

#QUESTION 4
# for i in range(20):
#     num = i+1
#     print(i+1, '---', num*num)

#QUESTION 5
# for i in range(8,90,3):
#     print(i)

#QUESTION 6
# for i in range(100,1,-2):
#     print(i)

#QUESTION 7
# for i in range(10):
#     print('A', end='')
# for i in range(7):
#     print('B', end='')
# for i in range(4):
#     # print('CD', end='')
#     print('C', end='')
#     print('D', end='')
# print('E', end='')
# for i in range(6):
#     print('F', end='')
# print('G')

#QUESTION 8
# name = input('Enter your name: ')
# num = eval(input('Enter the number times you want to print your name: '))
# for i in range(num):
#     print(name)

#QUESTION 9
# for i in range(100):
#     num1 = 1
#     num2 = i+1
#     print(num1,   num2)

#QUESTION 10
# row = int(input('Enter number of rows: '))
# col = int(input('Enter number of columns: '))
# for i in range(row):
#     for j in range(col):
#         print('*', end=' ')
#     print()

#QUESTION 11 not too sure with the answer. I copied the answer from the internet yet I didnt get the codes right
# high = eval(input('Enter how high you want the box to be: '))
# wide = eval(input('Enter how wide you want the box to be: '))
# for i in range(high):
#     print('*' + ('*' if i in (0,wide-1) else ' ') * (high-2) + '*')


# col=eval(input('Enter how high you want the box: '))
# row=eval(input('Enter how wide you want the box: '))

# for i in range (5):
#     for j in range(7):
#         if (j==0 or j==4)  or (i==0 or i==6):
#             print('*', end='')
#         else:
#             print(end=' ')
#     print()

#This is the answer I came up with for question 11
# x=eval(input('Enter the length of the box: '))
# y=eval(input('Enter the width of the box: '))


# for i in range (x):
#     for j in range(y):
#         if (j==0 or j==y-1)  or (i==0 or i==x-1):
#             print('*', end='')
#         else:
#             print(end=' ')
#     print()

#I realized that the width takes the shorter side and the length takes the longer side. You may want to look at this for me.
   
#QUESTION 12
# x = eval(input('Enter how high you want the triangle: '))
# for i in range(x):
#     for j in range(i+1):
#         print('*', end='')
#     print()

#QUESTION 13
# x = eval(input('Enter how high you want the triangle: '))
# for i in range(x):
#     for j in range(i,x):
#         print('*', end='  ')
#     print()

#QUESTION 14

# h = eval(input("Enter diamond's height: "))
# for x in range(h):
#     print(" " * (h - x), "*" * (2*x + 1))
# 
#    
# for i in range(x - 2, -1, -1):
#     print(" " * (x - i), "*" * (2*i + 1))
 

# #QUESTION 15
x = 7
for i in range(x):
    for j in range(i,x):
        print('', end='')
    print()
for i in range(x):
    for j in range(i):
        print('*', end='')
    print()