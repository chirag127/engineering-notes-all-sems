# Unit 2 - PROBLEM SOLING METHODS in ARTIFICIAL INTELLIGENCE

## Informed Search

Informed search is a type of search algorithm that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal state from a given state, and this estimate is used to guide the search process.

Some common informed search algorithms include:
- **Best-first search:** This algorithm uses an evaluation function to determine the order in which nodes are expanded. The evaluation function assigns a value to each node based on the estimated cost of reaching the goal state from that node. The node with the lowest evaluation value is expanded first.
- **A* search:** This is a best-first search algorithm that uses an admissible heuristic function to estimate the cost of reaching the goal state from a given node. The heuristic function must never overestimate the actual cost of reaching the goal state. A* search is guaranteed to find an optimal solution if one exists.
- **Greedy search:** This is a best-first search algorithm that uses a heuristic function to estimate the cost of reaching the goal state from a given node. The node with the lowest heuristic value is expanded first. Greedy search is not guaranteed to find an optimal solution.

Informed search algorithms can be more efficient than uninformed search algorithms because they use problem-specific knowledge to guide the search process. However, the quality of the solution found by an informed search algorithm depends on the quality of the heuristic function used. A good heuristic function can significantly reduce the search time, while a poor heuristic function can result in longer search times or even failure to find a solution.