import string
import random

# Target string
target = "Welcome to CS547!"

# Constants
random.seed(42) 
pop_size=50
crossover_rate = 0.75
mutation_rate = 0.03

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

def gen_individual():
    random_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits+ string.whitespace + string.punctuation) for _ in range(17))
    return random_string

def gen_population():
    population = []
    for i in range(pop_size):
        individual = gen_individual()
        population.append([individual,0])
    return population

def eval_population(population:list):
    for i in range(len(population)):
        population[i][1] = fitness(population[i][0])
    return population

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

genetic_algorithm()