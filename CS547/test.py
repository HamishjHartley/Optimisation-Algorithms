import random
import string
import numpy as np

# Parameters
mutation_rate = 0.1  # Fixed higher mutation rate
POP_SIZE = 50

# Ideal target string
ideal = "Welcome to CS547!"

# Fitness function to calculate similarity to the ideal string
def fitness(input: str, ideal: str):
    return sum(abs(ord(ideal[i]) - ord(input[i])) for i in range(len(ideal)))

# Initialize population with random strings
def initialize_population(POP_SIZE: int):
    population = []
    for _ in range(POP_SIZE):
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(ideal)))
        population.append([random_string, 0])
    return population

# Evaluate fitness for each individual in the population
def eval_population(population: list):
    for i in range(len(population)):
        population[i][1] = fitness(population[i][0], ideal)
    return population

# Find and return the best individual in the population
def best(population: list):
    return min(population, key=lambda x: x[1])  # Minimize the fitness value

# Tournament selection to select two parents
def tournament_selection(population: list, k: int = 5):
    selected = random.sample(population, k)
    return min(selected, key=lambda x: x[1])

# One-point crossover to create two new children from two parents
def one_point_crossover(parent_1, parent_2):
    length = len(parent_1[0])
    crossover_point = np.random.randint(1, length)
    child_1 = parent_1[0][:crossover_point] + parent_2[0][crossover_point:]
    child_2 = parent_2[0][:crossover_point] + parent_1[0][crossover_point:]
    return [child_1, 0], [child_2, 0]

# Selection and crossover to create a new population
def select_population(population):
    child_pop = []
    # Select top 50% and add random individuals for diversity
    selected_pop = sorted(population, key=lambda x: x[1])[:POP_SIZE // 2]
    selected_pop += random.sample(population, POP_SIZE - len(selected_pop))
    while len(child_pop) < POP_SIZE:
        parent_a = tournament_selection(selected_pop)
        parent_b = tournament_selection(selected_pop)
        child_a, child_b = one_point_crossover(parent_a, parent_b)
        child_pop.extend([child_a, child_b])
    return child_pop[:POP_SIZE]

# Mutate each individual in the population with the given rate
def mutate(population: list, rate: float):
    mutation_count = 0  # Track number of mutations for debugging
    for individual in population:
        mutated_string = list(individual[0])  # Convert to list for mutability
        for i in range(len(mutated_string)):
            if rate >= random.uniform(0, 1):
                mutated_string[i] = random.choice(string.ascii_letters + string.digits)
                mutation_count += 1
        individual[0] = ''.join(mutated_string)  # Convert back to string
    print(f"Mutations this generation: {mutation_count}")
    return population

# Genetic algorithm to evolve population toward ideal string
def genetic_algorithm():
    pop = initialize_population(POP_SIZE)
    scored_pop = eval_population(pop)
    generation = 0
    best_individual = best(scored_pop)

    # Continue until we find a perfect match (fitness of 0)
    while best_individual[1] > 0 and generation < 50_000:
        generation += 1
        new_pop = select_population(scored_pop)
        mutated_pop = mutate(new_pop, mutation_rate)
        scored_pop = eval_population(mutated_pop)
        
        # Update best individual and print progress
        best_individual = best(scored_pop)
        if generation % 500 == 0 or best_individual[1] == 0:
            print(f"Generation {generation} | Best fitness: {best_individual[1]} | Best individual: {best_individual[0]}")
        
        # Early stopping if the best individual matches the ideal exactly
        if best_individual[1] == 0:
            break

genetic_algorithm()
