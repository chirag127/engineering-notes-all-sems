 Here is the content in markdown format for the flow chart of Genetic Algorithm(GA) for the notes of Unit 5 - Genetic Algorithm(GA) in the subject of Application of Soft Computing:

### Flow chart of Genetic Algorithm(GA)

1. Start
2. Initialize population
- Randomly generate initial population of chromosomes(solutions)
- Evaluate fitness of each chromosome

3. Selection
- Select fitter chromosomes from population to breed next generation
- Higher fitness has higher chance of getting selected
- Selection methods: Roulette wheel selection, Tournament selection, etc.

4. Crossover
- Crossover parent chromosomes to produce offspring
- Offspring inherit traits from parents
- Single point crossover, Multi-point crossover, Uniform crossover, etc.

5. Mutation
- Randomly mutate offspring chromosomes
- Mutation adds diversity to population
- Flip bits or adjust values of genes in chromosome

6. Evaluate population
- Evaluate fitness of offspring chromosomes
- Include offspring in population
- Remove weaker chromosomes from previous generation

7. Check termination criteria
- If termination criteria is met, stop and return best solution
- Else go to step#3

8. End

The flow chart can be represented pictorially as:

[A pictorial representation of the flow chart can be included here]

Advantages:
- Guaranteed to find a solution
- Uses probabilistic transition rules, not deterministic
- Explores entire solution space
- Can solve complex problems with large solution spaces

Disadvantages:
- May take long time to converge to optimal solution
- May get stuck in local optima
- Sensitive to parameters like population size, crossover rate, mutation rate, etc.

Applications:
- Function optimization
- Machine learning
- Scheduling
- Pattern recognition
- Robotics
- Engineering design
- Etc.