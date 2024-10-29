import string
import random
from random import shuffle

# Identify test cases which have the highest coverage, 
# i.e which have the most 1s / least 0s. 

# Input text file
with open('C:/Users/theha/Documents/GitHub/Optimisation-Algorithms/CS547/newsmallfaultmatrix.txt') as f: lines = f.readlines()

# Simplifing for 5 inputs
matrix = lines[0:5]

# Constants
random.seed(42) 
pop_size=10
crossover_rate = 0.75
mutation_rate = 0.03

# Processes input into usable state (Comma separated list)
def process_input(input:list):
    for i in range(len(input)):
        # Delimiting string by commas
        length = len(input[i])-1
        input[i] = (input[i][0:length]).split(',')
    return input

#     FUNCTION CalculateAPFD(testSuite, faults):
def fitness(suite:list):
    faults = []
    for test in suite:
        test.pop(0)
        faults.append(test)
#     n = LENGTH(testSuite)  // Number of test cases
    n = len(suite)
#     m = LENGTH(faults)     // Number of faults
    m = len(faults)
#     totalFaultsRevealed = 0
    totalFaultsRevealed = 0
#     sumOfFirstReveals = 0
    sumOfFirstReveals = 0

    max_length = max(len(faults[0]) for sublist in faults)
#     FOR each fault in faults:
    # Determine the maximum number of elements in the sublists
    for i in range(max_length):
        for j,fault in enumerate(faults):
            if i < len(fault):  # Check if the index exists in the sublist
                print("Index:",i)
                print(fault[i])
                if fault[i] =='1':
                    print("Found fault at:", fault[j])
                    Tfi = j # TFi = Index of the first test case in testSuite that reveals fault
                    sumOfFirstReveals += Tfi # sumOfFirstReveals += TFi
                    break
    totalFaultsRevealed = sumOfFirstReveals
    print("Total faults revealed",totalFaultsRevealed)
#     // Calculate APFD using the formula
    APFD = 1 - (totalFaultsRevealed / (n * m) + (1 / (2 * n)))
    print(APFD)
    return APFD

# Generate random configuration of test case ordering
def gen_individual(matrix:list):
    test_set = random.sample(matrix, len(matrix))
    return test_set

# Generates a population of individuals
def gen_population(matrix:list):
    population = []
    for i in range(pop_size):
        individual = gen_individual(matrix)
        population.append([individual,0])
        #print("Individual: ", i, [individual,0])
    return population

def eval_population(population:list):
    for i in range(len(population)):
        population[i][1] = fitness(population[i][0])
        print(population[i][0])
    return population

proc_matrix = process_input(matrix) # Process the input

population = gen_population(proc_matrix) # Generate population from processed input

fitness(population[0][0])
print(population[0][0])


def fittest_individual(population:list):
    best = min(population, key=lambda x: abs(fitness(x[0])))
    return best
    
def find_top_50(population:list):
    top_50 = []
    for i in range(int(len(population)/2)):
        top_50.append(fittest_individual(population))
        # remove old best from array 
        population.pop(population.index(fittest_individual(population)))
    return top_50

# One-point crossover
def crossover(parent1, parent2):
    ind1, _ = parent1
    ind2, _ = parent2
    
    # Choose a random crossover point
    crossover_point = random.randint(1, len(ind1) - 1)
    
    # Generate children by swapping segments at the crossover point
    child1 = ind1[:crossover_point] + ind2[crossover_point:]
    child2 = ind2[:crossover_point] + ind1[crossover_point:]
    
    # Return children with fitness initialized to 0
    return [child1, 0], [child2, 0]

def select_and_generate_new_population(population):
    child_pop = []
    selected_pop = find_top_50(population)
    for i in range(0,pop_size-1,2):
        parent_a = selected_pop[random.randint(0,len(selected_pop)-1)] 
        parent_b = selected_pop[random.randint(0,len(selected_pop)-1)]
        child_a , child_b = crossover(parent_a, parent_b)
        child_pop.append(child_a)
        child_pop.append(child_b)
    return child_pop

def mutate(population):
    for individual in population:
        individual_list = list(individual[0])
        
        for i in range(len(individual_list)):
            if random.uniform(0, 1) < mutation_rate:
                individual_list[i] = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits+ string.whitespace + string.punctuation)
        
        individual[0] = ''.join(individual_list)
    return population

# Main GA loop
def genetic_algorithm():
    pop = gen_population()
    scored_pop = eval_population(pop)
    i = 0
    print("Generation",i)
    print(fittest_individual(scored_pop))
    while fittest_individual(scored_pop)[1] < 0:
        i += 1
        new_pop = []
        new_pop = select_and_generate_new_population(scored_pop)
        mutated_pop = mutate(new_pop)
        pop = mutated_pop
        scored_pop = eval_population(pop)
        print("Generation",i)
        print(fittest_individual(scored_pop))
