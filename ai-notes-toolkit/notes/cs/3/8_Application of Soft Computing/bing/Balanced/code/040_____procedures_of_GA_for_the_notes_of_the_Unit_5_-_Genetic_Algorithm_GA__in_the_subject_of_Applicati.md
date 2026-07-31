# Procedures of GA for the notes of the Unit 5 - Genetic Algorithm(GA) in the subject of Application of Soft Computing

- Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection.
- GA is good at taking larger, potentially huge search space and navigating them looking for optimal solution which we might not find in lifetime.
- GA is better than other traditional algorithm in that they are more robust.
- GA uses techniques inspired by evolutionary biology such as inheritance, mutation, selection, and crossover (also called recombination).
- The basic steps of GA are as follows  :
  - **Initialization**: Generate an initial population of size N, randomly or heuristically.
  - **Evaluation**: Calculate the fitness or objective function value of each individual in the population.
  - **Selection**: Select a subset of individuals from the current population based on their fitness, using a selection method such as roulette wheel, tournament, rank, etc.
  - **Crossover**: Apply a crossover operator to pairs of selected individuals, creating new offspring that inherit some features from both parents.
  - **Mutation**: Apply a mutation operator to some of the offspring, introducing small random changes in their features.
  - **Replacement**: Replace the current population with the new offspring, using a replacement method such as elitism, generational, steady-state, etc.
  - **Termination**: Check if a termination criterion is met, such as reaching a maximum number of generations, finding an optimal or near-optimal solution, or reaching a convergence threshold. If not, go back to the evaluation step and repeat the process.