## Unit 5 - Genetic Algorithm (GA)

- A genetic algorithm is a **metaheuristic** inspired by the process of **natural selection** that belongs to the larger class of **evolutionary algorithms** .
- Genetic algorithms are commonly used to generate **high-quality solutions** to **optimization and search problems** by relying on biologically inspired operators such as **selection, mutation, inheritance and recombination**  .
- The basic steps of a genetic algorithm are as follows:
  - **Initialization**: Generate a random population of individuals (possible solutions) with different characteristics (genes).
  - **Evaluation**: Assign a fitness score to each individual based on how well it solves the problem.
  - **Selection**: Choose a subset of individuals from the current population based on their fitness scores, using a probabilistic method such as roulette wheel selection or tournament selection.
  - **Crossover**: Create new individuals by combining the genes of two selected parents, using a method such as one-point crossover or uniform crossover.
  - **Mutation**: Modify some genes of the new individuals randomly, using a method such as bit-flip mutation or swap mutation.
  - **Replacement**: Replace the old population with the new one, using a method such as elitism or generational replacement.
  - **Termination**: Repeat the above steps until a stopping criterion is met, such as reaching a maximum number of generations, finding an optimal solution, or reaching a convergence threshold.