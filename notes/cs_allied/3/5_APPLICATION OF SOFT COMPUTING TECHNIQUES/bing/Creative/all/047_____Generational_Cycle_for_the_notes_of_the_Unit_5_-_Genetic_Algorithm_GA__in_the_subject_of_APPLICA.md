# Generational Cycle for the notes of the Unit 5 - Genetic Algorithm(GA) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- A genetic algorithm (GA) is a bio-inspired optimization technique that mimics the natural process of evolution and selection .
- A GA works on a population of candidate solutions, each encoded as a string of symbols (usually binary digits) that represent the values of the decision variables .
- A GA iterates through a series of generations, where each generation consists of the following steps   :
  - **Selection**: A subset of the population is chosen based on their fitness values, which measure how well they satisfy the objective function. The selection process favors the fitter individuals, but also allows some diversity to maintain exploration and avoid premature convergence  .
  - **Crossover**: Pairs of selected individuals are recombined to produce new offspring, by exchanging parts of their strings at random points. Crossover introduces variation and exploits the existing genetic material to create potentially better solutions  .
  - **Mutation**: Each offspring is subjected to a small probability of random changes in some of their string positions. Mutation introduces diversity and prevents the loss of genetic information due to crossover  .
  - **Evaluation**: The fitness values of the new offspring are calculated and compared with the existing population. The best individuals are retained for the next generation, while the worst ones are discarded   .
- The generational cycle is repeated until a termination criterion is met, such as reaching a maximum number of generations, achieving a desired fitness value, or finding no improvement for a certain number of iterations  .
- A GA can be represented by a flow chart as shown below:

![Flow chart of a genetic algorithm](https://upload.wikimedia.org/wikipedia/commons/6/6d/Genetic_algorithm.svg)