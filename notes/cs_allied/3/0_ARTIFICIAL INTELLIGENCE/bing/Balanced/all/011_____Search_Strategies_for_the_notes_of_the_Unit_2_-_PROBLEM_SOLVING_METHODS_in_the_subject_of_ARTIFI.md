# Search Strategies

Search strategies are methods of finding solutions to problems by exploring the space of possible states and actions. Search strategies can be classified into two categories: uninformed search and informed search.

## Uninformed Search

Uninformed search strategies do not use any domain-specific knowledge or heuristics to guide the search. They only use the problem definition, which specifies the initial state, the goal state, and the actions that can be performed in each state. Uninformed search strategies are also called blind search or brute-force search. Some examples of uninformed search strategies are:

- Breadth-first search: It expands the shallowest nodes first, i.e., the nodes that are closest to the root of the search tree. It is optimal (finds the shortest path to the goal) and complete (guarantees to find a solution if one exists), but it is memory-intensive and may take a long time to find a solution.
- Depth-first search: It expands the deepest nodes first, i.e., the nodes that are farthest from the root of the search tree. It is not optimal (may find a longer path to the goal) and not complete (may get stuck in infinite loops or dead ends), but it is memory-efficient and may find a solution quickly.
- Uniform-cost search: It expands the nodes with the lowest path cost first, i.e., the nodes that have the smallest sum of the costs of the actions from the root to the node. It is optimal and complete, but it is memory-intensive and may take a long time to find a solution.
- Depth-limited search: It is a variation of depth-first search that imposes a limit on the depth of the search tree. It is not optimal and not complete, but it avoids infinite loops and dead ends, and it is memory-efficient.
- Iterative deepening search: It is a combination of breadth-first search and depth-limited search. It performs a series of depth-limited searches with increasing depth limits until a solution is found or the search space is exhausted. It is optimal, complete, memory-efficient, and time-efficient.

## Informed Search

Informed search strategies use domain-specific knowledge or heuristics to guide the search. They estimate the cost or the quality of the nodes and select the most promising ones to expand. Informed search strategies are also called heuristic search or guided search. Some examples of informed search strategies are:

- Greedy best-first search: It expands the node that is closest to the goal, according to a heuristic function that estimates the distance from the node to the goal. It is not optimal and not complete, but it is fast and may find a solution quickly.
- A* search: It expands the node that has the lowest estimated total cost, according to a heuristic function that estimates the sum of the path cost from the root to the node and the distance from the node to the goal. It is optimal and complete, if the heuristic function is admissible (never overestimates the distance to the goal) and consistent (satisfies the triangle inequality), but it is memory-intensive and may take a long time to find a solution.
- Hill-climbing search: It is a local search strategy that starts from a random initial state and moves to a neighboring state that has a higher value, according to a heuristic function that evaluates the quality of the states. It is not optimal and not complete, but it is fast and may find a local optimum quickly.
- Simulated annealing search: It is a variation of hill-climbing search that allows some downhill moves (moves to a neighboring state that has a lower value) with a probability that decreases over time, according to a temperature parameter that controls the exploration-exploitation trade-off. It is not optimal and not complete, but it is fast and may find a global optimum with a high probability.
- Genetic algorithms: They are population-based search strategies that use the principles of natural selection and genetic recombination to generate new states from a set of existing states. They are not optimal and not complete, but they are fast and may find a near-optimal solution with a high probability.