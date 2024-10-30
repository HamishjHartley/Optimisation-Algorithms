import string
import random

# Input text file
with open('C:/Users/theha/OneDrive/Documents/GitHub/Optimisation-Algorithms/CS547/newsmallfaultmatrix.txt') as f: lines = f.readlines()

# Simplifing for 5 inputs
matrix = lines

# Constants
random.seed(250) 
n_iterations = 1001

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

# Generate random configuration of test case ordering
def gen_individual(matrix:list):
    test_set = random.sample(matrix, len(matrix))
    return test_set

# Generates a population of individuals
def gen_population(matrix:list, target_number):
    population = []
    for i in range(target_number):
        individual = gen_individual(matrix)
        population.append([individual,0])
        #print("Individual: ", i, [individual,0])
    return population

def eval_population(population:list):
    for i in range(len(population)):
        #print("Iteration:", i)
        population[i][1] = fitness(population[i][0])
        #print("Individual: ",population[i][0])
    return population

def fittest_individual(population:list):
    max_value = max(population, key=lambda x: x[1])
    return max_value

def evaluate_random_solutions(target_number):
    random_solutions = gen_population(matrix,target_number)
    random_solutions = eval_population(random_solutions)
    best = fittest_individual(random_solutions)
    print(best)
    return best

evaluate_random_solutions(10000)