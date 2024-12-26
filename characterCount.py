import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count= {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count) # it should print the output in Virtical view

# Example in Action
# Before Incrementing:
# Let’s say count = {'a': 2} and the next character in the string is 'a'.

# The current value of 'a' is 2.
# count[character] + 1 computes 2 + 1 = 3.
# After Incrementing:
# The dictionary is updated: count['a'] = 3.
# Now, 'a' has been counted 3 times.



