import time, sys
indent = 0 # Initial number of spaces to indent the line
indentIncreasing = True # Boolean to control whether indentation is increasing or decreasing
try:
    while True: # Infinite loop to keep the animation running
        print(' ' * indent, end='') # creates a string of spaces based on the value of indent to move the horizontally
        print('**********') # end='' ensures the next print statement continues on the same line for smooth output.
        time.sleep(0.1) # Pauses the program for 0.1 seconds to create a visible animation effect.
        
        if indentIncreasing:
            indent = indent + 1 
            if indent == 20:
                indentIncreasing = False # Switch direction when it reaches 20 spaces
        else:
            indent = indent - 1 
            if indent == 0:
                indentIncreasing = True # Switch direction when it returns to 0 spaces
except KeyboardInterrupt:
    sys.exit()
    