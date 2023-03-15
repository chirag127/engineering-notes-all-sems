### Informed Search

Informed search is a type of search algorithm that uses problem-specific knowledge to find solutions more efficiently than uninformed search methods. This knowledge is used to estimate the cost of reaching a goal state from a given state, allowing the algorithm to make more informed decisions about which states to explore.

Some common informed search algorithms include:

1. **Best-first search:** This algorithm uses an evaluation function to determine the order in which states are expanded. The evaluation function assigns a value to each state based on its estimated distance from the goal state, with lower values being more desirable. States with the lowest evaluation values are expanded first.

2. **Greedy search:** This is a type of best-first search that uses a heuristic function to estimate the cost of reaching the goal state from a given state. The heuristic function provides an estimate of the distance between the current state and the goal state, and states with lower heuristic values are expanded first.

3. **A* search:** This is another type of best-first search that combines the use of a heuristic function with the actual cost of reaching the current state from the start state. The evaluation function for A* is the sum of the heuristic value and the actual cost, and states with the lowest evaluation values are expanded first.

These are just a few examples of informed search algorithms. There are many other variations and techniques that can be used to improve the efficiency of search in problem-solving.