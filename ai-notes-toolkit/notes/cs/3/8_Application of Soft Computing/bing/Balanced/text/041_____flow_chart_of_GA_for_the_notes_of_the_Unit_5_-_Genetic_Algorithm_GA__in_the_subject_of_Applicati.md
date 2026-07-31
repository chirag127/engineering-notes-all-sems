### Flow chart of GA

A flow chart is a graphical representation of the steps involved in a process or an algorithm. A flow chart of GA shows the main components and operations of a genetic algorithm, which is a search-based optimization technique based on the principles of genetics and natural selection.

The following is a possible flow chart of GA for the notes of the Unit 5 - Genetic Algorithm (GA) in the subject of Application of Soft Computing:

- Start
- Initialize a population of candidate solutions (chromosomes) randomly or by using some heuristics
- Evaluate the fitness of each chromosome using a predefined objective function
- Repeat until a termination criterion is met (such as reaching a maximum number of generations, achieving a desired fitness level, or finding an optimal solution):
  - Select a subset of chromosomes (parents) for reproduction using a selection method (such as roulette wheel, tournament, or rank-based)
  - Apply crossover and mutation operators to the parents to generate new chromosomes (offspring)
  - Evaluate the fitness of the offspring using the objective function
  - Replace some or all of the current population with the offspring using a replacement method (such as elitism, generational, or steady-state)
  - Optionally, apply some local search or improvement techniques to the population
- Return the best chromosome (solution) found
- Stop

The following is a possible diagram of the flow chart of GA:

```
+------+     +-----------------+     +-----------------+
| Start|---->| Initialize      |---->| Evaluate        |
+------+     | population      |     | fitness         |
             +-----------------+     +-----------------+
                                              |
                                              V
                                        +-------------+
                                        | Termination |
                                        | criterion   |
                                        | met?        |
                                        +-------------+
                                              |
                                         +----+----+
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         V         |
                                        +-------------+
                                        | Select      |
                                        | parents     |
                                        +-------------+
                                              |
                                              V
                                        +-------------+
                                        | Apply       |
                                        | crossover   |
                                        | and         |
                                        | mutation    |
                                        +-------------+
                                              |
                                              V
                                        +-------------+
                                        | Evaluate    |
                                        | fitness     |
                                        | of          |
                                        | offspring   |
                                        +-------------+
                                              |
                                              V
                                        +-------------+
                                        | Replace     |
                                        | population  |
                                        +-------------+
                                              |
                                              V
                                        +-------------+
                                        | Apply       |
                                        | local       |
                                        | search      |
                                        | (optional)  |
                                        +-------------+
                                              |
                                              |
                                         +----+----+
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         |         |
                                         V         |
                                        +-------------+
                                        | Return      |
                                        | best        |
                                        | solution    |
                                        +-------------+
                                              |
                                              V
                                        +-------------+
                                        | Stop        |
                                        +-------------+
```