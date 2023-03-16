# Genetic operators

Genetic operators are the mechanisms that guide the genetic algorithm towards a solution to a given problem. They are inspired by the natural processes of evolution, such as selection, crossover and mutation  .

## Selection

Selection is the process of choosing the individuals from the current population that will be used to produce the next generation. The selection operator is based on the principle of survival of the fittest, which means that the individuals with higher fitness values have a higher chance of being selected .

There are different methods of selection, such as:

- Roulette wheel selection: Each individual is assigned a probability proportional to its fitness value, and then a random number is used to select an individual from the population.
- Tournament selection: A subset of individuals is randomly chosen from the population, and then the best one among them is selected. This process is repeated until the desired number of individuals is obtained.
- Rank selection: The individuals are sorted according to their fitness values, and then assigned a probability based on their rank. The higher the rank, the higher the probability of being selected.
- Elitism: The best individuals from the current population are directly copied to the next generation, without undergoing any genetic operators.

## Crossover

Crossover is the process of combining two individuals from the selected population to produce one or more offspring. The crossover operator is based on the idea of recombination, which means that the offspring inherit some characteristics from both parents  .

There are different types of crossover, such as:

- One-point crossover: A random point is chosen along the length of the individuals, and then the segments before and after the point are swapped between the parents to create two offspring.
- Two-point crossover: Two random points are chosen along the length of the individuals, and then the segments between the points are swapped between the parents to create two offspring.
- Uniform crossover: A random mask of bits is generated, and then the bits that match the mask are swapped between the parents to create two offspring.
- Arithmetic crossover: A random weight is generated, and then the offspring are created by applying a linear combination of the parents using the weight.

## Mutation

Mutation is the process of introducing random changes in the individuals of the population. The mutation operator is based on the concept of variation, which means that the offspring may have some characteristics that are different from both parents  .

There are different methods of mutation, such as:

- Bit-flip mutation: A random bit in the individual is flipped from 0 to 1 or vice versa.
- Swap mutation: Two random positions in the individual are swapped.
- Insertion mutation: A random position in the individual is chosen, and then a new value is inserted at that position.
- Inversion mutation: A random segment in the individual is chosen, and then reversed.