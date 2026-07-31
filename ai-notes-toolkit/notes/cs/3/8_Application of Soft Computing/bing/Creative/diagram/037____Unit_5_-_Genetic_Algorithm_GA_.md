## Unit 5 - Genetic Algorithm (GA)

- A genetic algorithm is a **metaheuristic** inspired by the process of **natural selection** that belongs to the larger class of **evolutionary algorithms** .
- Genetic algorithms are commonly used to generate **high-quality solutions** to **optimization and search problems** by relying on biologically inspired operators such as **selection, mutation, inheritance and recombination**  .
- The most commonly employed method in genetic algorithms is to create a group of **individuals** randomly from a given **population**. Each individual represents a **candidate solution** to the problem and has a **fitness value** that indicates how well it solves the problem .
- The genetic algorithm works by applying the following steps repeatedly until a **termination criterion** is met:
  - **Selection**: A subset of individuals is chosen from the current population based on their fitness values. The higher the fitness, the higher the chance of being selected.
  - **Crossover**: Pairs of selected individuals are combined to produce new individuals, called **offspring**, by exchanging some of their **genes**. Genes are the basic units of information that encode the characteristics of the solution.
  - **Mutation**: Some of the genes of the offspring are randomly modified to introduce **variation** and **exploration** in the search space.
  - **Replacement**: The offspring are inserted into the next generation of the population, replacing some of the less fit individuals.
- The genetic algorithm can be customized by choosing different **parameters** and **operators** that suit the problem domain. Some of the common parameters are:
  - **Population size**: The number of individuals in each generation of the population.
  - **Crossover rate**: The probability of applying crossover to a pair of selected individuals.
  - **Mutation rate**: The probability of applying mutation to an offspring.
  - **Selection method**: The technique used to select individuals from the population, such as **roulette wheel**, **tournament**, **rank**, etc.
  - **Crossover method**: The technique used to combine two individuals to produce offspring, such as **single-point**, **multi-point**, **uniform**, etc.
  - **Mutation method**: The technique used to modify the genes of an offspring, such as **bit-flip**, **swap**, **insert**, etc.
  - **Replacement method**: The technique used to insert the offspring into the next generation of the population, such as **generational**, **steady-state**, **elitism**, etc.
  - **Termination criterion**: The condition that determines when to stop the genetic algorithm, such as **maximum number of generations**, **maximum number of evaluations**, **convergence**, **optimal solution found**, etc.