# Local Search Algorithms and Optimization Problems

## Introduction

- Local search algorithms are a type of heuristic search methods that operate on a single current state and move to a neighboring state if it improves the objective function.
- Local search algorithms do not keep a search tree or a list of visited states, and therefore use less memory and can handle large state spaces.
- Local search algorithms are often used for solving optimization problems, where the goal is to find a state that maximizes or minimizes a given criterion, such as cost, profit, distance, etc.
- Optimization problems can be classified into two types: discrete and continuous. Discrete optimization problems have a finite number of possible states, while continuous optimization problems have an infinite number of possible states.
- Examples of optimization problems are: traveling salesman problem, knapsack problem, scheduling problem, etc.

## Local Search Strategies

- A local search strategy defines how to select a neighboring state from the current state, and when to terminate the search.
- Some common local search strategies are:

  - Hill-climbing: This strategy always moves to the best neighboring state, i.e., the one that has the highest value of the objective function. It terminates when it reaches a local maximum, where no neighbor has a better value. Hill-climbing can get stuck in local maxima, plateaus, or ridges.
  - Simulated annealing: This strategy is inspired by the physical process of annealing, where a metal is heated and then slowly cooled to reach a low-energy state. Simulated annealing starts with a high temperature, which allows it to move to any neighboring state, even if it has a lower value. As the temperature decreases, the probability of moving to a worse state decreases, and the search becomes more greedy. Simulated annealing can escape local maxima, but it requires a careful choice of the cooling schedule and the termination condition.
  - Tabu search: This strategy maintains a list of recently visited states, called the tabu list, and avoids revisiting them. This prevents the search from cycling back to previous states, and encourages exploration of new regions of the state space. Tabu search can overcome local maxima, but it needs a suitable size and update rule for the tabu list, and a stopping criterion.
  - Genetic algorithms: This strategy is inspired by the biological process of evolution, where a population of individuals undergoes reproduction, mutation, and selection. Genetic algorithms start with a random population of states, and generate new states by combining parts of two parent states (crossover) or randomly modifying a state (mutation). The new states are then evaluated by the objective function, and the best ones are selected to form the next generation. Genetic algorithms can explore a large and diverse set of states, but they require a good representation of states, and a balance between exploration and exploitation.

## Evaluation of Local Search Algorithms

- Local search algorithms can be evaluated by the following criteria:

  - Quality of solution: This measures how close the final state is to the global optimum, or how well it satisfies the objective function. Quality of solution depends on the problem domain, the objective function, and the local search strategy.
  - Efficiency: This measures how fast the algorithm can find a good solution, or how many iterations or evaluations it takes. Efficiency depends on the size and structure of the state space, the neighborhood function, and the local search strategy.
  - Robustness: This measures how well the algorithm can handle different instances of the same problem, or how sensitive it is to the initial state, the random choices, or the parameter settings. Robustness depends on the diversity and complexity of the problem instances, and the local search strategy.