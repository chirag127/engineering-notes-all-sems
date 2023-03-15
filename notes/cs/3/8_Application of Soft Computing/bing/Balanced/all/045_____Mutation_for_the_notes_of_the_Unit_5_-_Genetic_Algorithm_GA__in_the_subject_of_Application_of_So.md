# Mutation

- Mutation is a genetic operator that alters one or more gene values in a chromosome.
- The purpose of mutation is to introduce diversity into the population and to prevent premature convergence to a suboptimal solution .
- Mutation is usually applied with a low probability, denoted by pm, to avoid excessive disruption of the population.
- Mutation can be implemented in different ways depending on the representation of the chromosomes and the problem domain .
- Some common types of mutation are:
  - Bit flip mutation: A random bit in a binary coded chromosome is inverted.
  - Swap mutation: Two random genes in a permutation coded chromosome are swapped.
  - Uniform mutation: A random gene in a real-valued chromosome is replaced by a random value from a uniform distribution.
  - Gaussian mutation: A random gene in a real-valued chromosome is perturbed by a random value from a Gaussian distribution.
  - Adaptive mutation: The mutation probability or the mutation step size is adjusted dynamically based on some criteria, such as fitness, diversity, or generation number.