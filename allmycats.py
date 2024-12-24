# print('Enter Thme Name of Cat 1:')
# catName1 = input()
# print('Enter Thme Name of Cat 2:')
# catName2 = input()
# print('Enter Thme Name of Cat 3:')
# catName3 = input()
# print('Enter Thme Name of Cat 4:')
# catName4 = input()
# print('Enter Thme Name of Cat 5:')
# catName5 = input()
# print('Enter Thme Name of Cat 6:')
# catName6 = input()

# print('The Cat Names are:')
# print ( catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' '+ catName5 + ' ' + catName6 )

# We can enhance the above basic program with a advanced method using list

catNames = []
while True:
    print('Enter The Name of cat ' + str(len(catNames) + 1) + ' (Or Enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The Cat Names are:')
for name in catNames:
    print('  ' + name)











