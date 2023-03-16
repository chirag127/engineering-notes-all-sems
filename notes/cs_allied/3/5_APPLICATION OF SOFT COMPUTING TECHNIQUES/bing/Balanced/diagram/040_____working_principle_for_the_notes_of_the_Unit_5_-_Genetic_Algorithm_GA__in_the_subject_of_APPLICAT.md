### Working principle of genetic algorithm

A genetic algorithm (GA) is a computational method that mimics the process of natural selection to find optimal solutions to complex problems. A GA works as follows :

- **Initialization**: A GA starts with a random population of individuals, where each individual represents a possible solution to the problem. Each individual is encoded as a string of characters, called a chromosome, that corresponds to the features or parameters of the solution.
- **Evaluation**: A GA evaluates each individual in the population using a fitness function, which measures how well the individual solves the problem. The fitness function assigns a numerical score to each individual, reflecting its quality or performance.
- **Selection**: A GA selects some individuals from the current population to produce the next generation, based on their fitness values. The selection process favors individuals with higher fitness, as they have a higher chance of passing their genes to the offspring. There are different methods of selection, such as roulette wheel, tournament, rank-based, etc.
- **Crossover**: A GA applies a crossover operator to some pairs of selected individuals, to create new individuals by combining parts of their chromosomes. The crossover operator simulates the biological process of sexual reproduction, where offspring inherit traits from both parents. The crossover operator introduces diversity and exploration in the population, as it generates new solutions that may not exist in the previous generation.
- **Mutation**: A GA applies a mutation operator to some individuals in the population, to create new individuals by randomly modifying some parts of their chromosomes. The mutation operator simulates the biological process of genetic variation, where offspring may have some traits that are different from their parents. The mutation operator introduces diversity and exploration in the population, as it generates new solutions that may not exist in the previous generation.
- **Termination**: A GA repeats the steps of evaluation, selection, crossover, and mutation until a termination criterion is met. The termination criterion can be a predefined number of generations, a threshold of fitness value, a convergence of the population, etc.

The following diagram illustrates the working principle of a GA:

![GA diagram](https://static.javatpoint.com/tutorial/artificial-intelligence/images/artificial-neural-network-genetic-algorithm.png)

: Artificial Neural Network Genetic Algorithm - Javatpoint
: How the Genetic Algorithm Works - MATLAB & Simulink - MathWorks