### Working Principle of Genetic Algorithm (GA)

Genetic Algorithm (GA) is a search heuristic that is based on the process of natural selection. It is used to find approximate solutions to optimization and search problems. The working principle of GA can be summarized in the following points:

1. **Initialization**: A population of potential solutions to the problem is generated randomly. Each solution is represented as a chromosome, which is a string of genes.

2. **Evaluation**: The fitness of each chromosome in the population is evaluated using a fitness function. The fitness function measures how well the chromosome solves the problem at hand.

3. **Selection**: Chromosomes are selected for reproduction based on their fitness. The fitter the chromosome, the higher the chance it has to be selected for reproduction.

4. **Crossover**: Pairs of chromosomes are selected for mating and their genes are combined to create offspring. This process is called crossover and it introduces variation in the population.

5. **Mutation**: The genes of the offspring are randomly mutated with a certain probability. This introduces further variation in the population.

6. **Replacement**: The offspring replace the least fit individuals in the population.

7. **Termination**: The algorithm terminates when a stopping criterion is met, such as reaching a maximum number of generations or finding a satisfactory solution.

The above steps are repeated until the termination criterion is met. The final result is the fittest chromosome in the population, which represents an approximate solution to the problem.