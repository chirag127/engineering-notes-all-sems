 Here is the content in markdown format without any emojis or external links and in formal tone:

### Procedures of Genetic Algorithm (GA)

1.  Initialization: Initialize a population of n chromosomes (candidate solutions) randomly. Each chromosome represents a potential solution to the problem.
2.  Fitness evaluation: Evaluate the fitness f(x) of each chromosome x in the population. The fitness function measures the quality of the chromosome as a solution to the problem.
3.  Selection: Select chromosomes from the population to be parents for reproduction. Often the selection process favors chromosomes with higher fitness.
4.  Crossover: Perform crossover on the selected parent chromosomes to produce offspring chromosomes. Crossover involves swapping of gene segments between two parent chromosomes.
5.  Mutation: Apply mutation to the offspring chromosomes with a low probability. Mutation alters one or more gene values in a chromosome from its initial state. This adds diversity to the population.
6.  Replacement: Use the offspring chromosomes to replace the chromosomes in the population with lesser fitness. This forms a new generation of the population.
7.  Termination: If the termination criteria is met (maximum generations, solution is good enough, etc.), stop and return the best solution. Otherwise, go to step#2.

The steps are repeated iteratively until a termination criterion is met. At the end, the chromosome with the highest fitness contains the optimal or near-optimal solution to the problem. The key advantage of GA is that it searches a wide range of the solution space in parallel, avoiding local optima.