Test data generation using genetic algorithm is a technique that automates the process of creating test data that can cover different aspects of the software under test, such as statements, branches, paths, or definition-use pairs. A genetic algorithm is a heuristic that mimics the evolution of natural species in searching for the optimal solution to a problem. In this case, the problem is to find test data that can satisfy a given test criterion, such as executing a specific line of code or branch. A genetic algorithm works by creating an initial population of test data, evaluating their fitness according to how well they satisfy the test criterion, and applying genetic operators such as selection, crossover, and mutation to generate new test data until a termination condition is met.

The following diagram illustrates the basic architecture of a test data generation using genetic algorithm:

```
+-----------------+     +-----------------+     +-----------------+
| Initial         |     | Fitness         |     | Selection       |
| population      |---->| evaluation      |---->|                 |----+
+-----------------+     +-----------------+     +-----------------+    |
                                                                         |
+-----------------+     +-----------------+     +-----------------+    |
| Crossover       |<----| Termination     |<----| Mutation        |<---+
|                 |---->| condition       |---->|                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows the main steps of the algorithm:

- Initial population: The algorithm randomly generates a set of test data as the initial population.
- Fitness evaluation: The algorithm evaluates the fitness of each test data according to how well it satisfies the test criterion. For example, if the test criterion is to execute a specific branch, the fitness can be measured by the distance between the test data and the branch condition.
- Selection: The algorithm selects a subset of test data from the current population based on their fitness values. The selection process can use different methods, such as roulette wheel, tournament, or rank-based selection.
- Crossover: The algorithm combines two test data from the selected subset to create a new test data. The crossover process can use different methods, such as one-point, two-point, or uniform crossover.
- Mutation: The algorithm randomly modifies some test data from the selected subset to create a new test data. The mutation process can use different methods, such as bit-flip, swap, or insert mutation.
- Termination condition: The algorithm checks if a termination condition is met, such as reaching a maximum number of iterations, finding a test data that satisfies the test criterion, or reaching a fitness threshold. If the termination condition is met, the algorithm stops and returns the best test data. Otherwise, the algorithm repeats the steps from fitness evaluation to mutation.