 Here is the content in markdown format for the topic - ### Working principle of Genetic Algorithm (GA):

1. **Representation of chromosomes:** The solution to the problem is represented as chromosomes (string of 0s and 1s) whose lengths are equal to the number of variables in the problem.

2. **Population of chromosomes:** A set of chromosomes forms the population. The population size is selected by the user.

3. **Fitness calculation:** The fitness value of each chromosome is calculated using the fitness function. The chromosomes with high fitness values have more chances of survival.

4. **Selection:** The fittest chromosomes are selected from the population to produce offspring for the next generation. Selection is done using selection methods like roulette wheel selection or tournament selection.

5. **Crossover:** The selected chromosomes undergo crossover to produce offspring. Crossover is done at randomly selected crossover points. The offspring inherits traits from both the parents.

6. **Mutation:** Mutation is applied to the offspring with a low mutation probability to introduce randomness and generate variety. The values of some genes in the offspring are flipped.

7. **New population:** The offspring are combined with the existing population and the population for the next generation is formed.

8. **Stopping criteria:** If the stopping criteria (maximum number of generations or achieving sufficient fitness) is satisfied, then the algorithm stops, otherwise steps 3-7 are repeated.

The best chromosome gives the optimal solution to the problem.

Some advantages of GA are:
- They work on coding of parameters, not the parameters themselves. Hence, they can be applied to a wide variety of problems.
- They search a large space of possible solutions in parallel.
- They can often find an acceptable solution quickly.

[Representation of ASCII diagrams, examples, codes, applications, etc can be added here if required.]