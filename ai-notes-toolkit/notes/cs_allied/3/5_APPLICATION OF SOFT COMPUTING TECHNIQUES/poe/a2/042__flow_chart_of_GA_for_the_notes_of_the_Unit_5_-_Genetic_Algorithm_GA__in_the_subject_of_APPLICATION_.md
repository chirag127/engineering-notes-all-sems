 Here is the content in Markdown format without any emojis or external links:

### Flow Chart of Genetic Algorithm (GA)

1.  Generate initial population: Generate random solutions (individuals) to form the initial population. Each individual is represented by chromosomes which are string of 0s and 1s.
2.  Evaluate fitness: Evaluate the fitness of each individual in the population. The fitness function is the objective function of the optimization problem we are trying to solve.
3.  Selection: Select individuals from the population to be parents for reproducing the next generation. Individuals with higher fitness have higher chances of being selected. Selection can be done using various methods like roulette wheel selection, tournament selection, etc.
4.  Crossover: Perform crossover on the selected parents to produce offspring for the next generation. Crossover involves swapping of bits between the chromosomes of the parents. Single-point, two-point and uniform crossover are some of the types of crossover operators used.
5.  Mutation: Mutate the offspring with a very small probability to introduce diversity in the population. Mutation involves flipping a bit in the chromosome from 0 to 1 or vice versa.
6.  Next Generation: The offspring after crossover and mutation form the next generation population.
7.  Stopping criteria: Check if the stopping criteria is met. If not go to step #2. The algorithm stops if the maximum number of generations is reached or the fitness does not improve for a certain number of generations. The best solution obtained so far is the output of GA.

The content is written in a formal manner with points to make it look like study material. No emojis or external links are included. The content is written inside the specified header in Markdown format. Please let me know if you would like me to modify or add anything.