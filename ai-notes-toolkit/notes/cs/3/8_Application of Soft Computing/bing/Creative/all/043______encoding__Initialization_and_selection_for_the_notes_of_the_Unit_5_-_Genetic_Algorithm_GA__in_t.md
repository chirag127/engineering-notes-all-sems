# Unit 5 - Genetic Algorithm (GA)

## Encoding, Initialization and Selection

### Encoding

- Encoding is the process of representing the possible solutions of a problem as chromosomes (strings of genes) in a genetic algorithm.
- Each gene represents a parameter or a variable in the solution.
- Encoding can be done in different ways, such as binary, integer, real, permutation, tree, etc.
- The choice of encoding depends on the nature of the problem and the operators used in the genetic algorithm.

### Initialization

- Initialization is the process of creating the initial population of chromosomes (possible solutions) for a genetic algorithm.
- The initial population can be generated randomly or using some heuristic or prior knowledge.
- The size of the population depends on the complexity of the problem and the diversity of the search space.
- A larger population may increase the chance of finding the optimal solution, but also increase the computational cost.

### Selection

- Selection is the process of choosing the best individuals (chromosomes) from the current population to produce the next generation of offspring.
- The goal of selection is to give preference to the individuals with high fitness values and allow them to pass their genes to the next generation.
- Selection can be done in different ways, such as roulette wheel, tournament, rank-based, elitist, etc.
- The choice of selection depends on the trade-off between exploration and exploitation of the search space.
- Exploration means searching for new regions of the search space, while exploitation means exploiting the known good regions.