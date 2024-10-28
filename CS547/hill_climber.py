import string
import random

# Constants
random.seed(42) 

# Target string
target= "Welcome to CS547!"

def fitness(input_str: str):
    fitness = []
    # For each character in input string
    for i, char in enumerate(input_str):
        # Check distance of char in target string
        val = (ord(target[i]) - ord(input_str[i])) 
        fitness.append(abs(val))
    fitness = -sum(fitness) 
    # Return fitness value
    return fitness

def hill_climb():
    # Initialize with a random string of the same length as the target
    initial = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.whitespace + string.punctuation) for _ in range(len(target)))

    # If initial state is a goal state, print success and return
    if fitness(initial) == 0:
        print("Initial state is the goal state:", initial)
        return
    
    # Set the initial state as the current state and initialize variables
    curr = initial
    visited_states = set([curr])

    i = 0
    # Loop until a solution is found or no new states can improve the score
    while fitness(curr) < 0:
        print("Iteration", i)
        i += 1

        # Generate a unique new state that hasn't been visited
        new = curr
        while new in visited_states:
            # Randomly modify a character in the current state
            pos = random.randint(0, len(curr) - 1)
            new_char = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.whitespace + string.punctuation)
            new = curr[:pos] + new_char + curr[pos + 1:]

        # Add the new state to visited states
        visited_states.add(new)
        
        # Evaluate the new state
        print(new, "Fitness:", fitness(new))

        # If the new state is the goal, print success and break
        if fitness(new) == 0:
            break

        # If the new state improves upon the current state, update the current state
        if fitness(new) > fitness(curr):
            print("Improvement found, updating current state.")
            curr = new

hill_climb()
