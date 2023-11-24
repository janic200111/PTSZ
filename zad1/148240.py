import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
 
def calculate_completion_sum(n, tasks, setup_times, sequence):
    current_time = 0
    completion_sum = 0
    for i in range(n):
        task_index = sequence[i] - 1  
        if i > 0:
            prev_task_index = sequence[i - 1] - 1  
            current_time += setup_times[prev_task_index][task_index]
        ready_time = tasks[task_index][1]
        current_time = max(current_time, ready_time) + tasks[task_index][0]
        completion_sum += current_time
    return completion_sum
 
def select_parents(population, fitness_vals):
    total_fitness = sum(fitness_vals)
    selection_probs = [f/total_fitness for f in fitness_vals]
    return random.choices(population, weights=selection_probs, k=2)
 
def order_crossover(parent1, parent2):
    child = [None] * len(parent1)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child[start:end] = parent1[start:end]
 
    parent2_index = 0
    for i in range(len(child)):
        if child[i] is None:
            while parent2[parent2_index] in child:
                parent2_index += 1
            child[i] = parent2[parent2_index]
    return child
 
def swap_mutation(sequence):
    index1, index2 = random.sample(range(len(sequence)), 2)
    sequence[index1], sequence[index2] = sequence[index2], sequence[index1]
    return sequence
 
 
def create_initial_population(population_size, n):
    return [random.sample(range(1, n + 1), n) for _ in range(population_size)]
 
def genetic_algorithm(n, tasks, setup_times, population_size=100, generations=1000, mutation_rate=0.01):
    population = create_initial_population(population_size, n)
    best_sequence = None
    best_fitness = float('inf')
 
    for _ in range(generations):
        # Calculate fitness for each individual
        fitness_vals = [calculate_completion_sum(n, tasks, setup_times, individual) for individual in population]
 
        # Check for new best
        for i in range(population_size):
            if fitness_vals[i] < best_fitness:
                best_fitness = fitness_vals[i]
                best_sequence = population[i]
 
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_vals)
            child = order_crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = swap_mutation(child)
            new_population.append(child)
 
        population = new_population
 
    return best_fitness, best_sequence
 
def read_input_file(input_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        tasks = [list(map(int, file.readline().split())) for _ in range(n)]
        setup_times = [list(map(int, file.readline().split())) for _ in range(n)]
    return n, tasks, setup_times
 
def write_output_file(output_file, best_fitness, best_sequence):
    with open(output_file, 'w') as file:
        file.write(f"{best_fitness}\n")
        file.write(' '.join(map(str, best_sequence)) + '\n')
 
input_filename = sys.argv[1]
n, tasks, setup_times = read_input_file(input_filename)

population_sizes = list(range(200, 2001, 10000000000000))
generations = list(range(200, 10001, 100000000))
mutation = list(range(8, 11, 10))
v =[]
i=1
v1=[]
bb=best_fitness = float('inf')
bbv=[]
times =[]
for pop in population_sizes:
    for gen in generations:
        for mut in mutation:
            start_time = perf_counter()
            best_completion_sum, best_sequence = genetic_algorithm(n, tasks, setup_times,pop,gen,mut/100)
            elapsed_time = perf_counter() - start_time
            v.append(best_completion_sum)
            print(i, " ",best_completion_sum, " ", elapsed_time)
            if bb>best_completion_sum:
                #print("NEW BEST", pop, gen, mut)
                bb =best_completion_sum
                bbv=[pop,gen,mut]
            #v1.append(i)
            times.append(elapsed_time)
            i+=1

#print(bb,bbv)
#plt.plot(v1, v)
#plt.show()

#plt.plot(v1, times)
#plt.show()
parts = input_filename.split('_')
output_filename = f"out_{parts[1]}_148240_{parts[2]}"

write_output_file(output_filename, best_completion_sum, best_sequence)

print(f"Results written to {output_filename}")
