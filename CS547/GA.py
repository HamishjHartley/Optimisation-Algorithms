import random
import string
import secrets
from random import gauss
import numpy as np 

#n_dimensions = 6
n_iterations = 100
POP_SIZE = 10

ideal = "Welcome to CS547!"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !"

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
        random_string = ''.join((alphabet[(random.randint(0,51))]) for i in range(len(ideal)))
        population.append(random_string) 
    print(population)
    return population

#Return fitness value for each member of population in list
def assess_fitness(population:list):
    population_fitness = []
    for i in range(len(population)):
        population_fitness.append(fitness(population[i],ideal))
    best = np.argmin(population_fitness)
    return best

#One point crossover of two parents to create 2 unique children
def one_point_crossover(vector_1, vector_2):
    length = len(vector_1)
    c = np.random.randint(1, length)
    if c != 1:
        for i in range(c, length):
            vector_1[i] ,vector_2[i] = vector_2[i] ,vector_1[i]
    return vector_1, vector_2

#Returns a vector which has been mutated using Guassian convolution
def gauss_mutate(vector):
    p = 1 #probability of adding noise to element in vector
    sigma = 0.005 #variance of Normal distribution to convolve with
    min = -100
    max = 100

    for i in range(1,len(vector)):
        if p >= random.uniform(0,1):
            while True:
                n = random.gauss(0,sigma)#random number chosen from Normal distribution
                if (np.logical_and(n+vector[i]>=min, n+vector[i]<=max) == True): #Comparison between numpy arrays requires logical_or function
                    vector[i]= vector[i] +n
                    break
    return vector

#Iterates through fitness assessment, selection and breeding, and population reassembly
def genetic_algorithm(population:list, n_iterations:int):
    #Loop n_iteration times
    for i in range(n_iterations):
        best = assess_fitness(population) 
        child_pop = []
        for i in range(0,POP_SIZE,2):
            parent_a = population[i] 
            parent_b = population[i+1]

            child_a , child_b = one_point_crossover(parent_a, parent_b)
            
            #Mutate child_a, child_b    
            child_pop.append(gauss_mutate(child_a))
            child_pop.append(gauss_mutate(child_b))
        population += child_pop
    return population[best]

#population = initalize_population(POP_SIZE)
#solution = genetic_algorithm(population,n_iterations)

#print(solution-ideal)


