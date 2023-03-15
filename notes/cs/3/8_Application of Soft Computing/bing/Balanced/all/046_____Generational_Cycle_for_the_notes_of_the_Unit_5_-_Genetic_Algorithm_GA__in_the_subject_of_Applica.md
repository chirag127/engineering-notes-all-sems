# Generational Cycle for Genetic Algorithm

- A genetic algorithm (GA) is a bio-inspired optimization technique that mimics the natural process of evolution and selection .
- A GA works on a population of candidate solutions, each encoded as a string of symbols (usually binary digits) that represent the values of the decision variables .
- A GA iterates through a series of generations, where each generation consists of the following steps   :

  - **Selection**: A subset of the population is chosen based on their fitness values, which measure how well they satisfy the objective function. The selection process favors the fitter individuals, but also allows some diversity to maintain exploration.
  - **Crossover**: Pairs of selected individuals are recombined to produce new offspring, by exchanging parts of their strings at random points. Crossover introduces variation and exploits the existing genetic material to create potentially better solutions.
  - **Mutation**: Each offspring is subjected to a random alteration of one or more symbols in its string, with a low probability. Mutation introduces diversity and prevents premature convergence to suboptimal solutions.
  - **Evaluation**: The fitness values of the new offspring are calculated and compared with the existing population. The offspring may replace some or all of the existing individuals, depending on the replacement strategy. The replacement process ensures that the population size remains constant and that the best solutions are preserved.

- The GA terminates when a predefined stopping criterion is met, such as reaching a maximum number of generations, achieving a desired fitness value, or detecting no improvement for a certain number of generations  .
- The GA returns the best solution found in the final population as the output .