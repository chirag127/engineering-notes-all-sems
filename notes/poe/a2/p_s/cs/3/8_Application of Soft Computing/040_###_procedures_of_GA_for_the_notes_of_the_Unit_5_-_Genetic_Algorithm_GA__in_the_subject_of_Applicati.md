 Here is the content in markdown format for the procedures of Genetic Algorithm(GA) for the notes of Unit 5 - Genetic Algorithm(GA) in the subject of Application of Soft Computing:

### Procedures of Genetic Algorithm(GA)

1.  Initialization - Randomly initialize a population of chromosomes(solutions). Each chromosome represents a potential solution to the problem.
2.  Evaluation - Evaluate the fitness of each chromosome in the population. The fitness function determines the optimality of a chromosome.
3.  Selection - Select the fittest chromosomes from the population to reproduce and generate offspring for the next generation. This is done using selection methods like roulette wheel selection or tournament selection.
4.  Crossover - Perform crossover on the selected chromosomes to produce offspring chromosomes. Crossover involves exchanging genetic material between two chromosomes to generate new offspring. Common crossover methods are single-point crossover and two-point crossover.
5.  Mutation - Mutate the offspring chromosomes randomly to introduce diversity and explore new areas of the search space. Bitwise mutation is a common mutation technique used for binary encoded chromosomes.
6.  Replacement - Replace the least fit chromosomes in the population with the newly generated offspring chromosomes.
7.  Termination - If the termination criteria is not met, repeat from step #2. Otherwise, stop and return the best chromosome as the solution. Common termination criteria are maximum number of generations or achieving a satisfactory fitness level.

Advantages:
- GA is an adaptive search technique that does not require the objective function to be differentiable.
- It is robust to getting stuck in local optima as it searches a population of points, not a single point.
- It can handle both continuous and discrete variables and large solution spaces.

Disadvantages:
- GA may converge slowly if the search space is very large and complex.
- The optimal solution is not guaranteed and depends on the efficacy of the genetic operators and parameters.
- Fine tuning of GA parameters may be required to achieve good solutions.

[Include detailed ascii diagrams, examples, applications, codes, etc. if required]