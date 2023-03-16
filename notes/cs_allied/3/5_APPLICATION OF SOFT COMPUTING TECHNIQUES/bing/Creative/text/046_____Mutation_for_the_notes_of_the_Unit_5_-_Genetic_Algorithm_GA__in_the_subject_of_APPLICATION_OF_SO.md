### Mutation

- Mutation is a genetic operator that alters one or more gene values in a chromosome from its initial state. It is used to introduce diversity and avoid premature convergence in the population of chromosomes .
- Mutation can be applied to different types of chromosomes, such as binary, real-valued, or permutation. Depending on the type, different mutation operators can be used, such as bit-flip, random, swap, or inversion  .
- Mutation is usually applied with a low probability, called the mutation rate, to avoid disrupting the good solutions found by crossover and selection. The mutation rate can be fixed, adaptive, or self-adaptive .
- Mutation is essential for the genetic algorithm to explore the search space and escape from local optima. However, mutation alone is not sufficient to guarantee convergence to the global optimum, and it may also increase the complexity of the search space .