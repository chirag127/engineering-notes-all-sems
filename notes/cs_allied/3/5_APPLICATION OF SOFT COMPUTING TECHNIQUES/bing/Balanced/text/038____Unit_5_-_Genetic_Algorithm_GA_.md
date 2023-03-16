## Unit 5 - Genetic Algorithm (GA)

- A genetic algorithm is a **metaheuristic** inspired by the process of **natural selection** that belongs to the larger class of **evolutionary algorithms** .
- Genetic algorithms are commonly used to generate **high-quality solutions** to **optimization and search problems** by relying on biologically inspired operators such as **selection, mutation, inheritance and recombination**  .
- The basic steps of a genetic algorithm are:

  1. **Initialization**: Generate a random population of individuals (possible solutions) from a given search space.
  2. **Evaluation**: Assign a fitness value to each individual based on how well it solves the problem.
  3. **Selection**: Choose a subset of individuals from the current population based on their fitness values. The fitter individuals have a higher chance of being selected.
  4. **Crossover**: Combine two or more selected individuals to produce new offspring (new solutions). This mimics the biological process of recombination.
  5. **Mutation**: Apply random changes to some offspring to introduce diversity and avoid premature convergence. This mimics the biological process of mutation.
  6. **Replacement**: Replace the current population with the new offspring, or a combination of both.
  7. **Termination**: Repeat steps 2 to 6 until a stopping criterion is met, such as reaching a maximum number of generations, finding an optimal solution, or reaching a time limit.

- Genetic algorithms have several advantages, such as:

  - They are **robust** and can handle noisy and incomplete data.
  - They are **flexible** and can be applied to a wide range of problems.
  - They are **parallelizable** and can exploit multiple processors or machines.
  - They are **adaptive** and can adjust to changing environments or objectives.

- Genetic algorithms also have some limitations, such as:

  - They are **stochastic** and may not guarantee the same results in every run.
  - They may require **tuning** of parameters, such as population size, crossover rate, mutation rate, etc.
  - They may suffer from **premature convergence** and get stuck in local optima.
  - They may have **scalability** issues when dealing with large and complex problems.