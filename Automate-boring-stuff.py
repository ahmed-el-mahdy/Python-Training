# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')   

# name= ''
# while not name :
#     print('Enter your name:')
#     name=input()
# print('How many guestes will you have ?')
# numOfGuests=input()
# if numOfGuests:
#     print('Be sure to have enough room for all your guestes')
#     print('Done')

# print('My name is')
# for i in range (5):
#     print('jimmy five times ('+ str(i)+')')
        
# total = 0                   
# for num in range (101):    # it will cont from the begining and add the num value to total until the num value exced to 100 it will stop
#     total = total + num
# print (total)

# for i in range(0, 10, 2):  # 2 stand for step forward to move the next value into i
#     print(i)                  # it should print 0 2 4 6 8
# for i in range(0, 10, 2):  # 2 stand for step forward to move the next value into i
#     print(i)                  # it should print 0 2 4 6 8

# import random
# for i in range(5):
#     print(random.randint(1, 10)) # Return random integer in range [a, b], including both end points.

# # the same of the above but with better way 
# from random import * # to import everything from random module 
# for i in range(5):
#     print(randint(1,10))

# import sys
# while True:
#     print('Type exit to exit')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

# print('enter a number ^_*')
# spam = input()
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings!')
# for i in range(1, 11):
#     print(i)

# i = 1 
# while i < 11:
#     print(i)
#     i= i + 1

# def hello():
#     print('Howdy!')
#     print('Howdy!!!!')
#     print('Hello there.')
# hello()
# hello()
# hello()

# def hello(name):
#     print('Hello, ' + name) 
# hello('alice')
# hello('bob')    
# len('hello')
# spam = print('hello')
# None == spam
# print('cat', 'dog', 'ice', 'sky', sep=',') 

# def a():
#     print('a() starts')
#     b()
#     d()
#     print('a() returns')   
# def b():
#     print('b() start')
#     c()
#     print('b() returns')
# def c():
#     print('c() strat')
#     print('c() returns') 
# def d():
#     print('d() strat')
#     print('d() returns')
# a()

# def spam():
#     eggs = 31337
# spam()
# print(eggs)

# def spam():
#     eggs = 99 #local scop variable 
#     becon() #calling function becon which the egges=0 but in different local scop and not effect in here
#     print(eggs)
# def becon():
#     ham  = 101 
#     eggs = 0 
# spam()

# def spam():
#     print(eggs) # Here we call the global variable which defined in below code
# eggs=32 # defined as global scope
# spam()
# print(eggs)

# def spam():
#     eggs= 'spam local'
#     print(eggs) # will print the local value of eggs in spam
# def bacon():
#     eggs= 'bacon local'
#     print(eggs) # will print local value of eggs in bacon
#     spam()
#     print(eggs) # will print local value of eggs in bacon
# eggs= 'global'
# bacon()
# print(eggs) # it will print the global value for eggs

# def spam():
#     global eggs # using global definition to mark eggs as a global variable
#     eggs= 'spam'
# eggs = 'global'
# spam() # here by the sorting when we call the spam it will update the eggs value form into the spam fun
# print(eggs)

# def spam(divideBy):
#     try:             # using try method and print error massage instead of program fail and exit
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error Invalid argument.')
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# def spam(divideBy):
#     return 42 / divideBy
# try:                # Another way to use try but it will stop when the below exception
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error Invalid argument.')




































































