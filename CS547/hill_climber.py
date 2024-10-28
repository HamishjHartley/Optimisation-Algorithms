import string
import random

# Constants
random.seed(42) 

# Target string
target= "Welcome to CS547!"

def fitness(input:str):
    fitness = []
    # For each character in input string
    for i,char in enumerate(input):
        # Check distance of char in target string
        val = (ord(target[i]) - ord(input[i])) 
        fitness.append(abs(val))
    fitness = -sum(fitness) 
    # return fitness value
    return fitness

def hill_climb():
    inital = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits+ string.whitespace + string.punctuation) for _ in range(17))

    # Evaluate the initial state. If it is a goal state, return success.
    if fitness(inital) == 0:
        print("# Evaluate the initial state. If it is a goal state, return success.")
    # Make the initial state the current state.
    curr = inital
    i = 0
    # Loop until a solution is found or no operators can be applied:
    while(fitness(curr) < 0):
        print("Iteration", i)
        i += 1
    # Select a new state that has not yet been applied to the current state.
        new = curr.replace(curr[random.randint(0,len(curr)-1)], (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits+ string.whitespace + string.punctuation)))

    # Evaluate the new state.
        print("New state fitness:",str(fitness(new)))
    # If the new state is the goal, return success.
        if fitness(new) == 0:
            print("New state sucess")
            break
            
    # If the new state improves upon the current state, make it the current state and continue.
        if fitness(new) > fitness(curr):
            print("# If the new state improves upon the current state, make it the current state and continue.") 
            curr = new
            continue
        
hill_climb()