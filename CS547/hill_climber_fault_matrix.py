import string
import random

# Input text file
with open('C:/Users/theha/OneDrive/Documents/GitHub/Optimisation-Algorithms/CS547/newsmallfaultmatrix.txt') as f: lines = f.readlines()

# Simplifing for 5 inputs
matrix = lines

# Constants
random.seed(250) 
n_iterations = 1000

# Processes input into usable state (Comma separated list)
def process_input(input:list):
    for i in range(len(input)):
        # Delimiting string by commas
        length = len(input[i])-1
        input[i] = (input[i][0:length]).split(',')
    return input

# Calculate Average Percentage of faults detected, determining fitness of solution
def fitness(suite:list):
    faults = []
    for test in suite:
        faults.append(test)
    n = len(suite) # Number of test cases
    m = len(faults) # Number of faults

    totalFaultsRevealed = 0
    sumOfFirstReveals = 0

    max_length = max(len(faults[0]) for sublist in faults)
    # For each fault in faults
    for i in range(max_length):
        for j,fault in enumerate(faults):
            if i < len(fault):  
                if fault[i] =='1':
                    Tfi = j # TFi = Index of the first test case in testSuite that reveals fault
                    sumOfFirstReveals += Tfi # sumOfFirstReveals += TFi
                    break

    totalFaultsRevealed = sumOfFirstReveals
    # Calculate Average Percentage of faults detected 
    APFD = 1 - (totalFaultsRevealed / (n * m) + (1 / (2 * n)))
    return APFD

def hill_climb():
    # Initialize with a random string of the same length as the target
    proc_matrix = process_input(matrix)
    initial = random.sample(proc_matrix, len(proc_matrix))

    # If initial state is a goal state, print success and return
    if fitness(initial) == 1:
        print("Initial state is the goal state:", initial)
        return
    
    # Set the initial state as the current state and initialize variables
    curr = initial

    i = 0
    print("Generation", i)
    # Loop until a solution is found or no new states can improve the score
    for i in range(n_iterations):
        print("Generation", i)
        i += 1

        # Generate a unique new state that hasn't been visited
        new = curr.copy()
        
        #while new in visited_states:
        # Randomly modify ordering of two tests in the current state
        test_1 = random.randint(0, len(curr) - 1)
        test_2 = random.randint(0, len(curr) - 1)
        new[test_1] , new[test_2] = new[test_2] , new[test_1]

        # If the new state is the goal, print success and break
        if fitness(new) == 1:
            print("Success")
            break

        # If the new state improves upon the current state, update the current state
        if fitness(new) > fitness(curr):
            print("Improvement found, updating current state.")
            curr = new

        print("APFD value:",fitness(curr))

hill_climb()