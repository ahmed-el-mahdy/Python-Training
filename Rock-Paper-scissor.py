# Building a basic game using while condition and import module random and if and elif 
import random, sys
print('Rock, Paper, Scissors Game')
# These varibales keep track of the number of wins, losses, and ties.
wins=0
losses=0
ties=0
while True: # The main game loop.
    print ('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)) # print the previous results
    while True: # the player input loop.
        print('Enter your move: r-ock  p-aper  s-cissors  q-uit')
        playermove=input()
        if playermove == 'q':
            sys.exit() # quit the program.
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break # Break out of the player input loop.
        print ('Type one of r, p, s, or q.')
    # Display what the player chose:
    if playermove == 'r':
        print('Rock versus ...')
    elif playermove == 'p':
        print('Paper versus ...')
    elif playermove == 's':
        print('Scissors versus ...')    
    # Display what the computer chooses
    randomnumber = random.randint(1, 3)
    if randomnumber == 1:
        computermove = 'r'
        print('Rock')
    elif randomnumber == 2 :
        computermove = 'p'
        print('Paper')
    elif randomnumber == 3 :
        computermove = 's'
        print('Scissor')
    # Display and record the win/loss/tie:
    if playermove == computermove:
        print('It is tie!')
        ties = ties + 1
    elif playermove == 'r' and computermove == 's':
        print('You win!')
        wins = wins + 1
    elif playermove == 'p' and computermove == 'r':
        print('You win!')
        wins = wins + 1
    elif playermove == 's' and computermove == 'p':
        print('You win!')
        wins = wins + 1
    elif playermove == 'r' and computermove == 'p':
        print('You lose!')
        losses = + 1
    elif playermove == 'p' and computermove == 's':
        print('You lose!')
        losses = + 1 
    elif playermove == 's' and computermove == 'r':
        print('You lose!')
        losses = + 1