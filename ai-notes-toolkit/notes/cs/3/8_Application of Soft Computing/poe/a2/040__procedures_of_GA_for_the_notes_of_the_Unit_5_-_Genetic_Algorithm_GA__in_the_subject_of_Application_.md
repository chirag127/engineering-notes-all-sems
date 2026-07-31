 Here is the content in markdown format with formal tone and without any emojis or external links:

### Procedures of Genetic Algorithm (GA)

1. Generate initial population
- Randomly generate N chromosomes (solutions)
- Each chromosome represents a possible solution to the problem

2. Evaluate fitness
- Evaluate the fitness f(x) of each chromosome x in the population
- The fitness function represents the quality of the solution x

3. Select parents
- Select chromosome pairs as parents for breeding based on their fitness
- Higher fitness chromosomes have higher chances of being selected
- Selection methods: Roulette wheel selection, Rank selection, Tournament selection, etc.

4. Breed new offspring
- Perform crossover on the selected parent pairs to breed new offspring
- Crossover involves combining parts of both parents to generate new offspring
- Mutation is applied on new offspring with a low probability to maintain diversity

5. Repeat
- Repeat steps#2, #3 and #4 until termination condition is met
- The termination condition could be satisfying fitness criteria, number of iterations, etc.
- The chromosome with highest fitness is the optimal solution

The above are the key steps involved in the working of a basic Genetic Algorithm. The optimal solution is achieved over multiple iterations through processes of fitness-based selection and breeding.