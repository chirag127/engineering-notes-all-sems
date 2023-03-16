### Informed Search

Informed search is a type of search algorithm that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal state from a given state, and this estimate is used to guide the search process.

Some common informed search methods include:

1. **Best-first search:** This algorithm uses an evaluation function to determine the order in which nodes are expanded. The evaluation function assigns a value to each node based on the estimated cost of reaching the goal state from that node. The node with the lowest evaluation value is expanded first.

2. **Greedy search:** This is a type of best-first search that uses a heuristic function to estimate the cost of reaching the goal state from a given node. The heuristic function provides an estimate of the distance between the current node and the goal state. The node with the lowest heuristic value is expanded first.

3. **A* search:** This is another type of best-first search that combines the cost of reaching the current node from the start node with the estimated cost of reaching the goal state from the current node. The evaluation function for A* search is the sum of these two costs. The node with the lowest evaluation value is expanded first.

These are some of the informed search methods used in problem solving in the field of artificial intelligence. They can be applied to a wide range of problems to find solutions more efficiently than uninformed search methods.