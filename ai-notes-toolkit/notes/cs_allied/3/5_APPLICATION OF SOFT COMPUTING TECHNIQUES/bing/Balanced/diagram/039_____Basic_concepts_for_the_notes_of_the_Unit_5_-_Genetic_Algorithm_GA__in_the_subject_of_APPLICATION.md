### Basic concepts for the notes of the Unit 5 - Genetic Algorithm(GA) in the subject of APPLICATION OF SOFT COMPUTING TECHNIQUES

- A genetic algorithm (GA) is a heuristic search algorithm used to solve search and optimization problems. This algorithm is a subset of evolutionary algorithms, which are used in computation. Genetic algorithms employ the concept of genetics and natural selection to provide solutions to problems.
- Genetic algorithms are based on the ideas of natural selection and genetics. These are intelligent exploitation of random search provided with historical data to direct the search into the region of better performance in solution space. They are commonly used to generate high-quality solutions for optimization problems and search problems.
- Genetic algorithms operate on a population of potential solutions called individuals or chromosomes. Each individual is a string of genes, which are the basic units of information. Genes can be binary, real-valued, or symbolic.
- Genetic algorithms work by applying three main operators: selection, crossover, and mutation. Selection is the process of choosing the best individuals from the population based on their fitness scores. Crossover is the process of combining two individuals to produce offspring that inherit some characteristics from both parents. Mutation is the process of randomly altering some genes in an individual to introduce diversity and avoid premature convergence.
- Genetic algorithms follow a cycle of steps until a termination condition is met. The steps are:

  1. Initialize a random population of individuals.
  2. Evaluate the fitness of each individual in the population.
  3. Select the best individuals for reproduction.
  4. Apply crossover and mutation operators to generate new offspring.
  5. Replace the old population with the new offspring.
  6. Repeat steps 2 to 5 until the termination condition is satisfied.

- Genetic algorithms have several advantages, such as:

  - They are robust and can handle noisy and complex problems.
  - They can explore a large and diverse search space and avoid getting stuck in local optima.
  - They can adapt to changing environments and requirements.
  - They can incorporate domain knowledge and constraints easily.

- Genetic algorithms also have some limitations, such as:

  - They require a lot of parameters to be tuned, such as population size, crossover rate, mutation rate, etc.
  - They can be computationally expensive and time-consuming, especially for large and complex problems.
  - They can converge prematurely or lose diversity if the operators are not well designed.