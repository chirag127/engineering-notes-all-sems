# Unit 2 - PROBLEM SOLING METHODS in ARTIFICIAL INTELLIGENCE

### Informed Search
Informed search is a search strategy that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal from a given state, and this estimate is used to guide the search process.

Some common informed search methods include:
- **Best-first search:** This method uses an evaluation function to determine the order in which nodes are expanded. The evaluation function assigns a value to each node based on the estimated cost of reaching the goal from that node. The node with the lowest value is expanded first.
- **Greedy search:** This is a type of best-first search that uses a heuristic function to estimate the cost of reaching the goal from a given node. The heuristic function provides an estimate of the distance from the node to the goal, and the node with the lowest estimated distance is expanded first.
- **A* search:** This is another type of best-first search that combines the cost of reaching a node from the start state with the estimated cost of reaching the goal from that node. The evaluation function for A* search is the sum of these two costs, and the node with the lowest value is expanded first.

Informed search methods can be more efficient than uninformed search methods because they use problem-specific knowledge to guide the search process. However, the quality of the solution found by an informed search method depends on the accuracy of the heuristic function used to estimate the cost of reaching the goal. If the heuristic function is not accurate, the search process may not find the optimal solution.