### Working Principle of Genetic Algorithm (GA)

Genetic Algorithm (GA) is a search heuristic that is based on the process of natural selection. It is used to find approximate solutions to optimization and search problems. The working principle of GA can be summarized in the following points:

1. **Initialization**: GA starts with a population of randomly generated solutions, called chromosomes. Each chromosome represents a potential solution to the problem.

2. **Evaluation**: The fitness of each chromosome is evaluated using a fitness function. The fitness function measures how well the chromosome solves the problem.

3. **Selection**: Chromosomes are selected for reproduction based on their fitness. The fitter the chromosome, the higher the chance it has to be selected for reproduction.

4. **Crossover**: Pairs of chromosomes are selected for crossover, which is the process of exchanging genetic information between two chromosomes to create new offspring.

5. **Mutation**: After crossover, mutation is applied to the offspring. Mutation is the process of randomly changing the value of a gene in a chromosome.

6. **Replacement**: The new offspring are then added to the population, replacing the least fit chromosomes.

7. **Termination**: The algorithm terminates when a stopping criterion is met, such as reaching a maximum number of generations or finding a satisfactory solution.

This is the basic working principle of GA. It is an iterative process that continues until a satisfactory solution is found or a stopping criterion is met. The algorithm can be customized by changing the selection, crossover, and mutation operators, as well as the fitness function and the stopping criterion.