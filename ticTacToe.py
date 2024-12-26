theBoard = {
    'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
    'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
    'low-l': ' ', 'low-m': ' ', 'low-r': ' '
}

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

# List of valid keys
valid_moves = list(theBoard.keys())

turn = 'x'

for i in range(9):  # Up to 9 moves in a game
    printBoard(theBoard)
    print(f"Turn for {turn}.")
    print("Choose your move from the following options:")
    print(", ".join([move for move in valid_moves if theBoard[move] == '']))
    
    move = input("Enter your move: ").strip()
    
    # Validate input
    while move not in valid_moves or theBoard[move] != '':
        print("Invalid move! Choose an available position from:")
        print(", ".join([m for m in valid_moves if theBoard[m] == ''])) 
        # using ", ".join The .join() method takes a list of strings and concatenates them into a single string, with a specified separator between each element. 
        move = input("Enter your move: ").strip() 
        # using .strip() to removes all leading (before the text) and trailing (after the text) spaces.It does not affect spaces within the text
    
    theBoard[move] = turn  # Update the board
    
    # Switch turns
    turn = 'o' if turn == 'x' else 'x'

# Final board display
printBoard(theBoard)
print("Game over!")
