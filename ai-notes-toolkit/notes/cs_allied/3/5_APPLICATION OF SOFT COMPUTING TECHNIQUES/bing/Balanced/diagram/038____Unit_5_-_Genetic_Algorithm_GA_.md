## Unit 5 - Genetic Algorithm(GA)

- A genetic algorithm (GA) is a bio-inspired optimization technique that mimics the natural process of evolution.
- A GA operates on a population of potential solutions, called individuals or chromosomes, that encode the values of the decision variables.
- A GA iteratively applies a set of operators, such as selection, crossover, and mutation, to generate new individuals and improve the quality of the population.
- A GA evaluates the fitness of each individual, which is a measure of how well it satisfies the objective function and the constraints of the problem.
- A GA terminates when a predefined stopping criterion is met, such as reaching a maximum number of generations, finding an optimal or near-optimal solution, or converging to a similar fitness level.

### Basic Steps of a GA

- Step 1: Initialize a random population of individuals, usually with a fixed size.
- Step 2: Evaluate the fitness of each individual in the population.
- Step 3: Select a subset of individuals from the population to be the parents for the next generation, based on their fitness values. Common selection methods include roulette wheel, tournament, and rank-based selection.
- Step 4: Apply crossover and mutation operators to the selected parents to generate offspring. Crossover combines two or more parents to produce one or more children, while mutation introduces random changes to an individual. The crossover and mutation rates control the probabilities of applying these operators.
- Step 5: Evaluate the fitness of the offspring and replace some or all of the individuals in the population with the offspring, depending on the replacement strategy. Common replacement strategies include generational, elitist, and steady-state replacement.
- Step 6: Check the stopping criterion. If it is not met, go back to Step 3. Otherwise, return the best individual or the entire population as the final solution.