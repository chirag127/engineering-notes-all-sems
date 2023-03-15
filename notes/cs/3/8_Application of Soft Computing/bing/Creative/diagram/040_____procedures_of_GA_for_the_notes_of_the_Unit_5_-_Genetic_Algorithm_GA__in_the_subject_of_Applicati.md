### Procedures of GA

Genetic Algorithm (GA) is a search-based optimization technique that mimics the process of natural evolution. GA can be used to find optimal or near-optimal solutions for complex problems that are otherwise hard to solve by conventional methods. GA follows the following steps to generate and improve solutions  :

- **Initialization**: GA starts by generating a set of individuals, which is called population. Each individual is a possible solution for the given problem. An individual is characterized by a set of parameters, which are called genes. Genes are usually encoded as binary strings, but other representations are also possible.
- **Evaluation**: GA evaluates the fitness of each individual in the population using a predefined fitness function. The fitness function measures how well an individual solves the problem. The higher the fitness, the better the solution.
- **Selection**: GA selects a subset of individuals from the current population to produce the next generation. The selection process is based on the principle of survival of the fittest, which means that individuals with higher fitness have a higher chance of being selected. There are different methods of selection, such as roulette wheel, tournament, rank-based, etc.
- **Crossover**: GA performs crossover on the selected individuals to create new offspring. Crossover is a process of combining genes from two parents to generate new children. Crossover aims to explore new regions of the search space and exploit the good features of the parents. There are different types of crossover, such as one-point, two-point, uniform, etc.
- **Mutation**: GA performs mutation on some of the offspring to introduce random changes in their genes. Mutation is a process of flipping, swapping, inserting, or deleting some bits in a binary string. Mutation aims to prevent premature convergence and maintain diversity in the population. There are different types of mutation, such as bit-flip, swap, insert, etc.
- **Replacement**: GA replaces the old population with the new offspring to form the next generation. The replacement process can be either generational or steady-state. In generational replacement, the entire population is replaced by the offspring. In steady-state replacement, only a fraction of the population is replaced by the offspring.
- **Termination**: GA repeats the steps of evaluation, selection, crossover, mutation, and replacement until a termination criterion is met. The termination criterion can be a predefined number of generations, a threshold of fitness, a convergence of the population, or a combination of these factors.

: https://www.javatpoint.com/genetic-algorithm-in-machine-learning
: https://towardsdatascience.com/complete-step-by-step-genetic-algorithm-from-scratch-for-global-optimization-6fee5c55dd3b
: https://towardsdatascience.com/an-introduction-to-genetic-algorithms-c07a81032547
: https://en.wikipedia.org/wiki/Genetic_algorithm
: https://www.britannica.com/technology/genetic-algorithm
: https://www.geeksforgeeks.org/genetic-algorithms/