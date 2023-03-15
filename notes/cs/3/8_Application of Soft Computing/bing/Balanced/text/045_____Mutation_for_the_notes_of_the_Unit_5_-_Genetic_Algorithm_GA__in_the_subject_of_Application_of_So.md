### Mutation

- Mutation is a genetic operator that alters one or more gene values in a chromosome.
- The purpose of mutation is to introduce diversity into the population and to prevent premature convergence to a suboptimal solution .
- Mutation is usually applied with a low probability to avoid disrupting the good solutions found by crossover and selection .
- The mutation probability can be fixed or adaptive, depending on the problem and the algorithm.
- There are different types of mutation operators for different types of chromosomes, such as binary, real-valued, permutation, etc .
- Some examples of mutation operators are:
  - Bit flip mutation: A random bit in a binary chromosome is flipped from 0 to 1 or vice versa.
  - Uniform mutation: A random gene in a real-valued chromosome is replaced by a random value from a uniform distribution.
  - Swap mutation: Two random genes in a permutation chromosome are swapped.
- Mutation is a trade-off between exploration and exploitation of the search space. Too much mutation can lead to loss of good solutions, while too little mutation can lead to stagnation of the population.