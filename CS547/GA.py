import random
import string
import secrets
from random import gauss
import numpy as np 

rate = 0.05
POP_SIZE = 50

# Convert ideal to string list so it can be mutable
ideal = "Welcome to CS547!"

def fitness(input:str, ideal:str):
    fitness = 0
    # For each character in input string
    for i,char in enumerate(input):
        # Check distance of char in target string
        distance = ord(ideal[i]) - ord(input[i]) ** 2
        # add distance to accumlative fitness value
        fitness += distance
    # return fitness value
    return fitness

#Initializing random adult population vector
def initalize_population(POP_SIZE:int):
    population = []
    for i in range(POP_SIZE):
        #creating population 
        random_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(17))
        population.append([random_string,0])
    return population

def eval_population(population:list):
    for i in range(len(population)):
        population[i][1] = fitness(population[i][0],ideal)
    return population

# Returns best member of population
def best(population: list):
    # Find the individual with the best fitness
    best_individual = min(population, key=lambda x: abs(fitness(x[0], ideal)))
    return best_individual  # Return the individual and its fitness

def top_50(population:list):
    top_50 = []
    for i in range(int(len(population)/2)):
        top_50.append(best(population))
        # remove old best from array 
        population.pop(population.index(best(population)))
    return population

#One point crossover of two parents to create 2 unique children
def one_point_crossover(vector_1, vector_2):
    length = len(vector_1)
    c = np.random.randint(1, length)
    if c != 1:
        for i in range(c, length):
            vector_1[i] ,vector_2[i] = vector_2[i] ,vector_1[i]
    print(vector_1,vector_2)
    return vector_1, vector_2

# Returns new population after selection and crossover has been applied
def select_population(population):
    child_pop = []
    selected_pop = top_50(population)
    for i in range(0,POP_SIZE-1,2):
        parent_a = selected_pop[random.randint(0,len(selected_pop)-1)] 
        parent_b = selected_pop[random.randint(0,len(selected_pop)-1)]
        child_a , child_b = one_point_crossover(parent_a, parent_b)
        child_pop.append(child_a)
        child_pop.append(child_b)
    return child_pop

# Random mutation
def mutate(population:list, rate:int):
    for individual in population:
        for i in range(len(individual)):
            if rate >= random.uniform(0,1):
                individual[i] = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits))
    return population

#Iterates through fitness assessment, selection and breeding, and population reassembly
def genetic_algorithm():
    pop = initalize_population(POP_SIZE) 
    scored_pop = eval_population(pop)
    i=0
    print("Generation",i)
    while best(scored_pop)[1] < 0:
        i += 1 # Increment by 1
        new_pop = []
        new_pop = select_population(scored_pop)
        mutated_pop = mutate(new_pop,rate)
        pop = mutated_pop
        scored_pop = eval_population(pop)
        print("Generation", i)
        print(best(scored_pop))

genetic_algorithm()
#population = initalize_population(POP_SIZE) 
#one_point_crossover(population[0],population[1])

#genetic_algorithm(population)
#genetic_algorithm(population)

