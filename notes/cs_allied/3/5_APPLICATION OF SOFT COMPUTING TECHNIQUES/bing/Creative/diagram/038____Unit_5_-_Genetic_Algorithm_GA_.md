## Unit 5 - Genetic Algorithm (GA)

- A genetic algorithm is a **metaheuristic** inspired by the process of **natural selection** that belongs to the larger class of **evolutionary algorithms** .
- Genetic algorithms are commonly used to generate **high-quality solutions** to **optimization and search problems** by relying on biologically inspired operators such as **selection, mutation, inheritance and recombination**  .
- The most commonly employed method in genetic algorithms is to create a group of **individuals** randomly from a given **population**. Each individual represents a **candidate solution** to the problem and has a **fitness value** that indicates how well it solves the problem .
- The genetic algorithm works by **repeatedly** applying the following steps until a **termination criterion** is met:
  - **Selection**: Choose a subset of individuals from the current population based on their fitness values. The fitter individuals have a higher chance of being selected.
  - **Crossover**: Combine two or more selected individuals to produce new offspring. The offspring inherit some characteristics from each parent, creating diversity in the population.
  - **Mutation**: Alter some genes of the offspring randomly, introducing some variation in the population.
  - **Replacement**: Replace some or all of the current population with the new offspring, forming the next generation of the population.
- The genetic algorithm can be **customized** by changing the following parameters:
  - **Population size**: The number of individuals in each generation of the population.
  - **Crossover rate**: The probability of applying crossover to a pair of selected individuals.
  - **Mutation rate**: The probability of applying mutation to an offspring.
  - **Selection method**: The technique used to select individuals from the population, such as roulette wheel, tournament, rank-based, etc.
  - **Crossover method**: The technique used to combine selected individuals, such as one-point, two-point, uniform, etc.
  - **Mutation method**: The technique used to alter genes of an offspring, such as bit-flip, swap, insert, etc.
  - **Replacement method**: The technique used to replace the current population with the new offspring, such as elitism, generational, steady-state, etc.
  - **Termination criterion**: The condition used to stop the genetic algorithm, such as reaching a maximum number of generations, achieving a desired fitness value, or converging to a similar population.