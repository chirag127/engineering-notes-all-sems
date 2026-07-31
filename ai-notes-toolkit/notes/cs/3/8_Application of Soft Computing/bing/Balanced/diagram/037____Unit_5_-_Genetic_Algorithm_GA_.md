## Unit 5 - Genetic Algorithm (GA)

- A genetic algorithm is a **metaheuristic** inspired by the process of **natural selection** that belongs to the larger class of **evolutionary algorithms** .
- A genetic algorithm is used for finding **optimized solutions** to search problems based on the theory of **natural selection and evolutionary biology**.
- A genetic algorithm makes use of techniques inspired from evolutionary biology such as **selection, mutation, inheritance and recombination** to solve a problem .
- The most commonly employed method in genetic algorithms is to create a group of individuals randomly from a given population. This group is called the **initial population** .
- Each individual in the population is called a **chromosome** and represents a possible solution to the problem. A chromosome is composed of a sequence of **genes**, which are the basic units of information.
- Each chromosome is assigned a **fitness value** based on how well it solves the problem. The fitness value is calculated by a **fitness function** that evaluates the quality of the solution.
- The genetic algorithm then applies the following steps repeatedly until a termination condition is met:
  - **Selection**: A subset of chromosomes is chosen from the current population based on their fitness values. The selection process favors the fitter chromosomes, which have a higher chance of being selected for reproduction.
  - **Crossover**: Pairs of chromosomes are randomly selected from the subset and combined to produce new chromosomes. The crossover process recombines the genes of the parent chromosomes to create new variations of solutions.
  - **Mutation**: Some genes in the new chromosomes are randomly altered to introduce further diversity in the population. The mutation process introduces small changes in the solutions that may lead to improvement or deterioration.
  - **Replacement**: The new chromosomes replace some or all of the old chromosomes in the population. The replacement process determines which chromosomes will survive to the next generation.
- The termination condition can be based on a number of criteria, such as reaching a maximum number of generations, achieving a desired fitness value, or converging to a similar solution.
- The genetic algorithm returns the best chromosome (solution) found in the final population.