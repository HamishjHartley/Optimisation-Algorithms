import random
import string
import secrets
from random import gauss
import numpy as np 

#n_dimensions = 6
n_iterations = 100
rate = 0.05
POP_SIZE = 50

# Convert ideal to string list so it can be mutable
ideal = "Welcome to CS547!"

def fitness(input:str, ideal:str):
    fitness = 0
    # For each character in input string
    for i,char in enumerate(input):
        # Check distance of char in target string
        distance = ord(ideal[i]) - ord(input[i])
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
        population.append([random_string,fitness(random_string,ideal)])
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
    print(top_50)
    return population

population = initalize_population(10)
top_50(population)

#One point crossover of two parents to create 2 unique children
def one_point_crossover(vector_1, vector_2):
    length = len(vector_1)
    c = np.random.randint(1, length)
    if c != 1:
        for i in range(c, length):
            vector_1[i] ,vector_2[i] = vector_2[i] ,vector_1[i]
    return vector_1, vector_2

# Random mutation
def mutate(vector:list, rate:int):
    for i in range(len(vector)):
        if rate >= random.uniform(0,1):
            vector[i] = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits))
    return vector

#Iterates through fitness assessment, selection and breeding, and population reassembly
def genetic_algorithm(population:list, n_iterations:int):
    #Loop n_iteration times
    for i in range(n_iterations):
        print("Iteration", i)
        best = best(population) 
        child_pop = []
        for i in range(0,POP_SIZE-1,2):
            parent_a = population[i] 
            parent_b = population[i+1]

            child_a , child_b = one_point_crossover(parent_a, parent_b)

            #Mutate child_a, child_b    
            child_pop.append(mutate(child_a,rate))
            child_pop.append(mutate(child_b,rate))
        population += child_pop
        
    return population[best]

#population = initalize_population(POP_SIZE)
#solution = genetic_algorithm(population,n_iterations)

#print(solution)
