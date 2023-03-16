# Unit 5 - Genetic Algorithm (GA)

- A genetic algorithm is a **metaheuristic** inspired by the process of **natural selection** that belongs to the larger class of **evolutionary algorithms** .
- A genetic algorithm is used for finding **optimized solutions** to search problems based on the theory of **natural selection and evolutionary biology**.
- A genetic algorithm makes use of techniques inspired from evolutionary biology such as **selection, mutation, inheritance and recombination** to solve a problem .
- A genetic algorithm is composed of the following steps:
  - **Initialization**: Generate a random population of individuals (possible solutions) to the problem.
  - **Evaluation**: Assign a fitness value to each individual based on how well it solves the problem.
  - **Selection**: Select a subset of individuals from the current population based on their fitness values. The fitter individuals have a higher chance of being selected.
  - **Crossover**: Combine two or more selected individuals to produce new offspring (new solutions). This mimics the biological process of recombination.
  - **Mutation**: Apply random changes to some of the offspring to introduce diversity and avoid local optima. This mimics the biological process of mutation.
  - **Termination**: Check if the stopping criterion is met, such as reaching a maximum number of generations, finding an optimal solution, or reaching a predefined fitness threshold. If not, go back to the evaluation step and repeat the process.