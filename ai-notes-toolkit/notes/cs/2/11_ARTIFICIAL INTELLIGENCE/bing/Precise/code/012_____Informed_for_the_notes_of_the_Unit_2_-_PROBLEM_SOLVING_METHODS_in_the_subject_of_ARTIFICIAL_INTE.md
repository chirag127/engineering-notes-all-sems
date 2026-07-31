### Informed Search
Informed search, also known as heuristic search, is a type of search algorithm that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal state from a given state, and this estimate is used to guide the search process.

Some common informed search algorithms include:
- **Best-first search:** This algorithm uses a heuristic function to evaluate the desirability of each state and selects the most promising state to expand.
- **A* search:** This algorithm is a type of best-first search that uses a combination of the cost of reaching a state and the estimated cost of reaching the goal from that state to guide the search process.
- **Greedy search:** This algorithm is similar to best-first search, but it only considers the estimated cost of reaching the goal from a given state, ignoring the cost of reaching that state.
- **Iterative deepening A* (IDA*):** This algorithm is a variation of A* search that uses iterative deepening to control the amount of memory used by the search process.

Informed search methods can be very effective in solving problems where problem-specific knowledge is available. However, the quality of the solutions found by these methods depends on the accuracy of the heuristic function used to guide the search process. If the heuristic function is not accurate, the search process may not find the optimal solution or may take longer to find a solution.