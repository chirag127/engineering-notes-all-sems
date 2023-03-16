### Search Strategies for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

- Search strategies are methods to find solutions to problems in artificial intelligence (AI) .
- Search strategies can be classified into two types: uninformed and informed .
- Uninformed search strategies do not use any domain-specific knowledge or heuristic function to guide the search. They only use the problem definition and the goal state to explore the search space .
- Uninformed search strategies include:
  - Breadth-first search: It explores the search space level by level, starting from the root node and expanding all its children nodes, then all their children nodes, and so on .
  - Depth-first search: It explores the search space branch by branch, starting from the root node and expanding one of its children nodes, then one of its grandchildren nodes, and so on, until it reaches a goal state or a dead end. Then it backtracks and tries another branch .
  - Depth-limited search: It is a variation of depth-first search that limits the maximum depth of the search to avoid infinite loops or irrelevant paths .
  - Iterative deepening depth-first search: It is a combination of breadth-first search and depth-first search that gradually increases the depth limit until a solution is found or the search space is exhausted .
  - Bidirectional search: It is a strategy that searches from both the root node and the goal node simultaneously, and stops when the two searches meet in the middle .
  - Uniform cost search: It is a strategy that expands the node with the lowest path cost from the root node, where the path cost is the sum of the costs of the actions along the path .
- Informed search strategies use domain-specific knowledge or heuristic function to estimate the cost or the quality of a node or a path, and prioritize the search accordingly .
- Informed search strategies include:
  - Greedy best-first search: It is a strategy that expands the node that is closest to the goal, according to a heuristic function that estimates the distance or the cost from a node to the goal .
  - A* search: It is a strategy that expands the node that has the lowest estimated total cost from the root node to the goal node, according to a heuristic function that combines the path cost from the root node and the distance or the cost to the goal node .
  - Hill climbing search: It is a strategy that moves from the current node to a better neighbor node, according to a heuristic function that evaluates the quality of a node, and stops when it reaches a local maximum or a plateau .
  - Simulated annealing search: It is a strategy that moves from the current node to a random neighbor node, with a probability that depends on the difference in quality between the nodes and a decreasing temperature parameter, and stops when it reaches a global maximum or a minimum temperature .
  - Genetic algorithm: It is a strategy that generates a population of candidate solutions, and iteratively applies selection, crossover, and mutation operators to produce new generations of solutions, until a termination condition is met .