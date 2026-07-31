# Generational Cycle for Genetic Algorithm

- A genetic algorithm (GA) is a bio-inspired optimization technique that mimics the natural process of evolution and natural selection .
- A GA works on a population of candidate solutions, each encoded as a string of symbols (usually binary digits) that represent the values of the decision variables .
- A GA iterates through a series of generations, where each generation consists of the following steps  :
  - **Selection**: A subset of the population is chosen based on their fitness values, which measure how well they satisfy the objective function. The selection process favors the fitter individuals, but also allows some diversity to maintain exploration and avoid premature convergence.
  - **Crossover**: Pairs of selected individuals are recombined to produce new offspring, by exchanging parts of their strings at random points. Crossover introduces variation and allows the offspring to inherit traits from both parents.
  - **Mutation**: Each offspring is subjected to a small probability of random changes in their string, by flipping some bits. Mutation introduces further variation and helps to escape from local optima.
  - **Evaluation**: The fitness values of the new offspring are calculated and compared with the existing population. The fittest individuals are retained for the next generation, while the least fit ones are discarded.
- The GA terminates when a predefined stopping criterion is met, such as reaching a maximum number of generations, achieving a desired fitness value, or converging to a stable population  .
- A GA can be represented by a flowchart as shown below:

![Flowchart of GA](https://i.ytimg.com/vi/8VaSFQ0yNSA/maxresdefault.jpg)

- A GA can be used to solve various types of optimization and search problems, such as function optimization, machine learning, scheduling, routing, design, etc .