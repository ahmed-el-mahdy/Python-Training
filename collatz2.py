def collatz(number):
    if number % 2 == 0:  # Check if the number is even
        result = number // 2
        print(result)  # Print the resulting number
        return result  # Return the result for the next iteration
    else:  # If the number is odd
        result = 3 * number + 1
        print(result)  # Print the resulting number
        return result  # Return the result for the next iteration

while True: # Handeling the user input and the error
    try:
        print('Enter a positive integer:')
        number = int(input())  # Get input from the user and convert it to an integer
        if number <= 0:
            print("Please enter a positive integer greater than 0.")
            continue
        break  # Exit the loop if a valid integer is entered
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

while number != 1:  # Continue until the number becomes 1
    number = collatz(number)  # Call collatz() and update the number
