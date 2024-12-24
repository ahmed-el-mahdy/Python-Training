# built-in enumerate() function to loop through a list and access both the index and item simultaneously.
supplies = ['pens','staplers','flamethrowers','binders']

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
    
    
#     Purpose of enumerate():

# Simplifies iteration when both the index and the value of a list are needed.
# Eliminates the need to manually track the index using a counter.
# Real-World Application:

# Useful for scenarios where you need both the position and content of elements in a list, such as logging, debugging, or processing items based on their positions.
# Code Efficiency:

# This approach is cleaner and more Pythonic compared to manually iterating with range(len(supplies)).