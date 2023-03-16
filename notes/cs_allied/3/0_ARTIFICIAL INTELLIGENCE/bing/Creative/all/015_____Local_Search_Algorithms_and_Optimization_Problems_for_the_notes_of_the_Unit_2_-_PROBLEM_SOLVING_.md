# Local Search Algorithms and Optimization Problems

## Introduction

- Local search algorithms are heuristic methods for solving computationally hard optimization problems.
- Optimization problems are problems that require finding a solution that maximizes or minimizes a criterion among a number of candidate solutions.
- Examples of optimization problems are traveling salesman problem, vehicle routing problem, scheduling problem, etc.
- Local search algorithms examine and analyze many solutions (search space) by making local changes until an optimal solution is obtained or a number of iterations are performed.
- Local search algorithms are widely used for big problems and return a good but not optimal solution.
- Local search algorithms are also called iterative improvement algorithms.

## Characteristics of Local Search Algorithms

- Local search algorithms do not keep a search tree, but only a single current state.
- Local search algorithms use a function that evaluates the quality of a state, called objective function or cost function.
- Local search algorithms use a function that generates a set of neighboring states from a given state, called successor function.
- Local search algorithms use a strategy to select a neighbor state from the set of successors, called selection function.
- Local search algorithms use a criterion to terminate the search, called termination condition.
- Local search algorithms can be classified into deterministic or stochastic, depending on whether the selection function is deterministic or random.

## Advantages and Disadvantages of Local Search Algorithms

- Advantages:
  - Local search algorithms are simple to implement and understand.
  - Local search algorithms are efficient in terms of time and space complexity.
  - Local search algorithms can handle large and complex problems that are intractable for other methods.
  - Local search algorithms can be easily combined with other techniques, such as genetic algorithms, simulated annealing, etc.
- Disadvantages:
  - Local search algorithms are sensitive to the initial solution and may get trapped in a local optimum.
  - Local search algorithms do not guarantee to find the global optimum or even a good approximation.
  - Local search algorithms may require a lot of tuning and experimentation to find the best parameters.
  - Local search algorithms may not be suitable for problems that require finding a complete path or sequence of actions, rather than a final state.

## Examples of Local Search Algorithms

- Hill climbing: a simple local search algorithm that moves to the best neighbor state until no improvement is possible.
- Simulated annealing: a stochastic local search algorithm that allows some bad moves to escape from local optima, based on a probabilistic function that decreases with temperature.
- Tabu search: a deterministic local search algorithm that keeps a list of forbidden moves to avoid cycling and diversify the search.
- Genetic algorithms: a population-based local search algorithm that mimics the natural evolution process by applying crossover and mutation operators to a set of candidate solutions.