### Search Strategies

Search strategies are methods or algorithms that help an AI agent to solve a problem by finding a path from a start state to a goal state in a search space  . Search strategies can be classified into two types: uninformed and informed.

- Uninformed search strategies do not use any domain-specific knowledge or heuristic function to guide the search. They only use the information available in the problem definition. Examples of uninformed search strategies are breadth-first search, depth-first search, depth-limited search, iterative deepening depth-first search, bidirectional search, and uniform cost search .
- Informed search strategies use some domain-specific knowledge or heuristic function to estimate the cost or distance to the goal state from a given state. They try to find the optimal or near-optimal solution by expanding the most promising nodes first. Examples of informed search strategies are greedy search, A* search, hill climbing, simulated annealing, and genetic algorithms .

Some factors that affect the performance and quality of search strategies are:

- Completeness: whether the algorithm is guaranteed to find a solution if one exists.
- Optimality: whether the algorithm is guaranteed to find the optimal solution (the one with the lowest cost or highest value).
- Time complexity: how long the algorithm takes to find a solution.
- Space complexity: how much memory the algorithm uses to store the search space.