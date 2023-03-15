# Local Search Algorithms and Optimization Problems

## Introduction

- Local search algorithms are a type of heuristic search methods that operate on a single current state and move to a neighboring state if it improves the objective function.
- Local search algorithms are widely used for solving large and complex optimization problems, where the goal is to find a solution that maximizes or minimizes a given criterion.
- Local search algorithms do not keep track of the path or the search history, and only focus on the quality of the current state.
- Local search algorithms can be applied to problems that can be formulated as finding a solution in a set of complete configurations, such as the traveling salesman problem, the n-queens problem, the satisfiability problem, etc .

## Characteristics of Local Search Algorithms

- Local search algorithms have the following characteristics :
  - They are incomplete, meaning they do not guarantee to find an optimal solution or any solution at all.
  - They are anytime, meaning they can return a solution at any point during the search and improve it over time.
  - They are memoryless, meaning they do not store any information about the previous states or the search history.
  - They are stochastic, meaning they use randomness to explore the search space and escape from local optima.
  - They are adaptive, meaning they can adjust their parameters or behavior based on the feedback from the objective function.

## Types of Local Search Algorithms

- There are different types of local search algorithms, depending on how they select the next state to move to :
  - Hill-climbing: It moves to the best neighboring state that improves the objective function, and stops when no improvement is possible.
  - Simulated annealing: It moves to a random neighboring state, and accepts it with a probability that depends on the difference in the objective function and a decreasing temperature parameter.
  - Tabu search: It moves to the best neighboring state that is not in a tabu list, which is a short-term memory of the recently visited states, and updates the list periodically.
  - Genetic algorithms: They maintain a population of states, and generate new states by applying crossover and mutation operators, and selecting the fittest states according to the objective function.
  - Local beam search: It maintains a fixed number of states, and generates new states by applying a successor function to each state, and selecting the best states according to the objective function.