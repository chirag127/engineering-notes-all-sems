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
  7. **Termination**: Repeat steps 2 to 6 until a stopping criterion is met, such as a maximum number of generations, a satisfactory fitness level, or a lack of improvement.

- Genetic algorithms have several advantages, such as:

  - They are **robust** and can handle noisy and incomplete data.
  - They can **explore** a large and complex search space and find **global optima**.
  - They can **adapt** to changing environments and **learn** from previous solutions.
  - They are **flexible** and can be customized for different problems and domains.

- Genetic algorithms also have some limitations, such as:

  - They require a **good representation** of the problem and a **suitable fitness function** to guide the search.
  - They may **converge prematurely** to suboptimal solutions if the diversity is lost or the selection pressure is too high.
  - They may be **computationally expensive** and **slow** to converge compared to other methods.
  - They may **lack interpretability** and **explainability** of the solutions.