myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + 'is my pet.')
    
    
    
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
 # Or we can use a shorter method like below 
 
cat= ['fat', 'gray', 'loud']
size, color, disposition = cat


 