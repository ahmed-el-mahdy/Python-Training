import random  # Import the random module to generate random numbers.

numberOfStreaks = 0  # Initialize a counter to track how many experiments contain a streak of 6.

# Perform the experiment 10,000 times
for experimentNumber in range(10000):  
    # Step 1: Generate 100 random coin flips
    flips = []  # Create an empty list to store the results of 100 coin flips.
    for i in range(100):  # Loop 100 times to simulate 100 coin flips.
        if random.randint(0, 1) == 0:  # Generate a random integer (0 or 1).
            flips.append('T')  # Append 'T' (tails) to the list if the random number is 0.
        else:
            flips.append('H')  # Append 'H' (heads) to the list if the random number is 1.

    # Step 2: Check for a streak of 6 consecutive identical flips
    streak = 1  # Initialize a variable to track the length of the current streak.
    for i in range(1, len(flips)):  # Start the loop from the second flip (index 1).
        if flips[i] == flips[i - 1]:  # Check if the current flip is the same as the previous one.
            streak += 1  # If yes, increase the streak counter by 1.
        else:
            streak = 1  # If no, reset the streak counter to 1.

        if streak == 6:  # If a streak of 6 is found:
            numberOfStreaks += 1  # Increment the streak counter for the experiment.
            break  # Exit the loop early since we only care about one streak per experiment.

# Step 3: Calculate and print the percentage of experiments with a streak of 6
print('Chance of streak: %s%%' % (numberOfStreaks / 100))  
# Divide the number of experiments with streaks by 10000 to get a percentage.
# Format the result as a percentage with '%' and print it.
