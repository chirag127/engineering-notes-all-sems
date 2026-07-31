# Mutation

Mutation is one of the operators of genetic algorithm (GA) that introduces diversity into the population of chromosomes. It randomly alters the values of some genes in a chromosome, creating a new solution candidate. Mutation helps to avoid premature convergence and explore new regions of the search space.

## Mutation for binary-coded GA

A common way of implementing mutation for binary-coded GA is to flip each bit in a chromosome with a certain probability, usually very low. For example, if the mutation probability is 0.01, then each bit has a 1% chance of being inverted. This can be done by generating a random number between 0 and 1 for each bit and comparing it with the mutation probability. If the random number is less than or equal to the mutation probability, the bit is flipped; otherwise, it remains unchanged.

For example, suppose we have a chromosome with 10 bits:

`1010010110`

If we apply mutation with a probability of 0.01, we may get the following result:

`1010010110` -> `1010010111`

Only the last bit was flipped, as it was the only one that had a random number less than or equal to 0.01.

## Mutation for real-valued GA

For real-valued GA, where the genes are continuous numbers, mutation can be implemented in different ways. One of the simplest methods is to add a small random value to each gene, drawn from a normal distribution with mean zero and a given standard deviation. The standard deviation controls the magnitude of the mutation and can be fixed or adaptive. Adaptive mutation means that the standard deviation changes according to some criteria, such as the fitness of the chromosome, the diversity of the population, or the number of generations.

For example, suppose we have a chromosome with 3 real-valued genes:

`[1.23, -4.56, 3.14]`

If we apply mutation with a fixed standard deviation of 0.1, we may get the following result:

`[1.23, -4.56, 3.14]` -> `[1.18, -4.49, 3.11]`

Each gene was slightly perturbed by adding a random value from a normal distribution with mean zero and standard deviation 0.1.

## References

: Mutation (genetic algorithm) - Wikipedia
: Adaptive Mutation in Genetic Algorithm With Python Examples
: Mutation Algorithms for Real-Valued Parameters (GA)
: Genetic algorithm - Wikipedia
: Genetic Algorithms - Mutation - tutorialspoint.com