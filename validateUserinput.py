while True:
    print ('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
    
while True:
    print('insert a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        print('Password created successfully')
        break
    print ('Passwords can only must be letters and numbers.')
    