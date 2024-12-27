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

# # For Loop in range 
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is :' + supplies[i])

# 'howdy' in ['hello', 'hi', 'howdy']

# spam = ['hello', 'hi', 'gas']
# 'cat' in spam

# # Using the random.choice() and random.shuffle() Functions with Lists

# import random
# pets = ['bird','cat','mouse']

# random.choice(pets)

# import random
# people = ['ahmed' ,'ali' ,'zaid' ,'tarek']
# random.shuffle(people)

# spam = 42 
# spam = spam + 1
# #==========
# spam += 1

# # Methods 

# spam = ['asda','asdf','asds','asd']
# spam.index('asda')

# and so on to the reset of the element 

# How to add to the list 

# spam = ['fat','cat','bat']
# spam.append('rabit') # method to add an element to the list 

# # it will be spam = ['fat','cat','bat','rabit']

# # if we need to add element to list in spesific index 
# spam = ['fat','cat','bat']
# spam.insert(1,'rat')

# # We can also remove value from the list using remove module
# spam = ['fat','cat','bat']
# spam.remove('bat')

# # Sorting a list of numbers values upward 
# spam =  [2,3.2,5,1,7,6,9]
# spam.sort()
# # Sorting a list of string values Alphapatical 
# spam = ['mona','fathy','mousa','zain','rami']
# spam.sort()

# # Sorting a list with deffrenet value it will reteurn ---ERROR---
# spma = ['ali','zain','toka',1,2,5,8,3,4,6]
# spam.sort()

# # Sorting a list of numbers values reversed
# spam =  [2,3.2,5,1,7,6,9]
# spam.sort(reverse=True)

name = 'zophie'
name [0] # will show the first element from the name value which will be 'z' 
name [-1] # will show the last element from the name value which will be 'e'

name [0:4] #will show the elements for index 0 to 4   which will be 'zoph' 
# We can use this to check if this value in the elements of the array or not
'zo' in name    # it should reply with True and will be False if the element is not in the array

for i in name:
    print ('***' + i + '***') # it will print every element in a separated line between *** ***

# Tubles is like list but can not changed 

eggs = ('hello', 42)
eggs[0]

# if there is tuples content single element it's required a comma , in the end 
value = ('asd',)

# We can covert list to tuples like the below and we can conver a tuple to list as well
arst= tuple(['cat','dog',5])
list(('cat','dog',5))


# Dictionaries Methods

spam = {'color': 'red', 'age': 42 }
for v in spam.values():
    print(v)
# it'll print all the values in the dictionaries     
    
spam = {'color': 'red', 'age': 42 }
for k in spam.key():
    print(k)
# it'll print all the Keys in the dictionaries   

spam = {'color': 'red', 'age': 42 }
for i in spam.item():
    print(i)
# it'll print all the keys & Values in the dictionaries   


# We can check if an element is sorted in the dictionaries or not 
spam = {'name': 'zozo', 'age': 4}
'name' in spam.keys()   # name here as key
# will print True

'zezo' in spam.values()   # zezo here as values
# will print True

4 in spam.values()   # 4 here as values
# will print True

picnicItems = {'apples': 5, 'cups': 3}
'I am bringing ' + str(picnicItems.get('cups', 0)) + 'cups.'
# That's how we used dictionaries and retrive data from in into output 

spam = { 'name': 'Poika', 'age': 4} # we insert the string value between '' and the init without ''
spam.setdefault('color', 'black')
# we can check if there a key value does exist or not and add it if it does not exist


# Working with Strings

print ("Hello there!\nHow are you?\nI'm doing fine.")

print (''' Dear Alice,
       Eva's cat has been arrested for catnapping, cat burglary, and extortion.
       Sincerely,
       Bob''')

# we can use ''' ''' to print string statment with multi lines with no issue.

# Also we can use it to mark the writen command in multi lines as shown below

"""This is a test Python program.
written by Ahmed Elmahdy a.elmahdy.mail@gmail.com 

This program was desigend for python 3, not python 2.
"""

def spam():
    """ This a multiline comment to help 
    explain what the spam() function does. """
    print ('Hello!')
    
# Working with Strings 

name = 'al'
age = 30

f'My name is {name}. Next year I will be {age+1}.'

""" It will print 'My name is al. Next year I will be 31.' """

spam = 'Hello, World!'
spam = spam.upper()
""" it will print the string in upper case so we used spam = to restore the new value in the spam """    

spam = spam.lower()
""" it will print the string in lower case so we used spam = to restore the new value in the spam """ 

spam.islower()
# will display True 

""" Here we can check if the strings start with specific word """

'Jerrcy now wakel elgaow'.startswith('jerrcy')
""" It will print True and u need to remember it's case sencitive """

# here we can convert list into strings in a nice format by using .join function like the chatgpt example
', '.join(['cats', 'rat','bats'])

# acually we can convert string message into list by using split() function as shown below
'My name is Ahmed'.split()

'This is sentence one. This is sentence two'.split('. ')

listed= '''Dear Ali,
How have you been? I am fine.
There is a container in the fridge
That is labeled "Milk Experiment."

please do not drink it.
sincedrely,
Ahmed '''

listed.split('\n')
