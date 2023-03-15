### Informed Search

Informed search is a type of search algorithm that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal state from a given state, and this estimate is used to guide the search process. Some common informed search algorithms include:

1. **Best-first search:** This algorithm uses an evaluation function to determine the order in which nodes are expanded. The evaluation function assigns a value to each node based on the estimated cost of reaching the goal state from that node. The node with the lowest evaluation value is expanded first.

2. **Greedy search:** This is a type of best-first search that uses a heuristic function to estimate the cost of reaching the goal state from a given node. The heuristic function provides an estimate of the distance between the current node and the goal state. The node with the lowest heuristic value is expanded first.

3. **A* search:** This is another type of best-first search that combines the cost of reaching the current node from the start node with the estimated cost of reaching the goal state from the current node. The evaluation function for A* search is the sum of these two costs. The node with the lowest evaluation value is expanded first.

4. **Iterative deepening A* (IDA*):** This is a variation of A* search that uses iterative deepening to control the amount of memory used by the search process. At each iteration, the maximum depth of the search is increased, and nodes at that depth are expanded using the A* evaluation function.

These are some of the informed search methods used in artificial intelligence for problem-solving. They can be applied to a wide range of problems to find solutions more efficiently than uninformed search methods.