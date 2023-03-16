### Working principle of genetic algorithm

A genetic algorithm (GA) is a computational technique that mimics the process of natural selection to find optimal or near-optimal solutions to a given problem. A GA operates on a population of potential solutions, each encoded as a string of symbols called a chromosome. The chromosomes are evaluated by a fitness function that measures how well they solve the problem. The GA then applies genetic operators, such as selection, crossover, and mutation, to create a new population of chromosomes. The process is repeated until a termination criterion is met, such as reaching a maximum number of generations, achieving a desired fitness level, or finding the optimal solution.

The working principle of a standard GA can be summarized by the following steps:

1. **Initialization**: Generate a random initial population of chromosomes, usually of fixed length and binary representation.
2. **Evaluation**: Calculate the fitness of each chromosome in the population using the fitness function.
3. **Selection**: Select a subset of chromosomes from the current population to be the parents of the next generation. The selection is usually based on the fitness values, such that fitter chromosomes have a higher chance of being selected.
4. **Crossover**: Combine two or more parent chromosomes to produce one or more offspring chromosomes. The crossover is usually done by exchanging segments of the parent chromosomes at random points, called crossover points.
5. **Mutation**: Alter one or more symbols in some of the offspring chromosomes at random positions, called mutation points. The mutation is usually done by flipping binary bits or changing the values of the symbols.
6. **Replacement**: Replace the current population with the new population of offspring chromosomes, either completely or partially. The replacement can be done by keeping the best chromosomes from both populations, or by using a fitness-based or age-based criterion.
7. **Termination**: Check if the termination criterion is met. If not, go back to step 2. If yes, stop the algorithm and return the best chromosome as the solution.

The following figure illustrates the working principle of a standard GA:

![GA flowchart](https://www.javatpoint.com/images/ann/ga.png)

: https://www.javatpoint.com/artificial-neural-network-genetic-algorithm
: https://www.mathworks.com/help/gads/how-the-genetic-algorithm-works.html