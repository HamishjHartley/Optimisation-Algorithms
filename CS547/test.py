import string
import random
random.seed(42)  # initialize and make repeatable
from operator import itemgetter

# The target string as we will be making reference to that.
target = "Welcome to CS547!"
# Population size and other constants - these can be changed.
pop_size = 50
crossover_rate = 0.75
mutation_rate = 0.05

def fitness(input: str):
    # Calculate cumulative fitness based on character distances to target
    return -sum(abs(ord(target[i]) - ord(input[i])) for i in range(len(input)))

def gen_individual():
    random_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(len(target)))
    return random_string

def gen_population():
    return [[gen_individual(), 0] for _ in range(pop_size)]

def eval_population(population: list):
    for individual in population:
        individual[1] = fitness(individual[0])
    return population

def fittest_individual(population: list):
    return max(population, key=lambda x: x[1])

def find_top_50(population: list):
    # Sort population by fitness and return the top 50%
    sorted_population = sorted(population, key=lambda x: x[1], reverse=True)
    return sorted_population[:len(population) // 2]

def crossover(parent1, parent2):
    ind1, _ = parent1
    ind2, _ = parent2
    
    if random.uniform(0, 1) > crossover_rate:
        return [ind1, 0], [ind2, 0]
    
    # Choose a random crossover point
    crossover_point = random.randint(1, len(ind1) - 1)
    
    # Generate children by swapping segments at the crossover point
    child1 = ind1[:crossover_point] + ind2[crossover_point:]
    child2 = ind2[:crossover_point] + ind1[crossover_point:]
    
    return [child1, 0], [child2, 0]

def select_and_generate_new_population(population):
    new_population = []
    selected_pop = find_top_50(population)
    
    while len(new_population) < pop_size:
        parent_a = random.choice(selected_pop)
        parent_b = random.choice(selected_pop)
        
        child_a, child_b = crossover(parent_a, parent_b)
        new_population.extend([child_a, child_b])
        
    return new_population[:pop_size]

def mutate(population):
    for individual in population:
        individual_list = list(individual[0])
        
        for i in range(len(individual_list)):
            if random.uniform(0, 1) < mutation_rate:
                individual_list[i] = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        
        individual[0] = ''.join(individual_list)
    
    return population

# Main GA loop
pop = gen_population()
eval_population(pop)
generation = 0
print("Generation", generation)
print(fittest_individual(pop))

# Continue until target is reached or max generations are reached
while fittest_individual(pop)[1] < 0 and generation < 1000:
    generation += 1
    selected_population = select_and_generate_new_population(pop)
    mutated_population = mutate(selected_population)
    eval_population(mutated_population)
    pop = mutated_population
    
    best_individual = fittest_individual(pop)
    print("Generation", generation)
    print(best_individual)
    
    if best_individual[0] == target:
        print("Target reached!")
        break
