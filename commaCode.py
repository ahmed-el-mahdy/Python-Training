spam= [ 'apples','bananas','tofu','cats']

def joinList(list):
    joined = ''
    if len(list) == 0:
        return ''
    elif len(list) == 1:
        return list[0]
    else:
        return ', '.join(list[:-1]) + ', and ' + list[-1]

print(joinList(spam))        
print(joinList(['apples', 'bananas']))  # Output: "apples, and bananas"
print(joinList(['apples']))         # Output: "apples"
print(joinList([]))                 # Output: ""

# list[:-1]: Slices the list to include all elements except the last one.
# list[-1]: Refers to the last element of the list.
# ', '.join(list[:-1]): Joins all but the last element with a comma and space.
# Concatenation: Adds "and" before the final element for proper formatting.