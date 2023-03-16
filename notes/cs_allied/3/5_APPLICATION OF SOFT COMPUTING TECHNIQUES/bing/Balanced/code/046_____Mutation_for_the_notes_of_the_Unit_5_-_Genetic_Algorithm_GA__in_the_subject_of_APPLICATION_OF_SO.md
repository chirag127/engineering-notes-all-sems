### Mutation

- Mutation is a genetic operator that alters one or more gene values in a chromosome from its initial state. 
- Mutation is used to introduce and maintain diversity in the population of candidate solutions.  
- Mutation helps to avoid premature convergence to local optima by exploring new regions in the search space.  
- Mutation is usually applied with a low probability, as too much mutation can disrupt the good solutions and reduce the performance of the genetic algorithm.  
- Mutation can be implemented in different ways depending on the representation of the chromosomes and the problem domain. 
- Some common types of mutation are:
  - Bit flip mutation: This is used for binary coded chromosomes, where each bit has a probability of being inverted from 0 to 1 or vice versa.  
  - Swap mutation: This is used for permutation based chromosomes, where two genes are randomly selected and swapped. This is useful for problems like the traveling salesman problem. 
  - Uniform mutation: This is used for real-valued chromosomes, where each gene is replaced by a random value from a uniform distribution within a predefined range.  
  - Gaussian mutation: This is also used for real-valued chromosomes, where each gene is perturbed by adding a random value from a normal distribution with a mean of zero and a standard deviation of sigma.  
  - Adaptive mutation: This is a technique where the mutation probability or the mutation parameters are dynamically adjusted according to some criteria, such as the fitness of the population, the diversity of the population, or the progress of the search.