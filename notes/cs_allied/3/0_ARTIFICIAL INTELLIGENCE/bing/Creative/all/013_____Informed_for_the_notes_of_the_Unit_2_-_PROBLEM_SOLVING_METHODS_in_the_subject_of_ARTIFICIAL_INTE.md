# Informed Search

Informed search is a type of problem-solving technique in artificial intelligence that uses additional information or heuristics to guide the search process towards the goal state. Informed search algorithms are also called heuristic search algorithms. Heuristics are estimates of the cost or distance from the current state to the goal state. Heuristics help to reduce the search space and find the optimal solution faster and more efficiently.

Some of the common informed search algorithms are:

- **Best-first search**: This algorithm selects the node with the lowest heuristic value for expansion. It uses a priority queue to store the nodes according to their heuristic values. It is also called greedy search because it always chooses the most promising node. Best-first search is not guaranteed to find the optimal solution, and it may get stuck in local minima.

- **A* search**: This algorithm combines the heuristic value of the node with the actual cost of reaching the node from the start state. It uses the formula f(n) = g(n) + h(n), where f(n) is the evaluation function, g(n) is the cost function, and h(n) is the heuristic function. A* search is guaranteed to find the optimal solution if the heuristic function is admissible, meaning it never overestimates the true cost to the goal.

- **Iterative deepening A* (IDA*) search**: This algorithm is a variation of A* search that uses iterative deepening to limit the memory usage. It starts with a threshold value equal to the heuristic value of the start node, and expands only the nodes whose f(n) value is less than or equal to the threshold. If the goal is not found, the threshold is increased to the minimum f(n) value of the nodes that were pruned. IDA* search is also guaranteed to find the optimal solution if the heuristic function is admissible.

- **Recursive best-first search (RBFS)**: This algorithm is another variation of A* search that uses recursion to limit the memory usage. It keeps track of the f(n) value of the best alternative path for each node along the current path. It expands the node with the lowest f(n) value, and backtracks if the f(n) value of the current node exceeds the f(n) value of the best alternative path. RBFS is also guaranteed to find the optimal solution if the heuristic function is admissible.