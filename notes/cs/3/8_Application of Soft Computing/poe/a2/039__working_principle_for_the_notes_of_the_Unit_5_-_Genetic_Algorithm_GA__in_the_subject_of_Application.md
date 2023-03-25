 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Working principle of Genetic Algorithm (GA)

1. Representation: Encode the solution to the problem into a chromosome (string of bits/numbers). Each gene in the chromosome represents a parameter of the solution.
2. Initial population: Create a random initial population of n chromosomes.
3. Fitness evaluation: Evaluate the fitness of each chromosome in the population. The fitness is the measure of how good a solution is.
4. Selection: Select the fitter chromosomes from the population to be parents and breed a new generation. This can be done using methods like roulette wheel selection, tournament selection, etc.
5. Crossover: Perform crossover on the selected parents to produce offspring. Crossover involves swapping of gene segments between two parent chromosomes.
6. Mutation: Mutate the offspring by flipping/changing the values of some genes with a mutation probability. This introduces diversity in the population.
7. Next generation: The offspring population becomes the next generation. Go back to step 3 until the termination criteria is met (e.g. maximum generations reached).
8. Solution: The fittest chromosome in the final generation is the solution to the problem.

The steps are iterated until a good enough solution is found or the maximum number of generations is reached. GA works on the principle of natural selection and evolution to find the optimal solution.