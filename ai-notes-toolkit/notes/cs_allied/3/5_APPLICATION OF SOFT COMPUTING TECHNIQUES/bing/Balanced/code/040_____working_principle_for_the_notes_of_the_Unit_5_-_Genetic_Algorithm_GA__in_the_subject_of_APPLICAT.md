### Working principle of genetic algorithm

A genetic algorithm (GA) is a computational method that mimics the process of natural selection to find optimal solutions to complex problems. A GA works as follows  :

- **Initialization**: A GA starts with a population of randomly generated solutions, called individuals or chromosomes. Each individual is a string of characters (usually binary digits) that encodes a possible solution to the problem.
- **Evaluation**: A GA evaluates the quality of each individual using a fitness function, which assigns a numerical score to each solution based on how well it meets the desired criteria.
- **Selection**: A GA selects a subset of individuals from the current population to produce the next generation, based on their fitness values. The selection process favors individuals with higher fitness, but also maintains some diversity in the population to avoid premature convergence to a suboptimal solution.
- **Crossover**: A GA applies a crossover operator to some pairs of selected individuals, which creates new individuals by exchanging parts of their strings. Crossover introduces variation and recombination in the population, which can help explore new regions of the search space.
- **Mutation**: A GA applies a mutation operator to some individuals, which alters one or more characters in their strings. Mutation introduces random changes in the population, which can help escape from local optima and maintain diversity.
- **Termination**: A GA repeats the steps of evaluation, selection, crossover, and mutation until a stopping criterion is met, such as reaching a maximum number of generations, finding an individual with a desired fitness value, or reaching a convergence threshold.

The following figure illustrates the working principle of a standard GA:

![GA flowchart](https://static.javatpoint.com/tutorial/artificial-neural-network/images/artificial-neural-network-genetic-algorithm.png)

: https://www.javatpoint.com/artificial-neural-network-genetic-algorithm
: https://www.mathworks.com/help/gads/how-the-genetic-algorithm-works.html
: https://www.geeksforgeeks.org/genetic-algorithms/