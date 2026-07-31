### Mutation

- Mutation is a genetic operator that alters one or more gene values in a chromosome from its initial state. It is used to introduce diversity and avoid premature convergence in the population of candidate solutions.
- Mutation can be applied to different types of representations, such as binary, integer, real-valued, or permutation. Depending on the representation, different mutation operators can be used, such as bit-flip, swap, inversion, or Gaussian mutation .
- Mutation is usually applied with a low probability, denoted by *p<sub>m</sub>*. This means that each gene has a small chance of being mutated. The mutation probability can be fixed, adaptive, or self-adaptive.
- Mutation can help the genetic algorithm to explore new regions of the search space and escape from local optima. However, if the mutation rate is too high, it can disrupt the good building blocks and reduce the convergence speed. Therefore, a balance between exploration and exploitation is needed .