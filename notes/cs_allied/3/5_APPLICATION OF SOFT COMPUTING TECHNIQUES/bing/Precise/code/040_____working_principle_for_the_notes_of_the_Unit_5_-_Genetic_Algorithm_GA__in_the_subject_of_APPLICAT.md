### Working Principle of Genetic Algorithm (GA)

Genetic Algorithm (GA) is a search heuristic that is based on the process of natural selection. It is used to find approximate solutions to optimization and search problems. The basic steps involved in the working of a GA are as follows:

1. **Initialization**: A population of potential solutions to the problem is generated randomly. Each solution is represented as a chromosome, which is a string of genes.

2. **Evaluation**: The fitness of each chromosome in the population is evaluated using a fitness function. The fitness function measures how well the chromosome solves the problem at hand.

3. **Selection**: Chromosomes are selected for reproduction based on their fitness. The fitter the chromosome, the higher the chance it has of being selected for reproduction.

4. **Crossover**: Pairs of chromosomes are chosen for reproduction and their genes are combined to create offspring. This is done by exchanging segments of the chromosomes between the parents.

5. **Mutation**: The genes of the offspring are randomly mutated with a small probability. This introduces new genetic material into the population and helps to prevent the algorithm from getting stuck in a local optimum.

6. **Replacement**: The offspring are added to the population and the least fit chromosomes are removed to maintain a constant population size.

7. **Termination**: The algorithm terminates when a satisfactory solution has been found or when a predefined stopping criterion has been met.

These steps are repeated for multiple generations until a satisfactory solution is found. The GA is a stochastic algorithm, meaning that the solutions it finds are not guaranteed to be optimal, but they are often good approximations. It is a powerful tool for solving complex optimization problems and has been applied to a wide range of applications.