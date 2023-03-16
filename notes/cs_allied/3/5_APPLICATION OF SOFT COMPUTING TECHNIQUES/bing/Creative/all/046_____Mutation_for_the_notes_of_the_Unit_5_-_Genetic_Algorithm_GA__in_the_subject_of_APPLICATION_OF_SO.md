# Mutation

- Mutation is a genetic operator that alters one or more gene values in a chromosome from its initial state. It is used to introduce diversity and avoid premature convergence in the population of chromosomes .
- Mutation can be applied to different types of chromosomes, such as binary, integer, real-valued, or permutation. Depending on the type, different mutation operators can be used, such as bit-flip, swap, inversion, or Gaussian mutation .
- Mutation is usually applied with a low probability, denoted by pm, to avoid disrupting the good solutions found by crossover. The probability can be fixed, adaptive, or self-adaptive .
- Mutation can help the genetic algorithm to explore new regions of the search space and escape from local optima. However, mutation can also increase the complexity and size of the search space, making it harder to find the global optimum .