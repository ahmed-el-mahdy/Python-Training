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

def hello():
    print('Howdy!')
    print('Howdy!!!!')
    print('Hello there.')
hello()
hello()
hello()

def hello(name):
    print('Hello, ' + name)
    
hello('alice')
hello('bob')    

len('hello')

spam = print('hello')
None == spam

print('cat', 'dog', 'ice', 'sky', sep=',') 
