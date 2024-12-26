allGuests = { 'alice': { 'apples': 5, 'pretzels': 12},
             'bob': {'ham sandwiches': 3, 'apples':2},
             'carol': {'cups': 3, 'apple pies':1}}

def totalbrought(guests, item):
    numbrought = 0
    for k, v in guests.items():
        numbrought = numbrought + v.get(item, 0)
    return numbrought
    
print ('Number of things being brought:')
print (' - apples         ' + str(totalbrought(allGuests, 'apples')))
print (' - cups           ' + str(totalbrought(allGuests, 'cups')))
print (' - cakes          ' + str(totalbrought(allGuests, 'cakes')))
print (' - ham sandwiches ' + str(totalbrought(allGuests, 'ham sandwiches')))
print (' - apple pies     ' + str(totalbrought(allGuests, 'apple pies')))









