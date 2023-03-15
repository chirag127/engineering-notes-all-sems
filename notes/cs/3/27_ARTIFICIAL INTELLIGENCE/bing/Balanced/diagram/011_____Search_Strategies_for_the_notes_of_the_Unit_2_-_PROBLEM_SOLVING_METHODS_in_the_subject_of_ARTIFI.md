### Search Strategies for Artificial Intelligence

- Search strategies are methods to find solutions to problems in artificial intelligence (AI) by exploring the search space systematically or heuristically.
- Search space is the set of all possible states and actions that can be reached from the initial state by applying the problem rules.
- Search strategies can be classified into two categories: uninformed and informed.
- Uninformed search strategies do not use any domain-specific knowledge or heuristic function to guide the search. They are also called blind or brute-force search strategies.
- Informed search strategies use a heuristic function that estimates the cost or distance to the goal state from any given state. They are also called heuristic or intelligent search strategies.
- The basic uninformed search strategies are:
  - Breadth-first search (BFS): It expands the shallowest node in the frontier (the set of unexplored nodes) first. It is optimal (finds the shortest path) and complete (finds a solution if one exists) but has high space and time complexity.
  - Depth-first search (DFS): It expands the deepest node in the frontier first. It is not optimal (may find a longer path) and not complete (may get stuck in loops or infinite branches) but has low space and moderate time complexity.
  - Depth-limited search (DLS): It is a variant of DFS that limits the depth of the search to a predefined value. It avoids the problem of infinite branches but may miss the solution if it is deeper than the limit.
  - Iterative deepening depth-first search (IDDFS): It is a combination of BFS and DFS that performs DLS with increasing depth limits until a solution is found or the search space is exhausted. It is optimal, complete, and has low space and moderate time complexity.
  - Uniform-cost search (UCS): It expands the node with the lowest path cost from the initial state to the node. It is optimal and complete but has high space and time complexity.
  - Bidirectional search (BDS): It performs two simultaneous searches: one from the initial state to the goal state and one from the goal state to the initial state. It stops when the two searches meet in the middle. It is optimal and complete but has high space and time complexity and requires the goal state to be known in advance.
- The basic informed search strategies are:
  - Greedy search (best first search): It expands the node that appears to be closest to the goal state according to the heuristic function. It is not optimal and not complete but has low space and time complexity.
  - A* search: It expands the node that has the lowest estimated total cost, which is the sum of the path cost and the heuristic cost. It is optimal and complete if the heuristic function is admissible (never overestimates the true cost) and consistent (satisfies the triangle inequality). It has high space and moderate time complexity.