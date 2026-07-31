# Unit 2 - PROBLEM SOLING METHODS in ARTIFICIAL INTELLIGENCE

### Informed Search

Informed search, also known as heuristic search, is a search strategy that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal state from a given state, and this estimate is used to guide the search process.

Some common informed search algorithms include:
- **Best-first search:** This algorithm uses an evaluation function to determine the order in which nodes are expanded. The evaluation function assigns a value to each node based on the estimated cost of reaching the goal state from that node. The node with the lowest evaluation value is expanded first.
- **A*** search:** This is a best-first search algorithm that uses an admissible heuristic function to estimate the cost of reaching the goal state from a given node. The heuristic function must never overestimate the actual cost of reaching the goal state. A* search is guaranteed to find the optimal solution if one exists.
- **Greedy search:** This is a best-first search algorithm that uses a heuristic function to estimate the cost of reaching the goal state from a given node. The heuristic function is used to guide the search process, but it is not guaranteed to be admissible. Greedy search is not guaranteed to find the optimal solution.
- **Iterative deepening A* (IDA*):** This is a depth-first search algorithm that uses an admissible heuristic function to guide the search process. The algorithm iteratively increases the maximum depth of the search until a solution is found. IDA* is guaranteed to find the optimal solution if one exists.

Informed search methods can be much more efficient than uninformed search methods, but they require problem-specific knowledge to be effective. The quality of the heuristic function used can have a significant impact on the performance of the search algorithm. A good heuristic function can greatly reduce the number of nodes that need to be expanded, while a poor heuristic function can result in a search that is no better than an uninformed search.