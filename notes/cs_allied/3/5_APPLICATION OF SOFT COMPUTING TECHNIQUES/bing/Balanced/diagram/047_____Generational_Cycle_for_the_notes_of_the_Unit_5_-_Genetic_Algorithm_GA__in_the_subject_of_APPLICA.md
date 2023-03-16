### Generational Cycle for Genetic Algorithm

- A genetic algorithm (GA) is a bio-inspired optimization technique that mimics the natural process of evolution and selection .
- A GA works on a population of candidate solutions, each encoded as a string of symbols (usually binary digits) that represent the values of the decision variables .
- A GA iterates through a series of generations, where each generation consists of the following steps   :

  1. **Selection**: A subset of the population is chosen based on their fitness values, which measure how well they satisfy the objective function. The selection process favors the fitter individuals, but also allows some diversity to maintain exploration and avoid premature convergence.
  2. **Crossover**: Pairs of selected individuals are recombined to produce new offspring that inherit some features from each parent. Crossover is a probabilistic operation that aims to create better solutions by exchanging useful information between individuals.
  3. **Mutation**: Each offspring is subjected to a random alteration of one or more symbols in its string. Mutation is also a probabilistic operation that introduces some variation and diversity in the population, and helps to escape from local optima.
  4. **Evaluation**: The fitness values of the new offspring are computed and compared with the existing population. Depending on the replacement strategy, some or all of the old individuals are replaced by the new ones, forming the next generation.

- The GA terminates when a predefined stopping criterion is met, such as reaching a maximum number of generations, achieving a desired fitness value, or converging to a single solution  .
- The GA returns the best solution found in the final population as the output  .

- The following diagram illustrates the generational cycle of a GA:

```
+-----------------+
| Initial         |
| Population      |
+-----------------+
        |
        | Evaluation
        v
+-----------------+
| Selection       |
+-----------------+
        |
        | Crossover
        v
+-----------------+
| Mutation        |
+-----------------+
        |
        | Evaluation
        v
+-----------------+
| Replacement     |
+-----------------+
        |
        | Stopping criterion?
        v
       Yes
        |
        v
+-----------------+
| Output          |
| Best Solution   |
+-----------------+
```