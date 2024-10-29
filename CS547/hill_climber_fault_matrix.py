import string
import random

# Input text file
with open('C:/Users/theha/Documents/GitHub/Optimisation-Algorithms/CS547/newsmallfaultmatrix.txt') as f: lines = f.readlines()

# Simplifing for 5 inputs
matrix = lines[0:5]

# Constants
random.seed(42) 

# Calculate Average Percentage of faults detected
def fitness(suite: list):
    n = len(suite)  # Number of test cases
    m = len(suite[0])  # Number of faults (assuming uniform length for all)

    totalFaultsRevealed = 0
    sumOfFirstReveals = 0

    # For each fault in faults
    for i in range(m):
        for j, fault in enumerate(suite):
            if fault[i] == '1':
                Tfi = j  # Index of the first test case that reveals fault
                sumOfFirstReveals += Tfi
                break

    totalFaultsRevealed = sumOfFirstReveals
    # Calculate Average Percentage of faults detected
    APFD = 1 - (totalFaultsRevealed / (n * m) + (1 / (2 * n)))
    return APFD

def hill_climb():
    # Initialize with the matrix
    initial = matrix

    # If initial state is a goal state, print success and return
    if fitness(initial) == 0:
        print("Initial state is the goal state:", initial)
        return

    # Set the initial state as the current state and initialize variables
    curr = initial
    visited_states = set()
    visited_states.add(tuple(map(tuple, curr)))  # Add the initial state to visited states

    i = 0
    # Loop until a solution is found or no new states can improve the score
    while fitness(curr) < 1:
        print("Iteration", i)
        i += 1

        found_unique_state = False
        attempts = 0

        # Generate unique new state that hasn't been visited
        while not found_unique_state and attempts < 100:  # Limit attempts to avoid infinite loops
            new = [row[:] for row in curr]  # Deep copy of the current state
            
            # Swap two random rows (test cases) in the new state
            pos_1 = random.randint(0, len(curr) - 1)
            pos_2 = random.randint(0, len(curr) - 1)
            new[pos_1], new[pos_2] = new[pos_2], new[pos_1]

            # Check if the new state is unique
            if tuple(map(tuple, new)) not in visited_states:
                visited_states.add(tuple(map(tuple, new)))  # Add the new state as a tuple to visited states
                found_unique_state = True
            
            attempts += 1

        # Evaluate the new state if it's unique
        if found_unique_state:
            print(new)
            print("New State:", new, "Fitness:", fitness(new))

            # If the new state is the goal, print success and break
            if fitness(new) == 1:
                print("Found goal state:", new)
                break

            # If the new state improves upon the current state, update the current state
            if fitness(new) > fitness(curr):
                print("Improvement found, updating current state.")
                curr = new
        else:
            print("No unique state found after 100 attempts. Stopping.")

hill_climb()