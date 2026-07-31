### Informed Search

Informed search is a type of search algorithm that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal state from a given state, allowing the algorithm to make more informed decisions about which states to explore.

Some common informed search algorithms include:

1. **Best-first search:** This algorithm selects the most promising node for expansion based on an evaluation function. The evaluation function assigns a value to each node, representing the estimated cost of reaching the goal from that node.

2. **Greedy search:** This is a type of best-first search that uses a heuristic function to estimate the cost of reaching the goal from a given node. The heuristic function is problem-specific and provides an estimate of the distance to the goal.

3. **A* search:** This is another type of best-first search that combines the cost of reaching a node from the start state with the estimated cost of reaching the goal from that node. The evaluation function for A* search is the sum of the cost to reach the node and the heuristic estimate of the cost to reach the goal.

These are some of the informed search methods used in artificial intelligence for problem-solving. They can be applied to a variety of problems to find solutions more efficiently than uninformed search methods.